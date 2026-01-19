---
title: "Plotting our solar PV data"
categories: [open science, software engineering, programming, data visualisation, graphs, green
diary, solar]
---

We had 10 solar PV panels installed on our roof in south-east London back in 2022. I've finally
gotten round to writing code to grab live data from our solar system over the local area
network and plot the live data.

This has been a good excuse to try out publishing a simple dashboard
without an SQL database or a server. The visualisation is a [Marimo](https://marimo.io) app, exported as
web assembly. The Python code runs in the browser, and pulls parquet files directly from my cloud
bucket!

The full pipeline currently looks like this:

1. I have a little Linux PC (an [Intel NUC](https://en.wikipedia.org/wiki/Next_Unit_of_Computing))
   running 24/7 at home. It runs [Proxmox](https://www.proxmox.com) (a virtual
   machine host), with two virtual machines:
   One runs [Home Assistant OS](https://github.com/home-assistant/operating-system), the other runs Ubuntu. 
2. I've written a simple little Python package called [`envoy_recorder`](https://github.com/JackKelly/envoy_recorder)
   which runs on the Ubuntu VM. It is triggered by `cron` once a minute. This script:
    1. Grabs data from our Enphase Envoy over the local area network (from `https://envoy.local/ivp/pdm/device_data` - 
       I found this URL by looking through the debug logs for Home Assistant). 
       This returns a JSON object describing lots of measurements for each micro-inverter.
       [Here's some some example JSON returned by my Envoy](https://github.com/JackKelly/envoy_recorder/tree/main/example_envoy_json_data).
    2. Saves this JSON object to disk. The script deliberately doesn't even try to parse the JSON
       yet. I want to make sure we save _something_ to disk, even if it's not valid JSON. These JSON
       files are each about 1.5 kB after compression.
    3. If the set of JSON files is more than 15 minutes old then the code flushes the JSON files to a
       Parquet file locally (it's not possible to append to parquet so we read this month's parquet, append the new data in memory, and save
       this month's parquet back to disk). We also upload the newly update parquet to
       [Cloudflare R2](https://www.cloudflare.com/en-gb/developer-platform/products/r2/)
       (which is free, easy to configure, doesn't charge for egress, and allows for open access over HTTPS).
       A week of Parquet data is only 30 kB. The JSON files are then deleted.
3. To plot my per-inverter PV data, I used Marimo with Altair, and exported the notebook as `html-wasm`, and served the app
   on my blog (which is a Jekyll blog, hosted on GitHub pages). 
   The [dashboard is public](https://jack-kelly.com/solar/). And [here's the source code](https://github.com/JackKelly/home_energy_dashboard).

Whilst I'm super-impressed with a lot of these technologies, there have definitely been some issues
on the way, and - to be honest - I'll probably move away from WASM to hosting my Marimo app on my NUC, and use
a Cloudflare Tunnel to expose my own HTTP server to the world.

## The good bits

I've been using Marimo for a while as a replacement for Jupyter Notebooks. But it's been awesome to
find out that Marimo has some awesome additional features up its sleeve. Marimo makes it super-easy
to make reactive apps. And exporting to WASM and running Python in the browser feels like magic.

## The tricky bits

TBH, running Marimo in the browser as WASM still feels quite "bleeding edge". It definitely hasn't
been the butter-smooth dream I first thought it'd be of magically exporting Python to WASM and it
"just working" in the browser. Python code that runs perfectly on Ubuntu can throw all
sorts of weird and wonderful errors when running on pyodide in the
browser. For example, changing the timezone on a Polars datetime object breaks in WASM
because a specific datetime library isn't available in WASM. In total I probably hit up against
about 10 issues like that, and I wouldn't have had the time to get it working at all without
extensive help from Gemini!

Also, for some reason `Jekyll` and `GitHub Pages` refuse to publish JavaScript files with names that
start with an underscore (and there are lots of those files in `Marimo`'s WASM export!). So I wrote
a quick [script](https://github.com/JackKelly/JackKelly.github.io/blob/master/solar/remove_underscores.py)
to change the filenames, and change any reference to those filenames.

Also, running Marimo in WASM takes about 10 seconds to load in the browser. Which isn't ideal.

I did try using [`molab`](https://molab.marimo.io/notebooks) (the free, hosted service for Marimo
notebooks) but it also takes a while for the app to load. And it felt a bit glitchy, if I'm honest
(e.g. it takes a long time for the app to update after updating the code, and sometimes it didn't
save my edits).

## Next steps

- Create a dataset card on Hugging Face (this will just be a README pointing to my parquet files on
  R2). I'll include all the juicy details of our PV system, so other people can make best use of the
  data.
- Move away from WASM to hosting my Marimo notebook on my NUC.
- Record my home's power demand (at 1-second res) and my heating system's behaviour (using a bunch
  of 1-wire temperature sensors connected to an ESP32), collect it using MQTT, and publish that data too.
- Maybe build a retro physical display, maybe using a vacuum fluorescent display (VFD) "graphic equalizer" :).
