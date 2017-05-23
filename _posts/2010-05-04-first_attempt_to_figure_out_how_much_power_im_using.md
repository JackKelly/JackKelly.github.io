---
title: "First attempt to figure out how much power I\'m using"
date: 2010-05-04 09:50:19 +0000
categories: ["green diary", "electrical efficiency", "smart meters"]
permalink: /first_attempt_to_figure_out_how_much_power_im_using
---
I've had my AlertMe smart meter for a few days now. Here's a quick
attempt to annotate my power consumption

![Jack's annotated electricity
consumption](http://farm5.static.flickr.com/4010/4577838776_ce0794669b_o.png)

Consumption of individual appliances
------------------------------------

An ongoing task is for me to go round the house and measure each
device's energy consumption using a plug-in meter.  I try to measure the
total energy consumed over a week and then calculate the following
figures.  All the figures below are either direct measurements using a
plug-in power meter or are calculated from those measurements.  The"av
kWh per 24 hours" figure is either measured by leaving the plug-in meter
clocking up the consumption of the device over several days or, for
devices which draw power all the time, by multiplying the wattage by 24
hours.

<iframe frameborder="0" height="800" src="http://spreadsheets.google.com/pub?key=t-Ts6Xta0A9-tr27_xZjqgg&amp;single=true&amp;gid=8&amp;output=html&amp;widget=true" width="720"></iframe>

I'm somewhat surprised at how hungry the Fridge and Home Theatre PC are.
 154kg of CO<sub>2</sub> per year is roughly equivalent to a single flight from
London to Berlin for 1 person.

We don't buy meet at home (except for dog food) so it has occurred to me
in the past that we could actually get by with a much smaller fridge
freezer, especially if we're successful in growing a lot of our own food
and veg.  But the fridge is only a few years old so we're not going to
get rid of it any time soon.   Maybe I should dig out the manual and see
if there are any settings which are more energy efficient.

How accurate is the clamp meter?
--------------------------------

The smart meter clamps onto a single conductor at the main electricity
meter:

![smart meter
clamp](http://farm5.static.flickr.com/4030/4569076420_8bdf3da8e0.jpg)

You'll remember from physics class that electrical currents flowing
through a conductor induce a magnetic field.  The alternating current
running through the red cable feeding power into the house induces an
alternating magnetic field which, in turn, induces an alternating
current in the coil of wire in the smart meter's clamp.  The voltage
across this coil is then measured, digitised, sent wirelessly to the
AlertMe base station and then sent over my ADSL modem to AlertMe's
website.

As to whether or not the smart meter is reading accurately... I can't
figure out a really clean, simple way to check this (not least because
our house meter's rotating disk doesn't give a high resolution
instantaneous measurement of power, which is what the smart meter
produces).  My best attempt so far has been to compare Google's "total
power used on 3rd May" to my meter readings.  Except I didn't take meter
readings at 03/05/2010 00:00:00 and 04/05/2010 00:00:00 so I've had to
interpolate between my actual meter readings back to midnight (which
isn't going to be very accurate because our power usage is distinctly
lumpy).  Google reports that we used 4.7 kWh on 3rd May.  My
interpolated meter readings suggest we used 4.84 kWh for the 3rd May.
 So they're within range.  I suppose I should try to take some meter
readings at midnight.

As far as I'm aware, the "inductive clamp" sensor should be pretty
accurate with high [power
factor](http://en.wikipedia.org/wiki/Power_factor) loads (like tungsten
lamps) but less accurate with low power factor loads (fluorescent lamps,
switched mode power supplies including PC power supplies etc).  But, to
make matters worse, [the electromechanical meter also gets confused with
certain types of
loads](http://www.dslreports.com/forum/r19884549-Using-a-clampon-ampmeter#19896884).
 So, in other words, it's relatively easy to measure the power consumed
by a single tungsten lamp, but it's non-trivial measuring power consumed
by devices like PC power supplies or fluorescent lamps. But this "power
factor" stuff is a bit beyond my understanding of the physics; I need to
read up more about it.

[Read more about the Peckham Power Meter project (where we'll provide
you with an AlertMe meter) here](/power-meter-project)

