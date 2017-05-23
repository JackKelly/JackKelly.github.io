---
title: "Making a \"haunted staircase\" for Halloween using a Touch Board & Ableton Live"
date: 2016-11-18 15:52:19 +0000
categories: ["making", "kids", "audio"]
permalink: /making_a_haunted_staircase_for_halloween_using_a_touch_board
---
<span class="flickr-wrap"><span
class="flickr-image">[![P1040124](https://farm6.staticflickr.com/5520/31053583316_6d656e88d2_c.jpg "P1040124")](https://www.flickr.com/photos/37816297@N06/31053583316)</span></span>

For Halloween 2016, we made a "haunted staircase". Spooky sounds were
triggered as unsuspecting trick-or-treaters walked up the stairs outside
our house. This project [won the Bare Conductive Halloween
competition](https://twitter.com/BareConductive/status/806513603922706433)!
This blog post describes how we made our staircase...

(the photo above was taken by my wife, Ginnie)

Here's a video of the final result, as demonstrated by my five year-old
daughter, Olive:

<iframe width="740" height="416" src="https://www.youtube.com/embed/blNHySE9uIg?rel=0" frameborder="0" allowfullscreen>
</iframe>
<!--break-->

(sorry the video is a bit dark!)

To trigger the sounds, I used a Bare Conductive [Touch
Board](https://www.bareconductive.com/shop/touch-board) connected via
USB to a laptop running [Ableton
Live](https://www.ableton.com/en/live/). The Touch Board uses capacitive
sensing to detect either a direct contact of a hand or, if the
sensitivity is increased, then it can detect a nearby hand or foot.
Here's a video I made while I was testing the Touch Board. Here it's
being triggered by me touching the board's contacts:

<iframe width="740" height="416" src="https://www.youtube.com/embed/aTC5dsOVxh0?rel=0" frameborder="0" allowfullscreen>
</iframe>
To detect a person's foot on each step for the haunted staircase, I
gaffa taped a wire to each step like this:

<span class="flickr-wrap"><span
class="flickr-image">[![IMG\_20161118\_144038007](https://farm6.staticflickr.com/5326/31089026945_d9149c14ee_c.jpg "IMG_20161118_144038007")](https://www.flickr.com/photos/37816297@N06/31089026945)</span></span>

<span class="flickr-wrap"><span
class="flickr-image">[![IMG\_20161118\_144125575](https://farm6.staticflickr.com/5825/31089022285_803bdb5e48_c.jpg "IMG_20161118_144125575")](https://www.flickr.com/photos/37816297@N06/31089022285)</span></span>

<span class="flickr-wrap"><span
class="flickr-image">[![IMG\_20161118\_144130781](https://farm6.staticflickr.com/5675/31053266896_27f065586e_c.jpg "IMG_20161118_144130781")](https://www.flickr.com/photos/37816297@N06/31053266896)</span></span>

I originally tried gaffa-taping the wires directly to the concrete steps
but this didn't work very well, so I experimented with separating each
wire from the concrete step. I settled on using a strip of bubble-wrap
under each wire, and this seemed to work well.

The Touch Board is programmed using the Arduino IDE. I followed Bare
Conductive's [excellent tutorial on configuring the Touch Board to
trigger
Live](https://www.bareconductive.com/make/touch-board-ableton-live/). I
modified the code to configure the Touch Board to send MIDI notes
instead of proximity mapped MIDI controls (do this by commenting out the
code under the "Proximity (CC) electrodes" section and uncomment the
code under the "Touch (note) electrodes" section); and also set the
`touchThreshold` and `releaseThreshold` really low. The exact numbers
needed quite a bit of tweaking to get it to reliably detect a child's
foot on each step! [My code is on
github](https://github.com/JackKelly/haunted_staircase).

The Touch Board sends MIDI commands to Ableton Live over a USB
connection. Each audio sample lives in separate file. I used the "Zone"
panel in Ableton Live's Sampler's to configure each sample to be
triggered by a single MIDI note. Sampler provides lots of controls for
messing with the audio and adding spooky reverb etc.

Some of the samples were recorded by my two year old son and five year
old daughter. Other samples were downloaded. I wanted to record some
audio of our dog barking and slow this right down but I wasn't patient
enough to catch a good dog bark on my audio recorder!

To make the stairs look spooky, we hung a blackout-drape over the
stairs. This was supported by four straight lengths of wood which were
wire-strapped to the railings. We made some simple ghosts out of
cardboard and old sheets. To light the staircase, we used cheap
battery-powered LED lights with some coloured lighting gel.

It was lots of fun to build and kids enjoyed it!

Next time we might play with proximity sensing. Or use Ableton Live to
drive motorised ghosts! Or control lights (Ableton Live sends MIDI
commands and it should be fairly easy to use an Arduino (or the Touch
Board) to receive these MIDI commands and drive motors and/or lights).
And we definitely need to get some dry ice! And maybe trigger lights at
a distance: e.g. trigger strobes in the upstairs bedroom. Or fill our
car with dry-ice and then start a slow, pulsing red light in the car as
people get near; and maybe have a motorised "hand" thump against the
inside of the car window!

Here are some more photos:

<span class="flickr-wrap"><span
class="flickr-image">[![IMG\_20161029\_152944609\_HDR](https://farm6.staticflickr.com/5467/30946629632_65a94afdf0_c.jpg "IMG_20161029_152944609_HDR")](https://www.flickr.com/photos/37816297@N06/30946629632)</span></span>

<span class="flickr-wrap"><span
class="flickr-image">[![P1040116](https://farm6.staticflickr.com/5340/31053621896_527f9131ab_c.jpg "P1040116")](https://www.flickr.com/photos/37816297@N06/31053621896)</span></span>

<span class="flickr-wrap"><span
class="flickr-image">[![P1040114](https://farm6.staticflickr.com/5569/30946975432_297117dc0c_c.jpg "P1040114")](https://www.flickr.com/photos/37816297@N06/30946975432)</span></span>

<span class="flickr-wrap"><span
class="flickr-image">[![P1040118](https://farm6.staticflickr.com/5729/30946961612_c20c78ae9b_c.jpg "P1040118")](https://www.flickr.com/photos/37816297@N06/30946961612)</span></span>

<span class="flickr-wrap" style="width:450px;"><span
class="flickr-image">[![P1040120](https://farm6.staticflickr.com/5652/31053602956_001334b7a6_c.jpg "P1040120")](https://www.flickr.com/photos/37816297@N06/31053602956)</span></span>

