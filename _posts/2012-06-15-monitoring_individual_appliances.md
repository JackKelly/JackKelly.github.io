---
title: "Monitoring individual appliances"
date: 2012-06-15 14:59:49 +0000
categories: ["PhD", "CurrentCost"]
permalink: /monitoring_individual_appliances
---
For some time I've been monitoring my home's aggregate power consumption
using a [CurrentCost
EnviR](http://www.currentcost.com/product-envir.html).  I'm now planning
to upgrade my monitoring hardware.  Firstly, I want to install
[CurrentCost Individual Appliance Monitor
plugs](http://www.currentcost.com/product-iams.html) on my appliances
(£13.33 each).  Secondly, I want to measure aggregate real, reactive
power and voltage using an [Open Energy
Montitor](http://openenergymonitor.org/emon/emontx).

### List of appliances to monitor

(each Current Cost ENVI display can only cope with 9 IAMs)

 

<div>

A (livingroom)

</div>

1.  TV
2.  Amp
3.  Subwoofer
4.  HTPC
5.  Washing machine
6.  ADSL modem
7.  Livingroom lamp1
8.  Livingroom lamp2
9.  Livingroom lamp3

<div>

 

</div>

<div>

B (livingroom)

</div>

1.  Bedroom1 lamp1
2.  Bedroom1 lamp2
3.  Bedroom2 lamp
4.  Bedroom DAB radio etc
5.  Hair dryer
6.  Hair straighteners
7.  Iron
8.  Hoover

<div>

 

</div>

<div>

C (in study)

</div>

1.  Toaster
2.  Kettle
3.  Coffee Maker / Bread Maker
4.  Microwave
5.  Fridge
6.  Kitchen Radio
7.  Dish washer
8.  Kitchen lamp

<div>

 

</div>

<div>

D (in study)

</div>

1.  Laptop
2.  Desktop
3.  24" LCD
4.  Office HiFi
5.  Study lamp1 & lamp2 (sharing a plug)
6.  Printer
7.  GigE switch
8.  Fan
9.  Battery charger

### Cost

-   33 CurrentCost [individual appliance
    monitors](http://www.amazon.co.uk/gp/product/B005ERF3SI/ref=as_li_ss_tl?ie=UTF8&tag=aratedcom0d-21&linkCode=as2&camp=1634&creative=19450&creativeASIN=B005ERF3SI) =
    11 packs of 3 each = 11 <span class="Unicode">×</span> £39.95 =
    £439.45
-   3 more [Current Cost EnviR base
    stations](http://www.amazon.co.uk/Current-Cost-EnviR-White-Display/dp/B004QBSUW4/ref=sr_1_8?s=electronics&ie=UTF8&qid=1339772684&sr=1-8) (each
    can only handle 10 sensors) =3 <span class="Unicode">×</span> £27.99
    = £83.97
-   3 more [Current Cost USB
    cables](http://www.amazon.co.uk/Current-Cost-Data-Cable-RJ45/dp/B002FVT3XW)
    = 2 <span class="Unicode">×</span> £8.50 = £25.50
-   OpenEnergyMonitor (to measure aggregate real, reactive and voltage)
    = £27 for[ emonTx
    kit](http://shop.openenergymonitor.com/transmitters/) + £10
    for [CT](http://shop.openenergymonitor.com/ac-ac-adapter-uk-plug/) +
    £13 for [AC-AC voltage
    sensor](http://shop.openenergymonitor.com/ac-ac-adapter-uk-plug/) +
    £30
    for [BaseStation](http://shop.openenergymonitor.com/base-stations/) (I
    need to check if my existing [Nanode](http://www.nanode.eu/) will
    work with the addition of an [RFM12b
    module](http://www.hoperf.com/pro/rf/cob/RFM12B.htm) available from
    [RS for
    £6.17](http://uk.rs-online.com/web/p/radio-telemetry-data-modules/7312785/))=
    £80
-   TOTAL = £628.92

### Update 21/6/2012

I bought 3 CurrentCost Individual Appliance Monitors to test.  They
seeem to work well.  My main concern was that the wireless range would
be too short to allow me to monitor every appliance in my house but the
wireless range seems fine.  Sure, the system drops a few more samples
from the wireless monitor that's furthest from the CurrentCost EnviR but
the data is entirely usable.  I've modified [my Python logging
script](https://github.com/JackKelly/currentCostCosmTX) to handle
multiple sensors.

<!--break-->

