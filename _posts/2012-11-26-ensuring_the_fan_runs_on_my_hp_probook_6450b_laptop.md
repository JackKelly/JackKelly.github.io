---
title: "Ensuring the fan runs on my HP ProBook 6450b laptop"
date: 2012-11-26 20:19:27 +0000
categories: ["laptop", "linux"]
permalink: /ensuring_the_fan_runs_on_my_hp_probook_6450b_laptop
---
<span class="flickr-wrap" style="width:640px;"><span
class="flickr-image">[![](https://farm9.staticflickr.com/8314/8070144664_96c2e46694_z.jpg)](https://www.flickr.com/photos/37816297@N06/8070144664)</span></span>

I have an HP ProBook 6450b laptop which runs Ubuntu 12.10 and Windows 7.
It had a tedious and potentially expensive problem: when running Linux,
the CPU fan would fail to turn on until the CPU temperature reached
105℃. This was dangerously hot. I wrote about the problem in [detail on
the Ubuntu Forum](http://ubuntuforums.org/showthread.php?t=2060681),
including links to my conversations on the `linux-acpi` kernel list.

After spending about a month trying to find a software fix for this
problem, I decided it was time to get the soldering iron out to fix the
problem. Here's what I did: <!--break-->

-   I followed [the official HP guide for removing the
    keyboard](http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?lang=en&cc=us&taskId=125&prodSeriesId=4173642&prodTypeId=321957&objectID=c02476190)
    (it's really easy).
-   There are three wires running from the motherboard to the CPU fan:
    <span class="flickr-wrap" style="width:640px;"><span
    class="flickr-image">[![](https://farm9.staticflickr.com/8179/8070147527_f8777e9710_z.jpg)](https://www.flickr.com/photos/37816297@N06/8070147527)</span></span>
-   I cut the blue wire and left it disconnected.
-   I cut the red wire and tinkered with different resistors spliced
    into the red wire. I searched for a fan speed which would be quiet
    but produce significant cooling: <span class="flickr-wrap"
    style="width:640px;"><span
    class="flickr-image">[![](https://farm9.staticflickr.com/8450/8070140860_ea68f61a17_z.jpg)](https://www.flickr.com/photos/37816297@N06/8070140860)</span></span>
-   I settled for two resistors in parallel: <span class="flickr-wrap"
    style="width:640px;"><span
    class="flickr-image">[![](https://farm9.staticflickr.com/8169/8070129724_106f272809_z.jpg)](https://www.flickr.com/photos/37816297@N06/8070129724)</span></span>
-   One resister was a 47Ω (yellow, purple, black) the other was a 470Ω
    (yellow, purple, brown) giving a final resistance of 42.7Ω.
-   The finished product (not very tidy but it works!). <span
    class="flickr-wrap" style="width:640px;"><span
    class="flickr-image">[![](https://farm9.staticflickr.com/8449/8070140379_49bf06e243_z.jpg)](https://www.flickr.com/photos/37816297@N06/8070140379)</span></span>

(disclaimer: I'm not even vaguely qualified to tinker with laptop
hardware. I'm just some dude from the internets. I hacked together a
solution which worked for me and I've done my best to report what I did
in the hopes that this solution might work for others. If you break your
laptop trying to follow these steps then I'm sorry but I can't be held
responsible.)

