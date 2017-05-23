---
title: "Buying and installing a smart meter"
date: 2012-11-15 10:43:06 +0000
categories: ["PhD", "smart meters"]
permalink: /buying_and_installing_a_smart_meter
---
![PM1200](http://www.schneider-electric.co.uk/images/datasheet/electrical-distribution/PM1000V1-series-main.jpg)

I'd like to install a [smart meter](/what_is_a_smart_meter) so I can
collect whole-house readings of *real* and *reactive* power and voltage
once every five seconds for my PhD work on disaggregation. For several
months I've been prodding my utility company to replace my
"spinning-disk" meter with a smart meter but this isn't going to happen
any time soon, even if I offer to pay for the hardware and installation.
The existing spinning-disk meter is owned by the utility company so I
can't touch it. So my plan is to hire an electrician to install a smart
meter *downstream* of my spinning-disk meter. This blog post is just my
notes about smart meters (which to buy? how to communicate with it?
etc.) <!--break-->

Smart meter shops
=================

-   [SmartElectricityMeters.co.uk](http://smartelectricitymeters.co.uk)
-   [Universal Meter
    Services](http://universalmeterservices.co.uk/store/index.php?main_page=index&cPath=24)
    (only sells the ISKRA ME372 as of Nov 2012)
-   [StephenPWales](http://www.stephenpwales.co.uk/Product/single_phase/1phasex.php)

Open Energy Monitor
===================

-   [EmonTX](http://openenergymonitor.org/emon/emontx) can take 3 CT
    clamps
-   [Accuracy appears to be
    good](http://openenergymonitor.org/emon/node/974) (above 40 watts)

Schneider Electric
------------------

### [Energy Meter](http://www.powerlogic.com/product.cfm/c_id/1/sc_id/6/p_id/24) (extended range plus communications board)

![Energy
Meter](http://www.powerlogic.com/pics/fulls/EnergyMtrwebgraphic.jpg)

-   Not sure if I need the "extended range" model or not for 230V single
    phase? Most likely I just need the basic model.
-   Update interval???
-   1,2 or 3 CTs (which open to allow easy installation)
-   +-1% accuracy from 2% to 100% of CT rating (on a 100A CT this means
    accuracy drops off below 500W!)
-   [Comms
    board](http://www.powerlogic.com/literature/63230-216-213A1.pdf)
    provides RS485 modbus RTU

### [Enercept Meter](http://www.powerlogic.com/product.cfm/c_id/1/sc_id/6/p_id/23)

![Enercept](http://www.powerlogic.com/pics/fulls/EnerceptMtrwebgraphic.jpg)

-   Meter is in the CT
-   Enhanced model gives real, reactive and apparent and voltage
-   +-1% from 10-100% of CT rating (not great for my application).

<a name="PM1200">

### [PM1200](http://www.powerlogic.com/product.cfm/c_id/1/sc_id/4/p_id/56#) </a>

![PM1200](http://www.schneider-electric.co.uk/images/datasheet/electrical-distribution/PM1000V1-series-main.jpg)

-   £261.35
-   Accuracy? "1% of reading. Additional error of 0.05 of full scale for
    meter input current below 100mA". CTs deliver 0-5Amps. Lowest CT
    is 40A. 0.1/5 = 2% (same as Energy Meter). 2% of 40A = 0.8A.
    0.8A\*230V = 184W.
-   "Entry range power meter"
-   updates readings once per second
-   active power (class 1 accuracy), reactive power (class 2 accuracy),
    voltage, current, frequency, power factor

### [ION6200](http://www.schneider-electric.co.uk/sites/uk/en/products-services/electrical-distribution/products-offer/metering-monitoring/power-monitoring-devices/powerlogic-ion6200.page) with EP\#2

![ION6200](http://www.schneider-electric.co.uk/images/datasheet/electrical-distribution/se-6200-side-main.jpg)

-   Measures current using a CT clamp
-   4-quadrant metering, class 0.5 accuracy (IEC, ANSI) 0.5%
-   Voltage, current, power, frequency, power factor, demand, energy
-   RS-485 communications port Modbus RTU slave
-   64 samples per cycle (3.2kHz sample rate at 50Hz mains)
-   The ION6200 EP\#2 "M6200 A0 A 0 B 0 A0 A 0 R" costs £327.14

### For details of PowerLogic, contact:

-   Peter Meredith 01249 456 020. pete.meredith@schneider-electric.com

[Other Schneider Electric power monitoring
devices](http://www.schneider-electric.co.uk/sites/uk/en/products-services/electrical-distribution/products-offer/metering-monitoring/power-monitoring-devices/power-monitoring-devices.page).
The
[PM800](http://www.schneider-electric.co.uk/sites/uk/en/products-services/electrical-distribution/products-offer/metering-monitoring/power-monitoring-devices/powerlogic-pm800.page)
looks interesting but perhaps too advanced for my application.

-   [CT
    clamps](http://www.schneider-electric.co.uk/sites/uk/en/products-services/electrical-distribution/products-offer/metering-monitoring/current-transformers/ti.page#)
    (I think I need the 40A clamp for cables routed through the clamp,
    cat number 16500). These clamps do not appear to open so will need
    cables to be disconnected to be re-routed through the clamp.

[Nipun Batra](http://nipunbatra.wordpress.com/) uses a Schneider
Electric EM6400 (with RS485) with a 60:5 turn ratio class 5 CT with
accuracy 0.1%.

EM21-72D DIN Rail or Panel Mount Electricity meter
--------------------------------------------------

-   http://jdmetering.co.uk/single-phase-meters/em21-72d-din-rail-or-panel-mount-electricity-meter.html
-   CT-connected and has a pulse output and RS485 Modbus communications.
-   A full set of instrumentation values (Voltage, Current etc.) is
    available on the multi-line LCD display. Class 1 accuracy.
-   £102 inc VAT

Single-phase direct-connect smart meters
========================================

[Elster A102C](http://www.elstermetering.com/en/949.html)
---------------------------------------------------------

-   IrDA ([this blog](http://www.rotwang.co.uk/projects/meter.html)
    describes reading the IrDA from an A100C to get real power,
    apparently once a second).
-   [Dr (Prof?) Gregory has used a laptop's IrDA adapter to talk to a
    A100C](http://cgi.csc.liv.ac.uk/~greg/projects/rdmeters.html) and he
    describes some of the packet structure. No mention of
    reactive power.
-   The A102C gives gives kwh and kvarh measurements. I need the "Import
    kWh and kvarh, one rate" version with IrDA. Register 2 = Total kWh.
    Register 3 = Total kvarh (ADD kvarh Q1 lagging/inductive
    reactive import). "[Most reactive loads are inductive, so at most
    sites the PF is
    lagging](http://wiki.answers.com/Q/What_is_the_difference_between_lagging_power_factor_and_leading_power_factor)"
-   The A103C gives voltage and current (as well as kvarh?) but isn't
    readily available in the UK
-   Low cost and relatively compact
-   [A100C Operating and Maintenance
    Instructions](http://www.meterspec.com/143.pdf)
-   Purchase from Energy ICT on 01920 871094
-   could get 2: one for aggregate, one for lighting circuit (but buy
    just one to start with to make sure it works as I want)

[Elster A220](http://www.elstermetering.com/en/865.html)
--------------------------------------------------------

-   Current favourite
-   Optional RS485
-   Measuring instantaneous values
-   active, reactive and apparent
-   emailed Elster on 5/12/12 for more details
-   emailed [Tony
    Townley](http://www.elstermetering.com/en/electricity_metering_europe.html)
    (UK sales for Elster UK) on 3/1/2013
-   emailed JWInstruments and smartprocess.co.uk to ask if they can get
    hold of an A220.

[Elster AS230](http://www.elstermetering.co.uk/en/AS230.html)
-------------------------------------------------------------

-   [buy](http://smartelectricitymeters.co.uk/Elster%20AS230)
-   Specifically mentions WAN (wide area network) and HAN (home
    area network) in the specs
-   optical bidirectional IEC 62056-21 comms port. "The modular and
    optical port can be used to read data from any meter connected to
    the HAN... HAN interface will be available to match
    market requirements... M-Bus allows any remote meter to be read
    directly by the Utility or to be viewed on the Home Display."
-   "If you do want a live stream there is something called a live link
    that will show readings every few seconds for as long as the
    optical (62056-21) port is open"
-   CURRENT FAVOURITE (as of9th Jan 2013)
-   PC software is available.

[Elster A1140](http://smartelectricitymeters.co.uk/Elster%20A1140)
------------------------------------------------------------------

-   kWh import/export, kvarh and kVA
-   serial comms option "Communications are provided via the optical
    port and are supported by data stream mode, allowing fast reading of
    meter data. The A1140 permits up to 90 days of load profile data to
    be collected in less than 30 seconds. The RJ11 socket provides
    optional serial communications allowing remote access to the same
    data as the optical port."

[Iskra ME372](http://www.iskraemeco.si/emecoweb/eng/products/me372.html)
------------------------------------------------------------------------

-   [buy Iskra
    ME372](http://smartelectricitymeters.co.uk/Iskra%20ME372-ME372)
-   OFGEM approved
-   Need to specify options:
    -   RS485 instead of GSM/GPRS. Protocol: IEC 62056-46 (DLMS) on a
        GSM modem and optionally on RS485
    -   Reactive energy measurement (as well as active)
-   RTC sync by comm
-   instantaneous readings for active power, reactive power and voltage
    are **not** available over the RS-485 interface (deal breaker
    for me)
-   Accuracy class: 1 or 2 (active energy), 2 or 3 (reactive energy)
-   I [emailed
    Iskraemeco](http://www.iskraemeco.si/emecoweb/eng/privat/contact.html)
    on 16/11/12 to ask for more details; they replied on 20/11/12 and I
    have updated the above to reflect the new info.

[LANDIS+GYR E470](http://smartelectricitymeters.co.uk/Landis%20Gyr%20E470-E470)
-------------------------------------------------------------------------------

-   Pre-payment meter
-   No RS-485. Just optical serial.
-   Not clear if it can measure reactive power, or how frequently
    it measures.

[It looks
like](http://www.landisgyr.com/uk/en/pub/products_and_solutions.cfm) the
only meters Landi+Gyr sell in the UK are prepayment meters.

[EMGSM1](http://smartelectricitymeters.co.uk/EMGSM1)
----------------------------------------------------

-   Measures active, reactive, volts, current, power
-   No mention of ANY comms other than GSM.

Hardware used by [Kolter and Johnson's REDD system](https://www.zotero.org/jack_kelly/items/collectionKey/A2B7QF6C/itemKey/WPHH82KW/q/redd)
===========================================================================================================================================

-   [Enmetric PowerPort and Wireless
    Bridge](http://www.enmetric.com/platform#Hardware) for plug-level
    data

    -   Bridge talks to up to 50 PowerPorts and connects to Ethernet
        port
    -   802.15.4 wireless comms
    -   1Hz sample rate
-   [Powerhouse Dynamics
    eMonitor](http://www.powerhousedynamics.com/residential-energy-efficiency/)
    for circuit-level monitoring

    -   About USD 500 - 1000 depending on spec
    -   up to 24 CTs
    -   1 sample every 3 seconds over API
-   Two 200A TED CTs and Pico TA041 'scope probe to measure voltage
    (100:1 step down), connected to a National Instruments NI-9239 ADC
    (24-bit 15kHz)

Hardware used by Kim et al 2011
===============================

-   Zigbee wireless sensor network using [Digi
    kit](http://www.digi.com/products/).
-   Power data collected every 3 seconds.

Other plug-level metering solutions
===================================

-   Plugwise Pro 50. 50 IAMs for £2055 (£41 per IAM.) ZigBee. Each IAM
    is called a "[Circle](http://www.plugwise.com/idplugtype-g/circle)"

Getting data from the meter
===========================

Most meters appear to support MODBUS over RS-485. My plan would be to
install the meter in the fuse box and run an RS-485 cable to the
cupboard under the stairs, where a laptop would log data from the smart
meter and from my individual appliance monitors.

[RS-485](http://en.wikipedia.org/wiki/RS-485)
---------------------------------------------

-   Only specified the electrical characteristics, not the protocol.
-   RS-485 to USB converters cost about £35
-   From Nipun: "Beyond 10 metres, RS485 communication requires very
    expensive cabling... For cabling, if length is less than 10m, you
    can use metal shielded cable having 2 wires and
    plastic encapsulation. For more length, you need to put double
    shielded cable (which is much more costlier)"

[MODBUS](http://en.wikipedia.org/wiki/Modbus)
---------------------------------------------

-   Serial comms protocol.
-   Open and royalty-free.
-   Several different versions (RTU, ASCII, Modbus over TCP/IP etc)
-   [minimalmodbus](http://pypi.python.org/pypi/MinimalModbus/)
    Python library. Recommended by [Nipun
    Batra](http://nipunbatra.wordpress.com/).
-   [libmodbus](http://libmodbus.org/), written in C.
    Currently maintained. Can send/receive data using serial port
    or Ethernet. [Official Ubuntu
    package](http://packages.ubuntu.com/search?keywords=libmodbus)
    (available for 12.04 Precise, 12.10 Quantal and 13.04 Raring).


