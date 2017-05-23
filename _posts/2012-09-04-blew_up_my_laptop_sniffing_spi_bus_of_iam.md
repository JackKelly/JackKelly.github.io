---
title: "Blew up my laptop sniffing SPI bus of IAM!"
date: 2012-09-04 16:33:15 +0000
categories: ["PhD", "CurrentCost"]
permalink: /blew_up_my_laptop_sniffing_spi_bus_of_iam
---
<span class="flickr-wrap" style="width:640px;"><span
class="flickr-image">[![](https://farm9.staticflickr.com/8295/7930652528_0cf14306e5_z.jpg)](https://www.flickr.com/photos/37816297@N06/7930652528)</span></span>

I did something dumb. And expensive. And potentially dangerous. I blew
up my laptop! How did I achieve this amazing feat? By connecting a
Current Cost Individual Appliance Monitor to my laptop via a Bus Pirate
(note the burnt patch of PCB on the top right of the photo!). I took
care to make sure I was connecting the correct SDI lines, just as I had
successfully done when [sniffing data from my
EnviR](/sniffing_spi_data_from_my_current_cost_envir).

So why did I blow my laptop by connecting to an IAM?

<!--break-->

The IAM's circuit board doesn't connect to the mains earth connection
but I'm pretty sure that my laptop connects ground to mains earth. So I
think the the IAM's ground connection is allowed to float many, many
volts above earth. The end result was a big bang, a dead laptop
(currently awaiting a new motherboard costing several hundred pounds), a
dead Bus Pirate and the event caused the mains ring's
[RCD](http://en.wikipedia.org/wiki/Residual-current_device) to trip;
again suggesting that current was allowed to flow to earth.

Note that the mains earth is not connected to the IAM's circuit board.
DON'T DO WHAT I DID AND TRY TO HACK THE IAM UNLESS YOU REALLY, REALLY
KNOW WHAT YOU'RE DOING! Risk of electricution!

<span class="flickr-wrap" style="width:480px;"><span
class="flickr-image">[![](https://farm9.staticflickr.com/8440/7836248670_581c52fa1e_z.jpg)](https://www.flickr.com/photos/37816297@N06/7836248670)</span></span>
<span class="flickr-wrap" style="width:480px;"><span
class="flickr-image">[![](https://farm9.staticflickr.com/8295/7930848154_0677cbece9_z.jpg)](https://www.flickr.com/photos/37816297@N06/7930848154)</span></span>
<span class="flickr-wrap" style="width:640px;"><span
class="flickr-image">[![](https://farm9.staticflickr.com/8181/7930854292_cfc22e568c_z.jpg)](https://www.flickr.com/photos/37816297@N06/7930854292)</span></span>

How to avoid this nasty event happening again? I bought an optocoupler
which should allow me to isolate the target device being sniffed and the
Bus Pirate. I bought the Avago HCPL-090J-000E optocoupler ([£8.79 from
Farnell](http://uk.farnell.com/jsp/search/productdetail.jsp?SKU=1611323))
which is nice and fast. And [an SMD
adapter](http://uk.farnell.com/jsp/search/productdetail.jsp?SKU=1426172).
Some (most?) optocouplers would struggle to keep up with an SPI clock of
several MHz.

The optocoupler soldered onto its SMD adapter:

<span class="flickr-wrap" style="width:480px;"><span
class="flickr-image">[![](https://farm9.staticflickr.com/8457/7930657652_84fcb14312_z.jpg)](https://www.flickr.com/photos/37816297@N06/7930657652)</span></span>

Whilst awaiting my new laptop, I've resurrected an old Athlon X2
machine; installed Ubuntu 12.04 on it and, after replacing the heatsink
that had fallen off the CPU, and upgrading the graphics card to one that
can handle Unity's effects, I now have a working development system
again. (Yes, all my work was backed up from my laptop.) It's rather
frustrating because I'm already a bit behind schedule. Never mind. It
could've been worse. I could've electrocuted myself :/

The back of my blown bus pirate:

<span class="flickr-wrap" style="width:640px;"><span
class="flickr-image">[![](https://farm9.staticflickr.com/8030/7930644170_067ea2245b_z.jpg)](https://www.flickr.com/photos/37816297@N06/7930644170)</span></span>

My lethal hacked IAM. DO NOT TRY THIS AT HOME!

<span class="flickr-wrap" style="width:640px;"><span
class="flickr-image">[![](https://farm9.staticflickr.com/8435/7930621918_4bb64cb539_z.jpg)](https://www.flickr.com/photos/37816297@N06/7930621918)</span></span>

