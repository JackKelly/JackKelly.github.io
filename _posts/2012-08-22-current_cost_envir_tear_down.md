---
title: "Current Cost EnviR tear down"
date: 2012-08-22 10:07:12 +0000
categories: ["PhD", "CurrentCost"]
permalink: /current_cost_envir_tear_down
---
I may have to reverse engineer some parts of the Current Cost RF
protocol. The first step may be to sniff the [SPI
bus](http://en.wikipedia.org/wiki/Serial_Peripheral_Interface_Bus)
between the EnviR's PIC and the RF module. Hence I've taken the EnviR
apart. Here's what it looks like inside...

### Disassembly

It's very easy to pull apart. You just need to tease the back of the
plastic case away from the front using a thin but wide screw driver:

<span class="flickr-wrap" style="width:480px;"><span
class="flickr-image">[![](https://farm9.staticflickr.com/8302/7836275280_68e836a934_z.jpg)](https://www.flickr.com/photos/37816297@N06/7836275280)</span></span>
<!--break-->

To gain access to the main EnviR PCB it's not necessary to unscrew the
bottom of the case. But this is what the bottom looks like:

<span class="flickr-wrap" style="width:640px;"><span
class="flickr-image">[![](https://farm9.staticflickr.com/8299/7836280916_41b2ddb2a8_z.jpg)](https://www.flickr.com/photos/37816297@N06/7836280916)</span></span>

You can also remove the front plastic cover but it doesn't reveal
anything very interesting:

<span class="flickr-wrap" style="width:480px;"><span
class="flickr-image">[![](https://farm8.staticflickr.com/7250/7836277986_e3f175a737_z.jpg)](https://www.flickr.com/photos/37816297@N06/7836277986)</span></span>

### Inside

<span class="flickr-wrap" style="width:640px;"><span
class="flickr-image">[![](https://farm9.staticflickr.com/8445/7836259616_1ce4736683_z.jpg)](https://www.flickr.com/photos/37816297@N06/7836259616)</span></span>
<span class="flickr-wrap" style="width:480px;"><span
class="flickr-image">[![](https://farm9.staticflickr.com/8443/7836272486_c1d66a7411_z.jpg)](https://www.flickr.com/photos/37816297@N06/7836272486)</span></span>

Here's a close up of the PIC: a [Microchip
PIC18F86J90](http://www.microchip.com/wwwproducts/Devices.aspx?dDocName=en536111).
<span class="flickr-wrap" style="width:480px;"><span
class="flickr-image">[![](https://farm8.staticflickr.com/7272/7836268286_17e63371de_z.jpg)](https://www.flickr.com/photos/37816297@N06/7836268286)</span></span>

And here's the RF module... it's almost certainly an
[RFM01](http://www.hoperf.com/pro/rf/cob/rfm01.htm) running at 433MHz.
We can be confident that it's an RFM01 because [Beeny has sniffed the
SPI bus](http://nanode.random-chaos.org.uk/nanode/2011-11-14#i_2377538).

<span class="flickr-wrap" style="width:480px;"><span
class="flickr-image">[![](https://farm9.staticflickr.com/8439/7836263884_7a5908f2f8_z.jpg)](https://www.flickr.com/photos/37816297@N06/7836263884)</span></span>

Note that this device almost certainly is not a Zigbee device, despite
the fact that Current Cost are a member of the Zigbee alliance. How can
we be confident that this isn't a Zigbee device? For the following
reasons:

-   Zigbee nodes must be able to both send and receive. The EnviR can
    only receive.
-   Zigbee operates at [868MHz in
    Europe](http://en.wikipedia.org/wiki/ZigBee#Zigbee_technology). The
    [CurrentCost EnviR operates at
    433MHz](http://www.flickr.com/photos/37816297@N06/7836225972/in/set-72157631187622996).
-   Zigbee data rates vary from 20 to 900kbps whilst the Current Cost
    runs at 4kbps.


