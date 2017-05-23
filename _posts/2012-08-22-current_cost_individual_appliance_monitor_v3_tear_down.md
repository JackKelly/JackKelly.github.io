---
title: "Current Cost Individual Appliance Monitor v3 tear down"
date: 2012-08-22 07:21:40 +0000
categories: ["CurrentCost", "PhD"]
permalink: /current_cost_individual_appliance_monitor_v3_tear_down
---
**UPDATE: DO NOT TAKE APART A CURRENT COST IAM UNLESS YOU REALLY KNOW
WHAT YOU'RE DOING. IT APPEARS THAT THE CIRCUIT BOARD IS NOT ISOLATED
FROM THE MAINS. HENCE SECTIONS OF THE PCB WHICH YOU MIGHT ASSUME ARE AT
ONLY A FEW VOLTS MAY IN FACT BE HUNDREDS OF VOLTS ABOVE EARTH. I.E.
ELECTROCUTION RISK! HOW DO I KNOW? BECAUSE [I BLEW UP MY
LAPTOP](http://jack-kelly.com/blew_up_my_laptop_sniffing_spi_bus_of_iam)
ATTEMPTING TO SNIFF SPI DATA FROM AN IAM!**

What does a [Current Cost Individual Appliance
Monitor](http://www.currentcost.com/product-iams.html) v3 look like
inside? Let's find out... (click on a photo to view it full-size on
Flickr)

<span class="flickr-wrap" style="width:480px;"><span
class="flickr-image">[![](https://farm8.staticflickr.com/7114/7836229020_a23bdba3e0_z.jpg)](https://www.flickr.com/photos/37816297@N06/7836229020)</span></span><!--break-->
<span class="flickr-wrap" style="width:480px;"><span
class="flickr-image">[![](https://farm9.staticflickr.com/8304/7836225972_b186066798_z.jpg)](https://www.flickr.com/photos/37816297@N06/7836225972)</span></span>
<span class="flickr-wrap" style="width:480px;"><span
class="flickr-image">[![](https://farm8.staticflickr.com/7252/7836239288_11e77ff848_z.jpg)](https://www.flickr.com/photos/37816297@N06/7836239288)</span></span>
<span class="flickr-wrap" style="width:480px;"><span
class="flickr-image">[![](https://farm9.staticflickr.com/8296/7836235676_f0f8ed2b98_z.jpg)](https://www.flickr.com/photos/37816297@N06/7836235676)</span></span>

Note that this IAM claims to be a "transmitter only". This is supposedly
to differentiate it from the [EDF Wireless Transmitter
Plug](http://www.edfenergy.com/products-services/for-your-home/ecomanager/ecomanager-wireless-transmitter-plug-FAQs.shtml)
which can send and receive data.

### Disassembly

You'll need a T6 torx screw driver to take the screws out. The best I
could find at my local DIY store was this T6 torx bit. This was fine for
the top 2 screws but couldn't reach the lower 2 screws.

<span class="flickr-wrap" style="width:480px;"><span
class="flickr-image">[![](https://farm9.staticflickr.com/8299/7836232352_e2e7484018_z.jpg)](https://www.flickr.com/photos/37816297@N06/7836232352)</span></span>

### Inside

<span class="flickr-wrap" style="width:480px;"><span
class="flickr-image">[![](https://farm9.staticflickr.com/8288/7836252608_cd98c78628_z.jpg)](https://www.flickr.com/photos/37816297@N06/7836252608)</span></span>

The red wire is the aerial.

<span class="flickr-wrap" style="width:640px;"><span
class="flickr-image">[![](https://farm8.staticflickr.com/7260/7836256256_7262cc9fe9_z.jpg)](https://www.flickr.com/photos/37816297@N06/7836256256)</span></span>

The RF transmitter module (top of the photo, to the right of the red
aerial wire) is very likely to be an
[RFM02](http://www.hoperf.com/pro/rf/cob/rfm02.htm) but I haven't
confirmed this by sniffing the [SPI
bus](http://en.wikipedia.org/wiki/Serial_Peripheral_Interface_Bus). The
RF transmitter IC has "ST8886 1123AR FOGO" written on it. I haven't
found what this chip is, even after lots of googling.

<span class="flickr-wrap" style="width:480px;"><span
class="flickr-image">[![](https://farm9.staticflickr.com/8288/7836252608_cd98c78628_z.jpg)](https://www.flickr.com/photos/37816297@N06/7836252608)</span></span>
<span class="flickr-wrap" style="width:480px;"><span
class="flickr-image">[![](https://farm9.staticflickr.com/8440/7836248670_581c52fa1e_z.jpg)](https://www.flickr.com/photos/37816297@N06/7836248670)</span></span>

In the photo above you can just about see that the neutral mains pin
passes straight through the IAM whilst the live connection goes through
the PCB and through a very chunky jumper. Supposedly the IAM measures
the voltage drop across the chunky jumper to measure current.

<span class="flickr-wrap" style="width:640px;"><span
class="flickr-image">[![](https://farm8.staticflickr.com/7108/7836244348_1095883b20_z.jpg)](https://www.flickr.com/photos/37816297@N06/7836244348)</span></span>

**UPDATE: TO REPEAT: DO NOT TAKE APART A CURRENT COST IAM UNLESS YOU
REALLY KNOW WHAT YOU'RE DOING. IT APPEARS THAT THE CIRCUIT BOARD IS NOT
ISOLATED FROM THE MAINS. HENCE SECTIONS OF THE PCB WHICH YOU MIGHT
ASSUME ARE AT ONLY A FEW VOLTS MAY IN FACT BE HUNDREDS OF VOLTS ABOVE
EARTH. I.E. ELECTROCUTION RISK! HOW DO I KNOW? BECAUSE [I BLEW UP MY
LAPTOP](http://jack-kelly.com/blew_up_my_laptop_sniffing_spi_bus_of_iam)
ATTEMPTING TO SNIFF SPI DATA FROM AN IAM!**

