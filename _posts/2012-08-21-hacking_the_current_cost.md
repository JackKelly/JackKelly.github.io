---
title: "Hacking the Current Cost"
date: 2012-08-21 08:30:47 +0000
categories: ["PhD", "CurrentCost"]
permalink: /hacking_the_current_cost
---
I have almost 30 Current Cost Individual Appliance Monitors (I need to
monitor the power consumption of every appliance in my home for my PhD
project).  Unfortunately, I sometimes see drop-outs on a single channel
lasting thousands of seconds, which is simply unacceptable.  I see these
epic drop-outs even if the IAM is within a meter of its EnviR.  So data
is being lost somewhere between the IAM transmitting its packet and it
being sent via XML from the EnviR.  I think the IAMs simply squirt a
reading onto the RF carrier every 6 seconds without waiting for a "ping"
from the EnviR.  There are two possible places where the packets are
being lost:  1) the EnviR drops packets or 2) RF collisions

<div>

 

</div>

<div>

**1) EnviR drops packets**

</div>

<div>

If the EnviR is busy processing a packet of RF data when a new packet of
RF data arrives then maybe it will fail to receive the new packet.  So
if two IAMs send packets in quick succession then the second to send
will be ignored.   The RFM01 only has a 16 bit buffer so it could easily
overflow.  I have experiemented with setting two EnviRs to receive data
from a single IAM.  Sometimes both EnviRs receive a packet; sometimes
only one will receive a packet and sometimes both will drop the packet.
 I take this as evidence that sometimes an EnviR will drop a packet
because it's too busy.

</div>

<div>

 

</div>

<div>

**2) RF collisions**

</div>

<div>

An alternative explanation for the long drop outs is that some of the
failed IAM transmissions are caused by RF collisions. How likely are RF
collisions?  Apparently the Current Cost devices use a 4kbps data rate.
 So a single bit take 1/4000 of a second to transmit so a single byte
