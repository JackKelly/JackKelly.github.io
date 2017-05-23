---
title: "A better central heating control system"
date: 2011-10-18 07:04:04 +0000
categories: ["heating", "control", "energy efficiency", "nanode"]
permalink: /a_better_central_heating_control_system
---
*Update: The following blog describes my "ideal" central heating system;
the idea being that I'd build this myself if I got the time. It looks
like I won't get the time to build this any time soon so I've started
looking at off-the-shelf solutions. My research on off-the-shelf
solutions is detailed
[here](/existing_central_heating_control_systems).*

I find it remarkable that, in 2011, the average domestic central heating
controller is still so simple and un-user friendly. Domestic heating
accounts for a substantial proportion of the nation's CO<sub>2</sub> output, not
to mention domestic energy bills. There are a few companies making
"smart" heating controllers (e.g.
[PassivSystems](http://www.passivsystems.com/),
[microWatt](http://www.microwatt.co.uk/products/low-carbon-housing),
[HeatingSave](http://www.heatingsave.co.uk)) but the prices are, in my
humble opinion, way too high for kit which is, in technological terms,
not especially advanced. Many "off-the-shelf" smart heating control
systems are installed by a contractor (not DIY) which substantially
bumps up the price.

It seems that it should be possible to build, for a few hundred quid, a
system which will significantly decrease the chances of heating an empty
room (or house), whilst still ensuring the house is comfortable for the
occupants. As such, the system would pay for itself within a few years
and would also make the building more comfortable: a win-win which would
hopefully make the system popular.

I'll quickly describe my perspective: I live in a Victorian house with
gas central heating and thermostatic radiator valves (TRVs) on each
radiator and I recently refurbished our living room (lots of structural
& damp correction work plus internal wall insulation, floor insulation,
wet underfloor heating, lots of attention to airtightness, single-room
MVHR, loads of 1-wire temperature sensors embedded all over the place).
I want a control system which'll cheaply allow us to gain far better
control over our radiators, UFH and boiler. I was planning to use an
off-the-shelf [FS20
system](http://shop.conrad-uk.com/home-and-garden/home-automation-systems/remote-control-system-conrad-fs20/fs20-heating-control/)
without any PC control or modification but it's starting to look like
the FS20 system wont talk to my underfloor heating easily, which is what
got me thinking about creating my own control system. (Some (slightly
outdated) details of my pondering regarding FS20 are
[here](http://automatedhome.co.uk/vbulletin/showthread.php?t=2050&page=19))

Folks like [Ken Boak](http://sustburbia.blogspot.com/) and [Paul
Tanner](https://plus.google.com/113112452691546538779/about) are making
great progress with open-hardware heating controllers.

This page is a wish-list of features for my "ideal" heating controller.

(key: the number after each item indicates its priority: 1=high
priority; 3=nice but not essential).

### Main features

-   Room-by-room control of radiators (using radio-controlled motorised
    TRV heads so easy to install) - 1
-   Room-by-room temperature monitoring and scheduling - 1
-   Boiler doesn't have a "CH schedule". Instead each *room* has
    a schedule. Boiler only fires if 1 or more rooms calls for heat. - 1
-   Gas consumption metering (historical data storage so the user can
    compare, say, November's consumption for the past 10 years. This is
    useful to see the effect of insulation.) - 3
-   Weather compensation (including looking at forecasts to decide
    whether to bother putting the heating on in the morning) - 2
-   Optimise the schedule to maximise the length of time the boiler
    spends in condensing mode. - 2
-   The system should learn the thermal properties of the building (e.g.
    if the user wants to living room to be at 20℃ by 8pm and the
    external temperature is 5℃ then should the system start heating the
    room at 7:30pm or 7pm?) - 2
-   The system should have a (user-configurable) degree
    of "intelligence". For example, the system could attempt to learn
    when particular rooms are occupied and the target temperature of
    preference for each occupant. Occupancy information could come from
    a variety of sources including: smart phone GPS, smart electricity
    meter disaggregation (if the TV is on then someone is probably in
    the living room), security system movement detectors, on-line
    calendar etc.
-   the system must be resilient to communication failures (or a
    complete lack of internet connectivity; for example my gran doesn't
    have ADSL and I'd want my gran to be able to use the software.
    Wireless communication is error-prone and the system must adapt as
    gracefully as possible) - 1
-   So easy to use that your grandma could pick it up without needing
    a manual. Make it as easy as possible for the user. E.g. the user
    just tells the system “I’ll be in from x to y” and the system knows
    their temperature preferences (from learning when the individual
    complained rooms were too hot / too cold) and also knows their
    room-to-room movement patterns. e.g. the system knows I’m usually
    home at 8pm and that I spend an hour in the kitchen, an hour in the
    office, an hour in the livingroom and then go to bed.
-   ...but also makes it easy for 3rd party developers / hackers to add
    functionality - 1
-   Use as much off-the-shelf hardware as possible; allowing users to
    mix-and-match if technically possible - 1
-   Use as many open-standards as possible - 1
-   multi-user (most houses have more than one person living in them!
    each will have different preferences and schedules) - 3
-   Open source, hosted on GitHub (or similar), with high quality
    wikified documentation for both users and developers; including a
    one-page "quick-start" guide showing end-users where to get the kit,
    how to install themselves, how to setup. Use standard tech. E.g. use
    oAuth to authorise apps (if appropriate)
-   Interface:
    -   System hardware user interfaces in each room - 2
    -   Web interface (using Dynamic DNS) - must be secure
    -   iPhone, Android etc apps
    -   Allow the user to easily see how much energy they’re using and
        how much it’s costing them and break the data down into easily
        digested chunks (e.g. “with the external temp at 5C, it costs
        you 50p per night to heat your livingroom for 3 hours”). Perhaps
        use “game mechanics” / smiling/frowning faces to provide quite,
        gutteral feedback
    -   Google TV / Apple TV / Myth TV / XBMC etc apps
-   Hardware
    -   back end should be able to run on a tiny machine - possibly even
        an arduino?
    -   needs to be responsive
    -   needs to run in the absence on an internet connection
    -   needs to be able to talk to:
        -   boiler (with OpenTherm?)
        -   UFH pump and valves
        -   room thermostats
        -   zone valves / rad valves
        -   light switches
        -   electric heaters
        -   MVHR
        -   gas / electricity / water meters
-   Room occupancy:
    -   assign a probabilityOccupied value to each room
    -   The system must “miss” as infrequently as possible. People hate
        cold rooms. Perhaps, for room occupancy probabilities above a
        certain threashold (say 70%), translate the probability that a
        room will be occupied into a target temperature. E.g. if the
        user’s target temp is 18C, the current (unheated) temp is 15C
        and there’s a 75% chance that they’ll be in the room at a
        particular time then bring it up to 17C. (Caswell’s idea)
    -   probabilityOccupied can be informed by:
        -   at the most basic: a manually entered schedule
        -   user using smart phone / tablet / laptop to say “I’m here
            now”
        -   static computers (Desktops / HTPCs / laptops which live in
            one room) on the network could report to the heating control
            to say “I’m on and the user last interacted with me X
            minutes ago”; or the heating system could just ping the PCs
            (although there are lots of reasons why a PC might be on
            even though the user is elsewhere)
        -   Smart meters with
            [NILM](http://en.wikipedia.org/wiki/Nonintrusive_load_monitoring)
            could tell the heating control “the toaster has just come
            on” / “the upstairs TV has just come on” etc. The user could
            manually specify which device is in which room; or the
            system could correlate devices with other room
            occupancy data. But the system would have to be trained to
            know which appliances lived in which rooms and so it may be
            necessary to spend a week or two with a low power keyfob as
            Ken suggest
        -   Alarm sensors (PIR, window, door etc) (if present) or
            Arduino-based wireless motion sensors like
            [JeeLabs’](http://jeelabs.org/2010/10/15/room-node-redesign/)
        -   If we were to build our own TRV-head actuators then perhaps
            the actuators could have built-in ultrasonic movement
            detectors?
    -   One challenge is that none is the room occupancy data will be
        100% reliable so an algorithm would be required to sift through
        the live sensor data and also use prior experience to assign a
        probability that each room is (or will soon be) occupied.
        There’s lots of noisy room occupancy data; finding signal in the
        noise will be challenging
-   House occupancy:
    -   manually entered schedule
    -   pull in iCal / Google Calendar feeds (configurable: could assume
        that any empty entries or entries with “home” as the location
        mean you’ll be at home). Elegantly handle events marked as “TBC”
        in calendar.
    -   Track the geo location of occupants:
        -   It looks at how far you are away. If you’re &lt;100 miles
            then it calculates how long it’ll take to drive (perhaps
            using OSM / Google Maps) and/or learns from past
            experience e.g. “The fastest he’s ever gotten from South Ken
            to home is 45 minutes”.
        -   Foursquare / FaceBook places / Google Latitude
        -   Have an option in the smart phone app to send location
            whenever the app is used / automatically
        -   Have an option on the web interface to send location
-   allow functionality to post updates to twitter / facebook etc if the
    user wants / make it easy for users to compare with their friends
    (talk to Ed E about his ideas about socialising this)

### Existing kit

I did a bit of Googling this morning to see if anyone has successfully
hacked the FS20 wireless protocol used by the Conrad Wireless TRV
Actuators and Room Thermostats... and... much to my delight... it looks
like good old JeeLabs have made a good start on communicating with FS20
using their wireless module: <http://jeelabs.org/?s=FS20> I'm very
tempted to buy a Conrad Wireless TRV Actuator and Room Thermostat and
JeeLabs wireless module and make a start.

The idea I'm thinking of is something like this: use Conrad Wireless
TRVs, Room Thermostats and Boiler Control for basic heating control.
Then use a Nanode+JeeLabsWireless to add an open-source "Internet
gateway" to the FS20 system to allow for remote control and monitoring
of the heating system. One of the nice properties of this system is
that, when we move house (which may be in only a few year's time), I can
remove the DIY components from the system (i.e. the Nanode) and the core
FS20 system will continue to work.

