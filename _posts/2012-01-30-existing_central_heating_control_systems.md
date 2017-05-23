---
title: "Existing central heating control systems"
date: 2012-01-30 08:21:32 +0000
categories: ["heating", "green diary"]
permalink: /existing_central_heating_control_systems
---
A little while ago I wrote[some notes describing my "ideal" central
heating control system](/a_better_central_heating_control_system), which
I was planning to build myself.  Time is short so it looks like this
system won't be built for a while so I need something which I can buy
off-the-shelf which will satisfy as many of my requirements as possible
and also leave the door open to DIY tinkering in the future.  This blog
post is a collection of notes about off-the-shelf central heating
control systems.

### Requirements

1.  Programmable room thermostat in each room (which senses the
    temperature in the room, compares that to a temperature schedule for
    that room and turns on the TRV valves on the room's radiator if
    necessary).  This could be integrated into the TRV. 
2.  All communication should be wireless. (I have run a few cables
    around the house but not for every room).
3.  Room thermostats must be able to signal to the boiler to request
    more heat.  Having a single boiler schedule and thermostat to
    control the boiler is so utterly dumb it's frightening.
4.  The system needs to be able to work with our underfloor heating
5.  It would be awesome if the system could be controlled from a laptop
    / iPad / Android phone / iPhone, both within the house and outside
    the house

### Current Plan

