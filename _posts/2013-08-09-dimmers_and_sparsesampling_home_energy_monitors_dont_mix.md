---
title: "Dimmers and sparse-sampling home energy monitors don\'t mix"
date: 2013-08-09 15:48:53 +0000
categories: ["PhD", "CurrentCost"]
permalink: /dimmers_and_sparsesampling_home_energy_monitors_dont_mix
---
I have been recording the power consumption of my whole home using two
systems: a Current Cost CT clamp and my home-brew "[sound card power
meter](https://github.com/JackKelly/snd_card_power_meter)". The latter
samples my home's voltage and current waveforms at 44.1kHz and
calculates the apparent and active power once a second.

Most of the time, the signal from the Current Cost CT clamp and my SCPM
agree remarkably well.

One situation where the two systems disagree wildly is when our kitchen
ceiling lights are on. These lights consist of 10 x 10W Philips dimmable
LEDs driven by a cheap TRIAC dimmer. Here's a graph showing a time
period where the lights start off, then turn on, and then turn off
again. The Current Cost reports a rapidly varying power consumption. The
SCPM, on the other hand, reports a very steady power consumption. I have
also plotted the mains voltage to demonstrate that the mains voltage
wasn't doing anything odd during this period:

![](/files/dimmer_wierdness.png)

What's going on? Why does the Current Cost think the kitchen light's
power consumption wobbles up and down wildly? <!--break-->

My sound card power meter records the voltage and current waveforms
(sampled at 44.1kHz and downsampled to 16kHz). Here's one and a half
mains cycles (30ms) of the whole-home current waveform while the kitchen
lights are on:

![](/files/dimmer_wierdness_current_waveform.png)

Pretty spiky, huh?!

My hunch is that the Current Cost CT clamp transmitter sparsely samples
the mains current (to minimise battery usage) and hence outputs a wildly
different answer depending on which part of the current waveform the
transmitter samples. My SCPM system, on the other hand, samples
continuously and hence doesn't suffer from this problem.

