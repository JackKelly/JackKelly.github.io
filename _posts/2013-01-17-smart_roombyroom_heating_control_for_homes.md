---
title: "\"Smart room-by-room heating control for homes\""
date: 2013-01-17 14:31:09 +0000
categories: ["heating", "student project", "OpenTRV"]
permalink: /smart_roombyroom_heating_control_for_homes
---
Imperial MSc Computing Science students do [a 3-month individual project
over summer](http://www.doc.ic.ac.uk/lab/msc-projects/). Below is
another proposal I and my Ph.D. supervisor have just submitted. Of
course, there are no guarantees that any students will be interested...

<!--break-->

**Update: Dr Knottenbelt and I are planning to supervise at least two
students on this project. And it looks like an industrial partner may
(very kindly) be able to provide us with some PIR occupancy data for
doing room occupancy prediction.**

"Smart room-by-room heating control for homes"
==============================================

On average, heating a home for a year costs about £600 and produces
about 2.5 tonnes of CO2. Yet existing heating controls are really,
really dumb and hence waste a lot of energy heating empty rooms. Smarter
controls have been shown to reduce the energy required to heat a home by
up to 30% and can potentially make a home more comfortable. The basic
hardware setup includes:

-   Networked electronic radiator valve actuators to replace existing
    mechanical thermostatic radiator valve (TRV) heads. These provide
    room-by-room control of heating. Existing units are low cost
    (&lt;£30 per room), user-installable and battery powered (e.g. the
    [iTemp i30](http://www.saveonheatingbills.co.uk/Product/index.html)
    (pictured below), the [ELV
    TRV](http://translate.googleusercontent.com/translate_c?depth=1&ei=X973UJu5GI_64QSs8oGADA&hl=en&prev=/search%3Fq%3Delv%2Bmax!%26hl%3Den%26client%3Dubuntu%26hs%3DkCU%26tbo%3Dd%26channel%3Dfs%26gl%3Duk%26biw%3D1600%26bih%3D786&rurl=translate.google.co.uk&sl=de&twu=1&u=http://www.elv.de/max-funk-heizungsregler-system.html&usg=ALkJrhiZtJuNn9vasxEGKPufZSy-vJiXKA))
    ![](http://www.saveonheatingbills.co.uk/img/product/prodPic.gif)
-   A networked boiler controller. Instead of controlling the boiler
    using a single timer and single thermostat, allow each room to call
    for heat from the boiler.
-   A "bridge" to connect the system to the home's TCP/IP network,
    allowing users to modify their heating schedule from a smart phone
    or tv or from outside the home.

Suitable software would enable features such as:

-   Room-by-room temperature schedules (e.g. heat the kitchen for
    breakfast and dinner; heat the living room for the evening etc)
-   Use the boiler as efficiently as possible (minimise the water
    temperature returning to the boiler to try to keep the boiler in
    ["condensing mode"](http://en.wikipedia.org/wiki/Condensing_boiler))
-   Allow users to easily modify heating schedules from the home or over
    the network (e.g. from a smart phone). e.g. If you make a
    last-minute decision to go out for a pint then remotely tell the
    heating system to delay the start of the evening's heating.
-   Weather compensation (including both locally-installed external
    temperature sensors and downloaded forecasts to decide whether to
    bother putting the heating on in the morning)
-   The system should have a (user-configurable) degree
    of "intelligence". For example, the system could attempt to learn
    when particular rooms are occupied and the target temperature of
    preference for each occupant. Occupancy information could come from
    a variety of sources including: smart phone GPS (for house
    occupancy, not room occupancy), smart electricity meter
    disaggregation (if the TV is on then someone is probably in the
    living room), security system movement detectors, on-line
    calendar etc.
-   multi-user (most houses have more than one person living in them!
    each will have different preferences and schedules)
-   (more ideas listed
    [here](http://jack-kelly.com/a_better_central_heating_control_system))

Commercial solutions do exist but they tend to be prohibitively
expensive and/or use proprietary APIs and protocols (which means they
can't be integrated into smart home systems). An open-source heating
project has recently been started called
[OpenTRV](http://www.earth.org.uk/open-source-programmable-thermostatic-radiator-valve.html)
("TRV" stands for "thermostatic radiator valve").

Aim of the MSc project
======================

The aim of this MSc project would be to contribute a useful "module" to
the OpenTRV project. Exactly what you work on will be up to you.
Possible projects include:

-   Automatically learn the thermal properties of the house and/or
    occupancy patterns (the temperature data might have to be simulated
    given that the project will run during summer!)
-   In conjunction with the "Automatically learn the thermal properties
    of the house and/or occupancy patterns" item, consider the simplest
    possible TRV UI (buttons, lights, LCD display, sound, tactile
    feedback, etc) and hardware (occupancy detection, window/door-open
    sensors, light levels, relative humidity, noise levels, etc) that
    could robustly deduce heating patterns with at least some way of
    manually forcing the valve off (other than frost protection) for
    holidays, and on, at least for a while, for visitors or temporary
    alternations in routine. Model how much energy an automatic
    'setback' of a degree or so when a room is unoccupied, and what
    impact it could have on user comfort given the thermal mass and rad
    size of a room, and conversely how much it could improve convenience
    by needing little manual interaction. Do with a (supplied) regular
    occupancy pattern (eg child's bedroom) and a more sporadic or
    unusual one, such as maybe a student's or a night-shift worker's.
-   Model the building's physics to propose the most efficient heating
    schedule given a set of user-defined scheduling constraints
-   Hack / reverse-engineer an existing product so the OpenTRV project
    can interact with it. For example, add a
    [ZigBee](http://en.wikipedia.org/wiki/ZigBee) radio transceiver to
    the [iTemp
    TRV](http://www.saveonheatingbills.co.uk/Product/index.html) either
    by completely replacing the "brains" with something like a [Texas
    Instruments CS2530 ZigBee
    system-on-a-chip](http://www.ti.com/ww/en/analog/cc2530/index.shtml)
    (a single chip with both the ZigBee radio, a small processor, 8KB
    RAM and 32-256KB flash) or by hacking the existing firmware and
    adding a radio transceiver module like the
    [RFM12b](http://www.hoperf.com/rf/fsk/21.htm) (this will require
    some soldering)
-   Design, implement and test a secure "mesh networking" protocol to
    run on battery-powered radiator valves using low cost radio
    transceivers like the [RFM12b](http://www.hoperf.com/rf/fsk/21.htm).
    Needs to consume as little energy as possible to maximise battery
    life; but also needs to be responsive, reliable and resilient to
    failure of individual nodes. (Or just use
    [ZigBee](http://en.wikipedia.org/wiki/ZigBee)!)
-   Weigh pros and cons of simple star network using, for example,
    RFM12b modules vs mesh network (eg extra complexity and power drain
    for radios on more).
-   Research, design, implement and test algorithms to use the home's
    heat source as efficiently as possible. The heat source might be a
    modulating boiler, non-modulating boiler, heat pump, sunlight
    entering through south-facing windows etc. The "radiators" might be
    normal radiators or underfloor heating.
-   Design, implement and test the entire heating control system!
-   Review what already is already implemented and develop your own
    robust protocol to minimise radio on time for RX and/or TX (and thus
    energy consumption) for various components of the system such as
    TRVs, boiler interlock, any home automation gateway. Try to do this
    with and without the benefit of a local real-time clock, and maybe
    look at real microcontrollers such as PICAXE, JeeNode, etc to test
    the protocols and energy efficiency and timing accuracy. Look at the
    various trade-offs possible in battery life, system reliability,
    user annoyance and effort, etc...
-   Explore whether adding randomness deliberately to any of the
    algorithms may improve behaviour/performance, eg reduce collisions,
    "deadly embraces", etc, and explore what may already be in use in
    lower levels of any systems that you look at, eg in the
    radio protocols.

Some of these things are covered by patents so a patent search will be
necessary during the literature review.

We can provide funding to buy hardware. And we have some basic tools to
assist with reverse-engineering existing products and soldering. Some of
the tasks above might sound like they are "electrical engineering"
projects rather than CS projects but the electrical engineering involved
in, say, adding a new radio to an existing product should be pretty
minimal (and is something we can help with). The real work is the
programming and whole system algorithm design and robustness.

Further reading
===============

-   Bălan, Radu, Joshua Cooper, Kuo-Ming Chao, Sergiu Stan, and
    Radu Donca. ‘Parameter Identification and Model Based Predictive
    Control of Temperature Inside a House’. Energy and Buildings 43, no.
    2–3 (March 2011): 748–758.
    doi:[10.1016/j.enbuild.2010.10.023](http://dx.doi.org/10.1016/j.enbuild.2010.10.023).
-   Collotta, M., G. Nicolosi, E. Toscano, and O. Mirabella. ‘A
    ZigBee-based Network for Home Heating Control’. In 34th Annual
    Conference of IEEE Industrial Electronics, 2008. IECON 2008, 2724
    –2729, 2008.
    doi:[10.1109/IECON.2008.4758389](http://dx.doi.org/10.1109/IECON.2008.4758389).
-   Scott, James, A.J. Bernheim Brush, John Krumm, Brian Meyers, Michael
    Hazas, Stephen Hodges, and Nicolas Villar. ‘PreHeat: Controlling
    Home Heating Using Occupancy Prediction’. In Proceedings of the 13th
    International Conference on Ubiquitous Computing, 281–290.
    UbiComp ’11. New York, NY, USA: ACM, 2011.
    doi:[10.1145/2030112.2030151](http://dx.doi.org/10.1145/2030112.2030151)
-   [OpenTRV web
    page](http://www.earth.org.uk/open-source-programmable-thermostatic-radiator-valve.html)
-   Robert Hekker's [hacking of ELV home heating
    systems](http://blog.hekkers.net/tag/hvac/)
-   earth.org.uk's ["note on smart heating for small buildings in the
    UK"](http://www.earth.org.uk/note-on-smart-heating.html)
-   Some thoughts on ["a better central heating control
    system"](http://jack-kelly.com/a_better_central_heating_control_system)