I need to explore the [ELV
MAX!](http://translate.googleusercontent.com/translate_c?depth=1&ei=X973UJu5GI_64QSs8oGADA&hl=en&prev=/search%3Fq%3Delv%2Bmax!%26hl%3Den%26client%3Dubuntu%26hs%3DkCU%26tbo%3Dd%26channel%3Dfs%26gl%3Duk%26biw%3D1600%26bih%3D786&rurl=translate.google.co.uk&sl=de&twu=1&u=http://www.elv.de/max-funk-heizungsregler-system.html&usg=ALkJrhiZtJuNn9vasxEGKPufZSy-vJiXKA)
system.  Very good prices.  Has radiator TRVs, room thermostats and a
LAN gateway.  [Hekkers](http://blog.hekkers.net/tag/hvac) has done lots
of work with with ELV MAX! system (including
[talking](http://blog.hekkers.net/2011/10/16/max-interface-completed/)
to them)

Look into the [AlertMe smart heating
kit](https://www.alertme.com/business/smartheating.html) available
though British Gas.

I should also check for new products on
h[ttp://www.automatedhome.co.uk/category/hvac](http://www.automatedhome.co.uk/category/hvac)

...and figure out [what this very affordable wireless Conrad
TRV](http://www.amazon.co.uk/CONRAD-102950-Radio-energy-saver-regulator/dp/B002SKGMHK/ref=pd_sim_sbs_diy_27/279-2516679-6286153)
does.

...and look into <http://www.salus-tech.com> (they do programmable TRVs
and a bunch of other stuff) (thanks Derek for the link!)

... and look into [Owl's heating
controls](http://www.theowl.com/products/intuitionc.php)!...

The LightwaveRF system looks like a good bet.  There are some questions
I need to answer before going for it though (see below).  LightwaveRF do
have some TRV valves on the market today but these are one-directional
(and hence can't call for heat from the boiler).  "[Complete zonal
bi-directional heating control system (early spring
2012)](http://www.lightwaverf.com/forum/viewtopic.php?f=5&t=373)". The
last forum post on the topic suggests that LightwaveRF's heating kit
might be available Q3/Q4 2012.  The LightwaveRF Android software gets
rather bad reviews.

If LightwaveRF doesn't work out then the idea I'm thinking of is
something like this: use Conrad Wireless TRVs, Room Thermostats and
[Boiler
Control](http://www.conrad-uk.com/ce/en/product/560098/Conrad-FHT-8W-demand-control-heating-relay-IP65/SHOP_AREA_32573&promotionareaSearchDetail=005)
for basic heating control (still need to figure out exactly how the FS20
system will control the UFH). Then use a
Nanode+[JeeLabsWireless](http://jeelabs.org/?s=FS20) to add an
open-source "Internet gateway" to the FS20 system to allow for remote
control and monitoring of the heating system. One of the nice properties
of this system is that, when we move house (which may be in only a few
year's time), I can remove the DIY components from the system (i.e. the
Nanode) and the core FS20 system will continue to work.

I still need to look into the Homematic system.

And I also need to consider if I really want central programming.  The
easiest solution would be just to add programmable TRV heads to each
radiator (can be bought for £15-35 each) and forget about controlling
the system from the network.  I could add a simple Nanode system to turn
the boiler on/off from the web.

### LightwaveRF

-   [Manufacturer's website](http://jsjs.gostorego.com/heating-1.html)
-   [official youtube
    channel](http://www.youtube.com/user/lightwaverf/feed)
-   [Official forum](http://www.lightwaverf.com/forum)
-   free iPhone app - use locally or remotely
-   [Android
    App](https://market.android.com/details?id=com.w5h.lightwaverf&hl=en);
    gets mixed reviews; doesn't yet work with ICS or Honycomb
-   Rad valve = £29; Thermostat = £19 (don't think you need the external
    thermostat); wifi-link = £99
-   Several threads on AVforums
    -   [LightwaveRF automation - anyone tried
        yet?](http://www.avforums.com/forums/home-automation-lighting-security-climate-control/1442211-lightwaverf-automation-anyone-tried-yet.html)
-   [in depth
    review](http://www.automatedhome.co.uk/Reviews/LightwaveRF-Home-Automation-System-In-Depth-Review.html)
    (i need to read this)
-   868.3 MHz
-   Kit available for purchase via Amazon,
    [VelmaxLighting](http://www.velmaxlighting.co.uk/lightwaverf-smart-control.html),
    [WirelessLightingStore](http://www.wirelesslightingstore.com/lightwave-rf-central-heating-wireless-control/lightwaverf-wireless-radio-controlled-radiator-valve.html),
    [B&Q](http://www.diy.com/nav/fix/electrical/room-control?fh_view_size=150&fh_start_index=0) (!)
-   In general it looks like the hardware is well received but the
    software is considered a bit poor.  It might be best to wait a short
    while for the kit to mature.

questions:

-   hackable / open API? (some discussion of protocol
    [here](http://www.automatedhome.co.uk/vbulletin/showthread.php?t=3280)
    and
    [here](http://www.lightwaverf.com/forum/viewtopic.php?f=10&t=431))
-   how to control boiler?
-   how to control UFH? (the TRV replacement heads won't fit on my
    UFH manifold) guessing I'll have to use a switchable mains socket or
    something
-   I've heard the heating system can only do 3 zones, is this correct?

### FS20 System

-   [Available from Conrad
    UK](http://shop.conrad-uk.com/home-and-garden/home-automation-systems/remote-control-system-conrad-fs20/fs20-heating-control/)
-   Room kit (bi-directional radio thermostat, actuator, window alarm)
    costs about £63.  If you don't want a bi-directional
    controller (i.e. you don't want to be able to program the controller
    from a PC) then you can get the FHT 8 Set which costs £47.
-   [Boiler
    Control](http://www.conrad-uk.com/ce/en/product/560098/Conrad-FHT-8W-demand-control-heating-relay-IP65/SHOP_AREA_32573&promotionareaSearchDetail=005)
-   Long, long discussion of the system here:
    <http://www.automatedhome.co.uk/vbulletin/showthread.php?s=13d65f2528b4ec0a411d74da4bcff048&t=2050>
-   Gets good reviews on the thread I started here:
    <http://www.diynot.com/forums/viewtopic.php?p=1614404#1614404>
-   Pros:
    -   All wireless
        -   No need to run wires
        -   Could take it when we move (just put the old TRV heads back
            on the rads)
    -   Good value
    -   Cheapest internet control system I've yet found.
    -   There seems to be a good "hacker" environment growing up around
        the system <http://fhz4linux.info/tiki-index.php>
    -   Gets glowing reviews on the Conrad site:
        <http://reviews.conrad-uk.com/7844-en_gb/SHOP_AREA_17199/category.htm>
        (but that's on the Conrad site)
    -   JeeLabs have done some work with talking to the FS20 protocol
        which suggests it may be possible to build and FS20 interface
        with a Nanode <http://jeelabs.org/?s=FS20>
-   Cons:
    -   Looks a bit ugly
    -   Battery powered so have to buy and maintain batteries. But, on
        the plus side, means the devices won't add to our home's
        electricity consumption and no chance of an electric shock

### Controlling our living room UFH system

Current plan: will probably have to give up on the living room's UFH
being connected to the boiler and/or the other controls.

#### Option 1

[Buy the HomeMatic 4-zone Under Floor Heating
system](http://translate.googleusercontent.com/translate_c?hl=en&ie=UTF-8&sl=auto&tl=en&u=http://www.contronics.de/shop/Sonderpakete/Komplettpaket-fuer-Fussbodenheizung%3Fx64d1c%3D8b36af0646b1f35e0b868495a2381b47&prev=_t&rurl=translate.google.com&twu=1&usg=ALkJrhisjhqOwfxx-lO36O5A8mLr1H9PZg)
For 630 euros. This is way over my budget and I only have two UFH zones.
So this option is far from optimal but it does demonstrate that it is
possible to control UFH with FS20

#### Option 2

[Buy the FLV wireless thermostat plus wireless mains
switch](http://translate.googleusercontent.com/translate_c?hl=en&ie=UTF-8&sl=de&tl=en&u=http://www.elv.de/FS20-STR-Funk-Raumthermostat-Set-1-Thermostat,-1-Funk-Schaltsteckdose,-Batterien/x.aspx/cid_74/detail_10/detail2_27605/flv_/bereich_/marke_&prev=_t&rurl=translate.google.com&twu=1&usg=ALkJrhjfIX4IXRSw5p3ZBKxyJmy4MZgJEQ)
for 55.95 euros. Use the mains switch in series with a wired floor probe
thermostat to control a wired actuator (i.e. heat will only be sent to
the floor IF the FS20 thermostat calls for heat AND IF the floor
temperature is below 28 degrees C). Big question: will this system work
with the FHT8W Boiler Control? (I'd guess it does) (update 21/9/10 - no,
the STR thermostat wont work with either the FHT 8W or the FHZ1xxx PC
controllers)

#### Option 3

Buy a [Conrad FHT 80B Room
Thermostat](http://shop.conrad-uk.com/home-and-garden/remote-control-systems/conrad-fs20/fs20-heating-control/750404.html),
a [FS20 AS1
switch](http://shop.conrad-uk.com/home-and-garden/remote-control-systems/conrad-fs20/fs20-switch/620337.html)
and the FHT8W Boiler Control and hope that the 80B can be configured to
talk to the AS1 switch. This wont work if the 80B cannot communicate
with the AS1 switch. (update 21/9/10 - the 80B cannot work with the AS1
switch)

#### Option 4

Buy an [FS20 room thermostat plus wireless actuator plus window
sensor](http://shop.conrad-uk.com/home-and-garden/remote-control-systems/conrad-fs20/fs20-heating-control/751632.html).
Hack the window sensor so that it is connected to a wired floor
temperature probe. This will almost certainly work. The components could
be bought from Conrad-UK or from
[HouseTechSolutions](http://housetechsolutions.co.uk/). (update 21/9/10
- won't work: the FS20 wireless actuators are too bulky to fit onto UFH
manifolds!)

### Honeywell Total Connect

-   <http://www.mytotalconnect.com/comfort/yourhome.php>
-   No details at all.  Cost?  Tech specs?  Detailed feature list?! 
    Nope; just patronising stock photos of "happy families".
-   Prestige 2.0 thermostat costs £279 each!  Rediculous!  But, wait -
    it comes with a "high definition" display; oh joy&lt;/snark&gt;. 
    Seriously guys; stop taking the piss.

#### Bridging the FS20 wireless network to a TCP/IP network or a computer

The [FHZ1300 Radio Home Centre
PC](http://shop.conrad-uk.com/1/2-a2-uk0620371__conrad-fhz-1300-radio-home-centre-pc-652-22-.html)bridges
from the FS20 wireless network to a PC via USB.  Apparently the software
supplied with the FHZ1300 is all in German). PC can then either run the
[Homeputer Web
Server](http://shop.conrad-uk.com/home-and-garden/remote-control-systems/conrad-fs20/fs20-central-sets/750979.html "http://shop.conrad-uk.com/home-and-garden/remote-control-systems/conrad-fs20/fs20-central-sets/750979.html"){.external
.text} for £44 or the GPL'd
[Fhem](http://www.koeniglich.de/fhem/fhem.html "http://www.koeniglich.de/fhem/fhem.html"){.external
.text} software. There is a FHEM iPhone
[app](http://blog.gschaden.com/2009/01/18/fhem-iphone-gateway/ "http://www.gschaden.com/wp/2009/01/18/fhem-iphone-gateway/iPhone"){.external
.text} in development too (or was it just a proof of concept?). The
software is well maintained and the web stuff is optimised for Android
browser. There are more software apps listed here:
<http://fhz4linux.info/tiki-index.php>

### Simple programmable TRV heads

If you simply want programmable thermostats & actuators built into a TRV
head then such things can be bought for as little as £15.  But none seem
to be network-connected.  (e.g. search the Conrad website for Honeywell
HR20). Honeywell make an HR80UK (£80) which wirelessly connects to
either the CM Zone or Evotouch Control Panel.

### Wired actuators

#### <span class="mw-headline">Thermal actuator TS 230 V</span>

-   £18.70 from
    [http://www1.conrad-uk.com](http://www1.conrad-uk.com/ "http://www1.conrad-uk.com"){.external
    .free}
-   Normally closed. Apply constant(?) current to open
-   [The 230v was recalled because the housing can crack, exposing live
    wires](http://recalledproducts.org/recall/view/oreg-eberle-thermal-actuator "http://recalledproducts.org/recall/view/oreg-eberle-thermal-actuator"){.external
    .text}
    -   Possible solutions:
        -   Try to find somewhere to buy the 24v version
        -   or try the Thermal actuator TS+

#### <span class="mw-headline">Thermal actuator TS+</span>

-   <http://www.draytoncontrols.co.uk/NEWTSThermalActuator.aspx>

#### <span class="mw-headline">IDRATEK RVA001</span>

-   <http://www.idratek.com/HWMisc.htm#RVA001>
-   £32
-   Based on the Sauter AXT111-F202

#### <span class="mw-headline">Multi-Fit Thermal Actuator 24v (Low Voltage)</span>

-   <http://www.heatingcontrolsonline.co.uk/multifit-thermal-actuator-24v-low-voltage-p-433.html>
-   £20

#### <span class="mw-headline">Multi-Fit Thermal Actuator 230v</span>

-   <http://www.heatingcontrolsonline.co.uk/multifit-thermal-actuator-240v-p-396.html>
-   £17

### <span class="mw-headline">Programmable room thermostats</span>

<http://www.heatingcontrolsonline.co.uk/programmable-thermostats-c-21_31.html>

### Networked programmable room thermostats

#### [Heatmiser](http://www.heatmisershop.co.uk)

-   Do a wide range of room thermostats including wired, wireless and
    [WiFi](http://www.heatmisershop.co.uk/epages/Heatmiser.sf/en_GB/?ObjectPath=/Shops/Heatmiser/Categories/WiFi_Thermostats).
    Expensive though.  WiFi thermostats start at £149 each.
-   Their "[Internet Remote
    Control](http://www.heatmisershop.co.uk/epages/Heatmiser.sf/en_GB/?ObjectPath=/Shops/Heatmiser/Products/%22Netmonitor%20V3%22)"
    costs £383!

#### <span class="mw-headline">John Guest</span>

-   The John Guest Programmable Room Thermostats can definitely be
    controlled from the web although it's not clear if this control has
    to be done via several hundred quid's worth of boxes or if the
    thermostats have an Ethernet port. I've emailed to ask
    -   <http://www.johnguest.com/part_spec.asp?s=UFHNCSTAT_S1> (link
        broken Jan 2012)
    -   The stats are available for £50 each. A bargain if they do have
        Ethernet ports built in.

#### <span class="mw-headline">1-wire interface to Lux thermostats</span>

<http://hackaday.com/2007/10/24/1-wire-thermostat-control/>

#### <span class="mw-headline">Hacking the Honeywell HR20</span>

<http://openhr20.sourceforge.net/>

#### <span class="mw-headline">Proliphix</span>

-   <http://www.proliphix.com/products-network-basic.htm> \$254

#### <span class="mw-headline">Aprilaire</span>

-   [Aprilaire
    8870](http://www.aprilaire.com/index.php?znfAction=ProductDetails&category=23&item=8870 "http://www.aprilaire.com/index.php?znfAction=ProductDetails&category=23&item=8870"){.external
    .text} Network thermostat. About \$270

#### <span class="mw-headline">KNX</span>

"KNX is a standardised (EN 50090, ISO/IEC 14543), OSI-based network
communications protocol for intelligent buildings. KNX is the successor
to, and convergence of, three previous standards: the European Home
Systems Protocol (EHS), BatiBUS, and the European Installation Bus (EIB
or Instabus). The KNX standard is administered by the Konnex
Association."

[http://en.wikipedia.org/wiki/KNX\_(standard)](http://en.wikipedia.org/wiki/KNX_%28standard%29 "http://en.wikipedia.org/wiki/KNX_(standard)"){.external
.free}

KNX has definitely been used to connect room stats. E.g. [KNX BRINGS
21st CENTURY CONTROL TO HEATING AND OTHER SERVICES IN FARMHOUSE
RENOVATION](http://www.knxuk.org/case_studies.asp#43 "http://www.knxuk.org/case_studies.asp#43"){.external
.text}

A Google Shopping search for "KNX room thermostat" suggests they start
at £125.

There's a KNX touch panel with integrated web server for access from the
web / iPhone <http://www.iddero.com/en/products.php>

And there's a KNX Siemens IP viewer gateway thingy for about £500
<http://www.knxstore.com/knxstore/product/8/siemens-knx-ip-viewer-n-151/lang/en>

There's a KNX valve actuator for £50
<http://www.knxstore.com/knxstore/product/48/siemens-knx-230v-ac-valve-drive-electro-therm-ap-560r>

#### <span class="mw-headline">OpenTherm</span>

<http://en.wikipedia.org/wiki/OpenTherm>

An interesting forum topic on OpenTherm boilers and room stats:
<http://www.diynot.com/forums/viewtopic.php?t=222182&postdays=0&postorder=asc&start=0>

### <span class="mw-headline">Tech notes</span>

-   The connector for TRVs is "swivel nut (M 30x1.5)"

### Quick rant

Having been through the pain of searching for decent home heating
systems, I can't help thinking that this market is long overdue a
fundamental shake up.  Most "modern" products are obscenely over priced,
come with a miserable feature set and are pro-install only.  If someone
can come up with a decent-priced, DIY-installed, wireless heating
control system, with a TCP/IP bridge and an open API (to allow 3rd party
developers to build iOS / Android apps) then I'll be first in the
queue.  The market for thermostats seems to be stuck in the mid-1990s. 
Honeywell, for example, lists "high-definition full-color display" as
the most important feature of its top-spec thermostats, FFS; yet a [2.5"
colour TFT touch screen is only £10 from
Farnell](http://uk.farnell.com/midas/mct022a12tw240320pml/tft-2-2-qvga-portrait-touch-s/dp/2063198).

**update 13/3/2012**: Ars Technica has an article entitled "[The five
technologies that will transform homes of the
future](http://arstechnica.com/business/the-networked-society/2012/03/the-five-technologies-that-will-transform-homes-of-the-future.ars)."
 Guess what number 2 is?  Smart heating and power systems!  (they don't
mention disaggregation though)

**update
7/12/2015**: [http://www.wifithing.com](http://www.wifithing.com/) -
"internet of things made simple" have some home heating controls.

