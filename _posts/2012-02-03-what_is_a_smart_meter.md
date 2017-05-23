---
title: "What is a smart meter?"
date: 2012-02-03 16:34:05 +0000
categories: ["smart meters", "PhD", "introducing smart meter disaggregation"]
permalink: /what_is_a_smart_meter
---
This blog entry is part of [a series of posts introducing the topic of
smart meter disaggregation](/taxonomy/term/104).

Your existing electricity meter probably looks something like this:

[![Attribution: Kristoferb at
en.wikipedia](http://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Hydro_quebec_meter.JPG/320px-Hydro_quebec_meter.JPG "Electromechanical meter. Attribution: Kristoferb at en.wikipedia")](http://en.wikipedia.org/wiki/File:Hydro_quebec_meter.JPG)

<small>(image taken
by [Kristoferb](http://en.wikipedia.org/wiki/User:Kristoferb) at
[en.wikipedia](http://en.wikipedia.org/))</small>

By 2019, the UK government have mandated every electricity meter in
homes and businesses will be replaced by a "smart meter" (that's a grand
total of 53 million meters).  A smart meter is simply a digital meter
with some basic communications functions.  It will be paid for and
installed by the utility company.  It will talk to the utility company
over a GPRS data connection; and it will also be able to talk to the
"home area network" to provide data to in-house energy displays.

The [draft
spec](http://www.decc.gov.uk/publications/basket.aspx?filetype=4&filepath=11/tackling-climate-change/smart-meters/2393-smart-metering-industrys-draft-tech.pdf&minwidth=true#basket) for
smart meters in the UK was published by the [Smart Metering Design
Group](http://www.decc.gov.uk/en/content/cms/tackling/smart_meters/smdg/smdg.aspx) in
August 2011.  The specification states that the meter must be able to
supply meter readings to the home area network at a rate of one reading
every five seconds.  The meter will measure voltage, real power and
reactive power (in both directions).  Some utility companies have
already started to install smart meters; British Gas plan to have 2
million smart meters installed by the end of 2012 ([Centrica,
2010](http://www.centrica.com/index.asp?pageid=1041&newsid=1970)). 

If you can't wait for a smart meter to be installed then you could buy
and install a "home energy monitor". These are available for around £40;
although some utility companies give them away for free.  Home energy
monitors are user-installable.  I used a Current Cost home energy
monitor for [my MSc project on
disaggregation](http://jack-kelly.com/my_msc_project_on_disaggregation_is_on_the_imperial_website).
 It recorded a sample of apparent power once every six seconds.

This is a reading produced by my Current Cost home energy monitor:

<span class="flickr-wrap" style="width:640px;"><span
class="flickr-image">[![meterPlot](https://farm8.staticflickr.com/7033/6812534035_3466d39707_z.jpg "meterPlot")](https://www.flickr.com/photos/37816297@N06/6812534035)</span></span>

The value of sample at time *t* is the sum of the power being consumed
by every appliance active at time *t*​.

<!--break-->

