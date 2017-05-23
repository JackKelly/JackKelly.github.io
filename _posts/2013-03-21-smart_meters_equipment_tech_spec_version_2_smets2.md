---
title: "Smart Meters Equipment Tech Spec Version 2 (SMETS2)"
date: 2013-03-21 20:01:53 +0000
categories: ["smart meters", "PhD", "DECC", "UK", "reactive power"]
permalink: /smart_meters_equipment_tech_spec_version_2_smets2
---
By ~~2019~~ 2020, all homes in the UK will have a smart meter installed.
DECC is working on the spec for these meters at the moment. In the
context of my PhD on smart meter disaggregation, I have several
questions I need to answer about these specs:

-   exactly which power metrics will UK smart meters expose to the home
    area network (HAN)? (just active power? And reactive power? Can we
    distinguish between [leading vs
    lagging](http://en.wikipedia.org/wiki/Power_factor#Definition_and_calculation)? THD?)
-   report rate? (one measurement every 5 seconds? [The 2011 "Functional
    Requirements
    Catalogue"](http://jack-kelly.com/uk_smart_meters_sample_rate_and_reactive_power)
    said "*The smart metering system shall support capture of
    consumption and demand data at 5 second intervals.*"
-   and how could a disaggregation system read these data?

The [Smart Meters Equipment Tech Spec Version 2
(SMETS2)](https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/68898/smart_meters_equipment_technical_spec_version_2.pdf)
was released in Jan 2013. Some useful paragraphs for those of us
interested in disaggregation: <!--break-->

5.3 Physical Requirements...
============================

The HAN \[Home Area Network\] Interface of ESME \[Electricity Smart
Metering Equipment\] shall be capable of:

-   ix\. joining a [ZigBee](http://en.wikipedia.org/wiki/ZigBee) network
    utilising the 2400 – 2483.5 MHz harmonised frequency band; and
-   x\. supporting Communications Links based on ZigBee [SEP \[Smart Energy
    Profile\]](http://www.zigbee.org/Standards/ZigBeeSmartEnergy/Overview.aspx)
    v1 and [DLMS COSEM \[Device Language Message Spec COmpanion Spec for
    Energy
    Metering\]](http://www.dlms.com/information/whatisdlmscosem/index.html).

\[From the Government Response part 1 to SMETS2: "ZigBee SEP v1 will be
specified in SMETS 2 as the HAN application layer standard for gas and
the IHD. For electricity, all communications with the DCC \[[Digital
Communications
Company](http://www.solarpowerportal.co.uk/news/decc_launches_smart_metering_data_communications_company_consultation)
AKA the WAN and ultimately the utility company, I think\] will use DLMS,
‘tunnelled’ over ZigBee SEP. In-premise data transfer between the meter
and the IHD, CAD, and / or PPMID will use ZigBee SEP v1. Suppliers will
be required to demonstrate compliance of their equipment against the
SMETS and the GB Companion Specification... the Government notes that
ZigBee SEP v2 (with required extensions for the GB market) will need
considerable additional work, is not yet proven, and will not be
available within the required timescales. More generally, the Government
recognises that any relevant new protocols which emerge over time could
be introduced into the SMETS, subject to the SEC modification
procedures."\]

### 5.4.8.1 Active Energy Imported

ESME shall be capable of recording cumulative Active Energy Imported in
the Active Import Register(5.6.4.3).

### 5.4.8.2 Active Energy Exported

ESME shall be capable of recording cumulative Active Energy Exported in
the Active Export Register(5.6.4.2).

### 5.4.8.4 Consumption data

ESME shall be capable of recording to:

-   i\. the Cumulative and Historical Value Store(5.6.4.11) in kWh:
    -   a\. Consumption on the Day up to the Local Time;
    -   b\. Consumption on each of the eight Days prior to such Day;
    -   c\. Consumption in the Week in which the calculation is performed;
    -   d\. Consumption in each of the five Weeks prior to such Week;
    -   e\. Consumption in the month in which the calculation is performed; and
    -   f\. Consumption in the thirteen months prior to such month.
-   ii\. to the Daily Consumption Log(5.6.4.14) in kWh the Consumption on
    each of the 731 Days prior to such Day.

### 5.4.8.9 Half hour profile data

ESME shall be capable of recording in each 30 minute period (commencing
at the start of minutes 00 and 30 in each hour), the following
information (including the UTC date and time at the end of the 30 minute
period to which the data relates) in the Profile Data Log(5.6.4.28):

-   i\. Consumption;
-   ii\. Active Energy Exported;
-   iii\. Reactive Energy Imported; and
-   iv\. Reactive Energy Exported.

### 5.4.8.10 Maximum Demand Import data

ESME shall be capable of recording:

-   i\. to the Maximum Demand Active Energy Import Value(5.6.4.21), the
    maximum value of Consumption recorded in any 30 minute period
    (commencing at the start of minutes 00 and 30 in each hour and including
    the UTC date and time at the end of the 30 minute period to which the
    data relates) since the Maximum Demand Active Energy
    Import Value(5.6.4.21) was last reset (as set-out in section 5.5.3.21);
    and
-   ii\. to the Maximum Demand (Configurable Time) Active Energy Import
    Value(5.6.4.22), the maximum value of Consumption recorded in any 30
    minute period (commencing at the start of minutes 00 and 30 in
    each hour) within the time period specified in Maximum Demand
    Configurable Time Period(5.6.3.23) (including the UTC date and time at
    the end of the 30 minute period to which the data relates) since the
    Maximum Demand (Configurable Time) Active Energy Import Value(5.6.4.22)
    was last reset (as set-out in section 5.5.3.23).

### 5.4.8.13 Reactive Energy Imported

ESME shall be capable of recording cumulative Reactive Energy Imported
in the Reactive Import Register(5.6.4.30).

### 5.4.8.14 Reactive Energy Exported

ESME shall be capable of recording cumulative Reactive Energy Exported
in the Reactive Export Register(5.6.4.29).

### 5.4.11.1 Average RMS voltage

ESME shall be capable of calculating the average value of RMS voltage
over a configurable period as defined in the Average RMS Voltage
Measurement Period(5.6.3.5) and:

-   i\. recording the value calculated (including the UTC date and time at
    the end of the period to which the value relates) in the Average RMS
    Voltage Profile Data Log(5.6.4.8);

5.5.1 HAN Interface information provision
-----------------------------------------

ESME shall be capable, immediately upon establishment of a
Communications Link with Type 1 Devices (as set-out in section 5.4.2.1)
and Type 2 Devices (as set-out in section 5.4.2.2), of **providing the
Constant, Configuration and Operational Data (set-out in sections 5.6.1,
5.6.3 and 5.6.4) to Type 1 Devices and Type 2 Devices (with timely
updates of any changes to all data)**.

### 5.5.3.14 Read Operational Data

A Command to read the value of one or more of the operational data items
set-out in section 5.6.4. In executing the Command, ESME shall be
capable of sending such value(s) in a Response via its HAN Interface.

5.6 Data Requirements
=====================

This section describes the minimum information which ESME is to be
capable of holding in its Data Store.

### 5.6.4.3 Active Import Register

The register recording the cumulative Active Energy Imported.

### 5.6.4.4 Active Power Import

The import of Active Power measured by ESME.

### 5.6.4.11 Cumulative and Historical Value Store

A store capable of holding the following values:

-   i\. nine Days of Consumption comprising the current Day and the prior
    eight Days, in kWh and Currency Units;
-   ii\. six Weeks of Consumption comprising the current Week and the prior
    five Weeks, in kWh and Currency Units; and
-   iii\. fourteen months of Consumption comprising the current month and the
    prior thirteen months, in kWh and Currency Units.

### 5.6.4.14 Daily Consumption Log

A log for storing 731 date stamped entries of Consumption arranged as a
circular buffer such that when full, further writes shall cause the
oldest entry to be overwritten.

### 5.6.4.30 Reactive Import Register

The register recording the cumulative Reactive Energy Imported.

6 In Home Display Technical Spec
================================

6.2 Physical requirements
-------------------------

An IHD shall as a minimum include the following components:

-   i\. a Data Store;
-   ii\. a HAN Interface; and
-   iii\. a User Interface.

An IHD shall be mains powered and shall be capable of operating at a
nominal voltage of 230VAC and consuming no more than an average of 0.6
watts of electricity under normal operating conditions.

An IHD shall:

-   iv\. display the IHD Identifier(6.5.1.1);

and be capable of:

-   v\. joining a ZigBee network utilising the 2400 – 2483.5 MHz harmonised
    frequency band; and
-   vi\. supporting Communications Links based on ZigBee SEP v1.

6.3 Functional Requirements
---------------------------

6.3.4 Information pertaining to the Supply of electricity to the Premises
-------------------------------------------------------------------------

An IHD shall be capable, upon establishment of a Communications Link
with ESME (as set-out in section 6.3.1.1), of providing the following
information^3^ on its User Interface and providing updates of any
changes to the information **every 10 seconds thereafter**.

### 6.3.4.8 Instantaneous Active Power Import \[NUM\]

A near real-time indication of the Active Power Import in kW and the
cost to the Consumer of maintaining that Instantaneous Active Power
Import for one hour.

\[no mention of the IHD displaying reactive power or power factor\]

And from ["Government Response to the Consultation on draft licence
conditions and technical specifications for the roll-out of gas and
electricity smart metering
equipment"](https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/43106/4965-gov-resp-cons-tech-spec-smart-meters.pdf)
(published 2012):

1.22 The Consultation proposed that SMETS should enable consumers to
access their energy consumption data over their Home Area Network (HAN)
and transfer consumption information to other devices in the home. Data
could be accessed through a “bridging device”. The Consultation invited
comments on this approach. There was almost unanimous agreement that a
bridging device or Consumer Access Device was the most suitable way to
provide the consumer with access to information from smart metering
systems. The Government has decided that the capability will be included
in the SMETS to provide access to information for consumer devices and
will continue to consider how best to support secure and consumer
friendly access to consumer data locally. It is intended that the
proposed operational licence condition will place a requirement on
energy suppliers to make consumption data available to consumers via
this bridging device. These requirements will be defined in future
iterations of the SMETS as necessary.

Consumer access to consumption data
===================================

Summary of issue
----------------

The Consultation proposed that SMETS should enable consumers to access
their energy consumption data over their HAN and enable transfer of
consumption information to other devices in the home. Having considered
three options (a “bridging” device, a physical port within the smart
metering system, or inclusion of a second transmission system), the
Government proposed that access to data should be enabled via a
“bridging device”. The Consultation invited comments on this approach.
The Consultation also stated that the Government intended to develop a
secure but consumer friendly connection process to enable access.

Government consideration of issue
---------------------------------

4.73 An important requirement of smart metering systems is the
capability to store 13 months of half hourly consumption data and
provide real time and historic consumption and pricing information to
consumers. Through the Consultation, the Government examined how to
enable consumers to access their own consumption data locally, i.e. in
their home and not via their supplier, taking into account the need to
protect data privacy and ensuring that the security of the End-to-End
Smart Metering System is maintained.

4.74 On this issue there was almost unanimous agreement that a bridging
device or Consumer Access Device (CAD) (**envisaged to be a secure
wireless connection that will convert and transmit the information
available via the HAN interface to equipment in the home such as routers
and dongles**) was the most suitable way to provide the consumer with
access to information from smart metering systems.

Government conslusion
---------------------

The Government has decided that the capability will be included in the
SMETS to provide access to information for consumer devices. The
Government has decided to introduce an operational licence condition
(see section 2). The Government intends that this would include a
requirement for energy suppliers to make energy consumption data
available to consumers from the smart metering system.

On the topic of CADs, The Government Response part 1 to SMETS2 says:

> several options exist for pairing Consumer Access Devices (CADs) with
> the communications hub. The Government continues to assess these
> (particularly in terms of the consumer experience, and security), but
> is confident that none are likely to result in any further amendments
> to SMETS 2.

Conclusions
===========

This is the "first iteration" of SMETS2, so things may change.

### Will a measure of reactive power be available over the HAN?

So, I take from the published docs that it should be possible to request
both reactive and active cumulative energy measurements over the HAN,
although off-the-shelf IHDs won't bother to display reactive power.

### Sample period

~~On the topic of sample period, SMETS2 makes *no* mention of a 5 second
sample period. In contrast, [DECC's "Functional Requirements
Catalogue"](http://www.decc.gov.uk/assets/decc/Consultations/smart-meter-imp-prospectus/1480-design-requirement-annex.pdf)
(30th March 2011) section ES.11 stated that "*The smart metering system
shall support capture of consumption and demand data at 5 second
intervals.*" Instead SMETS2 talks about "*timely updates*" / "*ten
seconds*". So I'm a little unclear. SMETS2 doesn't mention anything
about the rate at which the *meter* should sample; instead the "10
seconds" figure is for the IHD update rate. Is it possible that the
meter will still be required to sample at 5 second intervals (as stated
in the 2011 document) but that IHDs will only be required to display
data every 10 seconds? (Which is less of a worry for disaggregation
researchers because we could use our own Consumer Access Device to pull
5-second data from the meter). Dropping to 10 seconds will, I fear, have
an impact on disaggregation performance.~~

~~**update 25/3/13: I've just spoken to a very helpful person at DECC.
Smart meters will allow access to *changes* in active power consumption
at a rate of "better than 10 seconds".**~~

**update 27/3/13: see the section below on "Push or pull?"**

### Leading / lagging / four-quadrant measurement

Meters will measure:

-   reactive energy imported
-   reactive energy exported
-   active energy imported
-   active energy exported

[This really useful
PDF](http://style.landisgyr.com/apps/products/data/pdf1/Power_Flow_2.pdf)
(especially illustration 2) describes the relationship between leading /
lagging; reactive import/export and active import/export and the
"four-quadrant" metering. ~~From this, it looks like SMETS2 meters will
effectively provide four-quadrant metering (i.e. amongst other things we
will be able to distinguish between capacitive and inductive reactive
loads).~~

~~**update 25/3/13: I've just spoken to a very helpful person at DECC.
Smart meters will only report active power over the HAN, not
reactive.**~~

**update 27/3/13: see the section below on "Push or pull?"**

### THD

There's no mention of measuring total harmonic distortion
(unsurprisingly)

### Allowing users to get at their own data from within the home

Consumer Access Devices (CADs) should allow users to get access to their
own data (and hence use this data for disaggregation).

### Push or pull? **update 27/3/13:**

It seems I had failed to understand that there's a distinction between
the smart meter *pushing* data onto the HAN and other HAN devices
*pulling data from* the smart meter.

For the "push" mode, it seems that the smart meter will only push active
power data (not reactive). It will only push data if there's a change.
The fastest rate the meter will push data is 0.1Hz. It will be
considerably slower than this during periods of little change. The specs
haven't defined a threshold for what counts as a "change".

For the "pull" mode, **devices can poll for active power data from the
meter "as often as they wish"**. In the draft specs, the CAD can request
the historic half hourly reactive energy data (3 months worth). There
are no plans to make real time reactive power available; but a firm
decision hasn't yet been taken on this.

The active power readings are instantaneous values as determined by that
particular meter’s sampling / averaging algorithm. DECC's specs do not
place any requirements on this area.

