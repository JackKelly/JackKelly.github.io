---
title: "UK Smart Meters: sample rate and reactive power"
date: 2011-10-13 16:46:53 +0000
categories: ["smart meters", "reactive power", "UK", "PhD", "DECC"]
permalink: /uk_smart_meters_sample_rate_and_reactive_power
---
I've been doing some research on exactly what parameters UK smart meters
will record.

I've found [DECC's "Functional Requirements
Catalogue"](http://www.decc.gov.uk/assets/decc/Consultations/smart-meter-imp-prospectus/1480-design-requirement-annex.pdf).

These are *proposed* requirements rather than confirmed requirements
but, none the less, they are useful.

The functional requirements for electricity smart meters include the
measurement of kW, RMS voltage and kVAr (reactive power). "The smart
metering system shall be capable of storing 13 months of half hourly
(kWh and cubic metres) consumption data." On the topic of sampling
frequency: "The smart metering system shall support capture of
consumption and demand data at 5 second intervals."

(it looks certain that the kW reading will be transmitted over the Home
Area Network but it's not entirely clear whether or not the voltage and
kVAr (reactive power) measurements will also be exposed to the HAN.)

Some more relevant information from the DECC/ofgem document ["Smart
Metering Implementation Programme - Response to Prospectus Consultation
- Supporting Document 3 of 5 - Design
Requirements"](http://www.decc.gov.uk/assets/decc/Consultations/smart-meter-imp-prospectus/1478-design-requirements.pdf):

quoting straight from p41 of the document:

> "Conclusions\
> \* 4.45 The Government has concluded that on the basis of initial
> policy analysis and further evidence presented the objective of IHD
> \[In Home Display\] electricity consumption updates every five seconds
> should remain. In acknowledgement of the current state of HAN \[Home
> Area Network\] technology the initial minimum requirement will be for
> an update frequency better than ten seconds for the HAN. The minimum
> requirement for five second updates will be reflected in future
> functional requirement changes when technology improvements are
> evident. The change to five second updates will be subject to
> governance arrangements for maintaining the technical specifications
> described in Chapter 5.
>
> \* 4.46 For gas, the requirement will be for a HAN update frequency
> not greater than 30 minutes. It is anticipated that battery technology
> and smart metering equipment\
> power consumption will improve in the future potentially allowing for
> more frequent gas IHD updates. As the IHD is capable of operating at
> the significantly higher update frequency requirement for electricity,
> a subsequent improvement in gas\
> update frequency would not impact IHDs already installed. Once again
> the minimum requirement for higher frequency gas updates should be
> reflected in future functional\
> requirement changes when technology and battery improvements are
> evident."