takes 8/4000 seconds = 2ms.  The RF packets on the CC transmitter are
[16 bytes long](http://gangliontwitch.com/ccPower.html). So a single
packet takes 16 x 2ms = 32ms.  So about 30 packets can fit into a second
and 180 can fit into the 6 second gap between IAM transmissions.  Let's
make the maths simple and assume that we have 180 discrete time slots
per 6 second cycle.  The chance of a single IAM transmitting in any
given time slot is 1/180.  If we had only two IAMs then the chance of
them sharing a single time slot (and hence colliding) is 1/180 x 1/180 =
1/32400.  But we have 30 IAMs hence we have a total of 30-choose-2 pairs
= 435 pairs, so the chance of any pair colliding is 435/32400 = 1.3%;
which is rather too high for comfort given that I want this logging to
run for months and months.  And of course there are several reasons to
believe the chance of a collision is even higher: we don't have discrete
time slots and collisions can happen between any set of transmitters,
not just pairs.  Ick.

</div>

<div>

 

</div>

<div>

**My plan**

</div>

First I'm going to assume that the main problem is that the EnviR drops
packets because it's too busy.  Hence I want to connect an
RF receiver directly to my laptop in order to sniff IAM data directly
from the air without having to use an EnviR.  I'm somewhat out of my
depth here!  After  a bit of googling, I came across [this Nanode IRC
conversation](http://nanode.random-chaos.org.uk/nanode/2011-11-14) about
sniffing the SPI bus of a Current Cost to reverse engineer their
protocol.  I assume I just need a [Bus
Pirate](http://proto-pic.co.uk/bus-pirate/) to sniff the SPI bus of the
EnviR to get the initialisation commands the EnviR sends to its on-board
RFM01 RF module; and then I can buy an RFM01 module and connect this to
the bus pirate's SPI bus to communicate directly with the RFM01 from my
laptop.

If I find that RF collisions are a major problem then I may investigate
the [EDF wireless transmitter
plugs](http://www.edfenergy.com/products-services/for-your-home/ecomanager/ecomanager-upgrades.shtml#).
 These are similar to the Current Cost IAMs except, crucially, the EDF
models use *transceivers* and not just transmitters.  The EDF Eco
Manager base station "pings" each transmitter plug in sequence and the
transmitter plug responds within [about
20ms](http://forum.jeelabs.net/comment/5279#comment-5279).  This should
totally avoid RF collisions.  The problem is that I already have 30
Current Cost IAMs!  I'm planning to take one apart to see if there's any
possibility of converting it to a trasceiver type (the IAMs say
"transmitter only" on the back).  If not then I guess I'll have to try
to return or eBay my IAMs and buy EDF transmitter plugs.  I'll still
have to build my own transciever because each Eco Manager can only
handle 14 transmitter plugs.  If I use multiple Eco Managers then RF
collisions will become possible again.

Below are some notes on tools and forums...

### SPI to USB converters

-   [USB to I2C & SPI converter and
    analyser](http://www.ebay.co.uk/itm/USB-I2C-SPI-Converter-and-Analyser-/310260909457)-
    £24.90 - eBay - UK seller
-   [Devantec USB to I2C, SPI and
    Serial](http://www.robotshop.com/eu/devantec-usb-i2c-spi-serial-interface.html)
    - €24.59 - RobotShop.com
-   [Microchip ADM00419 Break Board MCP2210 mini
    USB-SPI](http://uk.farnell.com/jsp/displayProduct.jsp?sku=2078571)-
    £9.79 - Farnell
-   [RFM12B USB light
    Stick](http://busware.de/tiki-index.php?page=RFM12BUSB) (using an
    ATmega32u4) - €39 -  Busware.de
-   [JeeNode](http://jeelabs.com/products/jeenode) (RFM12b
    with ATmega328p) - €18.50 - JeeLabs.com
-   [Bus Pirate](http://proto-pic.co.uk/bus-pirate/) - £20 -
    ProtoPic (purchased)
    -   [Review on
        SkyWired](http://skywired.net/blog/2011/11/bus-pirate-review/)
    -   [bus pirate basic probe
        set](http://proto-pic.co.uk/bus-pirate-basic-probe-set/)
    -   [bus pirate cable](http://proto-pic.co.uk/bus-pirate-cable/)

### Logic Analysers

-   [Saleae 8 Channel 24 MHz](http://www.saleae.com/logic/) - [£132 from
    Proto-Pic](http://proto-pic.co.uk/usb-logic-analyser/)
-   ["Saleae Logic Compatible" clone for
    £30](http://robosavvy.com/store/product_info.php/products_id/3153/currency/GBP) -
    [blog post about Saleae
    kockoffs](http://hackaday.com/2011/12/15/saleae-logic-analyzer-knockoff-hacking/)

### RF modules

-   [Beeny found
    that ](http://nanode.random-chaos.org.uk/nanode/2011-11-14#i_2377538)the
    Current Cost EnviR uses an RFM01 receiver and Current Cost
    transmitters use RFM02 transmitters operating at 433MHz.  The EDF
    EcoManager and EDF IAMs (both of which appear to be made by
    Current Cost) probably use RFM12b transceivers.
-   [RFM12b specs](http://www.hoperf.com/rf_fsk/fsk/RFM12B.htm)
-   [RFM12B 433MHz is £6.32 from
    Farnell](http://uk.farnell.com/quasar/rfm12b-433-d/module-transceiver-5db-433mhz/dp/1878282)
-   [RFM12
    tutorial](http://blog.strobotics.com.au/tutorials/rfm12-stuff/)

### Forum threads and blog posts

-   [Eco Manager Teardown and help identify
    RF](http://forum.jeelabs.net/node/661) - Jan 2012 -
    forum.jeelabs.net
    -   [EDF Eco Manager is made by Current
        Cost](http://forum.jeelabs.net/comment/4236#comment-4236)
    -   [It uses a
        433MHz RFM12b](http://forum.jeelabs.net/comment/5264#comment-5264)
    -   Some results from sniffing the SPI bus
        ([here](http://forum.jeelabs.net/comment/5279#comment-5279) and
        [here](http://forum.jeelabs.net/comment/6832#comment-6832))
-   [KenB talking briefly about sniffing the Current Cost's SPI bus
    using a Bus
    Pirate](http://community.cosm.com/node/714#comment-1928) - July 2011
-   [Nanode IRC log for Nov 2011 where Beeny talks about sniffing the
    CC's SPI
    bus](http://nanode.random-chaos.org.uk/nanode/2011-11-12#i_2377160)
-   [DIY radio receiver for CurrentCost sensors on
    GanglionTwitch](http://gangliontwitch.com/ccPower.html).

### Current Cost specs

-   RF buad rate = [3.918 Kbps
    (found by Beeny)](http://nanode.random-chaos.org.uk/nanode/2011-11-12#i_2377180)
-   [Uses RFM01 RX / RFM02 TX pair (found
    by Beeny)](http://nanode.random-chaos.org.uk/nanode/2011-11-14#i_2377538)
-   Transmitter "[sends 16 bytes of manchersterized data over the air,
    which results in eight bytes of
    data](http://gangliontwitch.com/ccPower.html)"
-   [RFM01 init parameters (in the
    InitRFM01 function)](http://gangliontwitch.com/ccPower.html)

<!--break-->

