---
title: "Success pinging EDF IAM and receiving response."
date: 2012-09-06 16:25:20 +0000
categories: ["PhD", "CurrentCost", "EcoManager"]
permalink: /success_pinging_edf_iam_and_receiving_response
---

*Table of contents*

* TOC
{:toc}

<span class="flickr-wrap" style="width:640px;"><span
class="flickr-image">[![EDF IAM with
Nanaode](https://farm9.staticflickr.com/8295/7944346618_21c5ff399c_z.jpg "EDF IAM with Nanaode")](https://www.flickr.com/photos/37816297@N06/7944346618)</span></span>

Yesterday my first [EDF Individual Appliance
Monitor](https://shop.edfenergy.com/Item.aspx?id=540&CategoryID=1)
arrived. These are very, very similar to Current Cost IAMs except for
several vital differences:

1.  Each EDF IAM can both send and receive (the CC IAMs can only send).
2.  Each EDF IAM will only report its wattage when polled by the EDF
    EcoManager base station. This is *great* for my application because
    I should be able to completely avoid RF collisions.
3.  Each EDF IAM also has a relay to turn the appliance on or off. This
    relay can be activated using the manual override switch on the EDF
    IAM or over RF
4.  The packets appear to include a simple checksum! (The CC
    Transmitters don't bother with a checksum.)

I've made good progress today. I think I can now reliably talk to my EDF
IAM and get replies.

<!--break-->

Interestingly, the EDF kit appears to use almost exactly the same RF
configuration as the CC kit; but with a slightly different packet
structure. The EDF IAMs use a base frequency of 433.97MHz (compared with
433.90MHz for the CC kit) and a bitrate of 3.918 kbps. The RFM01 I set
up to receive CC packets can recieve the EDF IAM packets easily. As far
as I can tell, the EDF IAM packets are not "manchesterised" like the CC
IAM packets; and the EDF RF packets are only 12 bytes long compared with
16 bytes of manchesterised data for the CC packets.

## Sniffing RF packets from the EDF IAM

The EDF IAM probably emits only a 12 byte packet. But I captured and
displayed 16 bytes just in case the packet is longer than 12 bytes. The
packets below were received using an
[RFM01](http://www.hoperf.com/rf_fsk/fsk/18.htm) and my [RFM01 Current
Cost code](https://github.com/JackKelly/rfm_current_cost) (using exactly
the same settings as for the Current Cost IAMs) running on a
[Nanode](http://www.nanode.eu/).

### EDF IAM transmissions when manual override is turned on and off.

#### No appliance plugged into the EDF IAM.



```
BYTE
00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15

first time on:
52 55 10  0  3  0 41 4B  7  0 53 A0 62  2  0  0 
52 55 10  0  3  0 41 4B  7  0 53 A0 60  0  1 80 

first time off:
52 55 10  0  3  0 41 4B  0  0 4F 95 40  0  0  0 
52 55 10  0  3  0 41 4B  0  0 4F 95 40 80  0  0 

second time on:
52 55 10  0  3  0 41 4B  0  0 53 99 40  0  0  0 
52 55 10  0  3  0 41 4B  0  0 53 99 60  0  0 19 

second time off:
52 55 10  0  3  0 41 4B  0  0 4F 95 60  0  0  0 
52 55 10  0  3  0 41 4B  0  0 4F 95 40  2  0  5 

third time on:
52 55 10  0  3  0 41 4B  0  0 53 99 40  0  0  0 
52 55 10  0  3  0 41 4B  0  0 53 99 40  0  0  0 

third time off:
52 55 10  0  3  0 41 4B  0  0 4F 95 40 40  0  0 
52 55 10  0  3  0 41 4B  0  0 4F 95 40  0  0  0 

fourth time on:
52 55 10  0  3  0 41 4B  0  0 53 99 40  8  0  0 
52 55 10  0  3  0 41 4B  0  0 53 99 70  0  0  0 

fourth time off:
52 55 10  0  3  0 41 4B  0  0 4F 95 60  1  B  4 
52 55 10  0  3  0 41 4B  0  0 4F 95 60  0  0  0
```



The EDF IAM appears to transmit two packets which are nearly identical
for each manual switching event. Perhaps this is a simple way to
increase resilience to dropped packets? I won't bother repeating the
packets from now on...

#### Different loads plugged into the IAM



```
Plugged into a dimmable 75W lamp
Gradually increasing.
showing only the first transmission after "on":
52 55 10  0  3  0 41 4B 11  0 53 AA 40  0  0  0 
52 55 10  0  3  0 41 4B 1C  0 53 B5 40  0  0  0 
52 55 10  0  3  0 41 4B 26  0 53 BF 40  0  0  0 
52 55 10  0  3  0 41 4B 2C  0 53 C5 40  0  0  0  
52 55 10  0  3  0 41 4B 35  0 53 CE 40  0  0  0
52 55 10  0  3  0 41 4B 3D  0 53 D6 40  0  0  0 

Kettle:
52 55 10  0  3  0 41 4B  4  0 53 9D 
52 55 10  0  3  0 41 4B 42  9 53 E4 
52 55 10  0  3  0 41 4B FF  8 53 A0 
52 55 10  0  3  0 41 4B DD  8 53 7E 
```



So, based on this very limited set of observations:

-   Bytes 0 to 7 never change. Supposedly some of these bytes must be
    the ID. I only have a single EDF IAM so I can't yet figure out which
    bytes are the ID. I plan to order some more EDF IAMs and an
    EcoManager tomorrow (I buy this EDF kit directly from EDF).
-   Bytes 8 and 9 appear to be involved in communicating the measured
    watts value. I think byte 9 is the most significant byte whilst byte
    8 is the least significant byte.
-   Byte 10 is always 0x53 when the EDF IAM turns on and 0x4F when it
    turns off.
-   Byte 11 appears to be an 8-bit checksum using the [modular sum
    algorithm](http://en.wikipedia.org/wiki/Checksum#Modular_sum)
    against bytes 0 to 10.
-   Byte 12 is always either 0x40, 0x42, 0x44, 0x60, 0x62 or 0x70. These
    all start with 01 in binary which leads me to think that the tail of
    the EDF packet is 01 (binary)
-   Bytes 13-15 appear to be just noise, strongly supporting the
    hypothesis that the EDF IAM packet is only 12 bytes long.

## Pinging the EDF IAM

I don't (yet) have an EDF EcoManager base station. But [cii
reported](http://forum.jeelabs.net/comment/6832#comment-6832) a
"conversation" between his EDF EcoManager and a single IAM. His
conversation went like this:



```
00 01 02 03 04 05 06 07 08 09 10 11

ping from EcoManager:
46 55 10 00 01 00 50 53 00 00 4F 9E

and a reply from plug 1
52 55 10 00 01 00 41 4B 00 00 4F 93
```



My IAM produces packets like this:

`52 55 10 0 3 0 41 4B 0 0 4F 95`

So I came up with an 11-byte packet using the patterns in cii's data and
added a checksum to come up with:



```
Ping from my RFM12b:
46 55 10  0  3  0 50 53  0  0 4F A0

Reply from EDF IAM:
52 55 10  0  3  0 41 4B  0  0 53 99
```



## The tuning button



```
00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15

After pressing the "tune" button:
52 82 3B 36 66  0 43 4F  0  0 53 90 40  0  0  0 
52 82 3B 36 66  0 43 4F  0  0 53 90 60  0  0  0 

on:
52 55 10  0  3  0 41 4B  0  0 53 99 60  0  0  0 
52 55 10  0  3  0 41 4B  0  0 53 99 40  0  0  0 

off:
52 55 10  0  3  0 41 4B  0  0 4F 95 40  0  0  0 
52 55 10  0  3  0 41 4B  0  0 4F 95 40  0  0  0

on:
52 55 10  0  3  0 41 4B  0  0 53 99 40  0  0  0 
52 55 10  0  3  0 41 4B  0  0 53 99 60  0  0  0 

off:
52 55 10  0  3  0 41 4B  0  0 4F 95 40  0  0  0 
52 55 10  0  3  0 41 4B  0  0 4F 95 42  s0  0  0 

After pressing the "tune" button again:
52 7E 32 3B 7E  0 43 4F  0  0 53 A0 40  0  0  0 
52 7E 32 3B 7E  0 43 4F  0  0 53 A0 40  0  0  0 

on:
52 55 10  0  3  0 41 4B  0  0 53 99 40  0  0  0 
52 55 10  0  3  0 41 4B  0  0 53 99 40  0  0  0 

off:
52 55 10  0  3  0 41 4B  0  0 4F 95 40  0  0  0 
52 55 10  0  3  0 41 4B  0  0 4F 95 40  0  0  0 

After pressing the "tune" button again:
52 1D 1D 1F 5D  0 43 4F  0  0 4F E9 40  0  0  0
52 1D 1D 1F 5D  0 43 4F  0  0 4F E9 40  0  0  0 
```



The tuning button is just odd. To recap, I pressed the tuning button
three times and the three responses from the EDF IAM were:



```
52 82 3B 36 66  0 43 4F  0  0 53 90 40  0  0  0 
52 7E 32 3B 7E  0 43 4F  0  0 53 A0 40  0  0  0 
52 1D 1D 1F 5D  0 43 4F  0  0 4F E9 40  0  0  0
```



-   Byte 0 is always 0x52
-   Bytes 5, 8 and 9 are always 0

It's also interesting that the EDF IAM doesn't change its "on" or "off"
packet after being "tuned". This is in contrast to the CC IAMs which do
change their packets after being tuned. Perhaps the EDF IAMs require a
command from the EcoManager to tell the EDF IAMs which ID to adopt (this
would be sensible as only the EcoManager base knows which IDs are
current in use and which are available).

## Implementation

I've started work on an DIY EDF EcoManager. [My AVR C++ code is on
github](https://github.com/JackKelly/rfm_edf_ecomanager). I'm using an
RFM12b 433MHz and a Nanode. At the time of writing, the code can ping my
single EDF IAM, checks the incomming packet's checksum and extracts the
wattage. All very simple and the code is rather ugly at the moment
because I'm still hacking around a lot.

## Sample rate

I had hoped that I'd be able to sample each appliance once every, say,
three seconds. It looks like it is possible to ping the EDF IAM as
rapidly as you want but it appears that the EDF IAM only bothers to take
a sample once every six seconds or so. In other words, it appears to not
sample the wattage when you ping the EDF IAM but instead it's
independently measuring the wattage and storing this value ready for
transmission when you poll for it.

## Who makes the EDF IAM?

<span class="flickr-wrap" style="width:480px;"><span
class="flickr-image">[![Back of EDF
IAM](https://farm9.staticflickr.com/8182/7944335674_e5a78344cd_z.jpg "Back of EDF IAM")](https://www.flickr.com/photos/37816297@N06/7944335674)</span></span>

Note that this EDF IAM has a model name "IAM" whilst the CC IAMs have
the model name "IAM Transmitter Only".

## Wiki page for technical details of the EDF EcoManager protocol

I've started [a wiki page for technical details of the EDF EcoManager
protocol](https://github.com/JackKelly/rfm_edf_ecomanager/wiki/Technical-details-of-the-EDF-EcoManager-and-accessories).
Please feel free to edit!

