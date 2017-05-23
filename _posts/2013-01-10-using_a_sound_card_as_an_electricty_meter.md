---
title: "Using a sound card as an electricty meter"
date: 2013-01-10 13:04:11 +0000
categories: ["PhD"]
permalink: /using_a_sound_card_as_an_electricty_meter
---
Just some quick notes on using a 20bit 96kHz sound card on Linux (Ubuntu
Server) to sample measurements from a current transformer and AC-AC
adapter.

I followed [this
guide](http://howto.blbosti.com/2010/03/ubuntu-server-install-alsa-sound-and-moc-music-on-console/)
to get audio working on Ubuntu Server. I then tinkered with Audacity
(using X over SSH). (My ultimate plan is to either use arecord to record
the signal or write a Python or C++ program to do the sampling and
processing).

I used the [standard Open Energy Monitor current
transformer](http://openenergymonitor.org/emon/buildingblocks/report-yhdc-sct-013-000-current-transformer)
with a 22 ohm burden resistor (which gives about a 0.89V peak-to-peak
output when presented with a 30 amps RMS primary current: 0.89V
peak-to-peak is, [according to
WikiPedia](http://en.wikipedia.org/wiki/Line_level#Nominal_levels), the
standard for line inputs and 30amps RMS is, I believe, the most my house
every pulls)

For the voltage reading, I'm using the standard Open Energy Monitor
AC-to-AC converter. This feeds into an 80mA fuse, then into a simple
resistor divider (10k and 220ohms). This gives about 0.7v across the
220ohm resistor which is fed into the sound card's line input. I use two
1N5282 diodes (1.3v forward voltage bias) in parallel across in the
220ohm resistor to guarantee that the peak to peak voltage never goes
above 1.3v.

[More details on the OEM
forum](http://openenergymonitor.org/emon/node/1680?page=1#comment-9023).
<!--break-->

