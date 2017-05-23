---
title: "New year HTPC woes"
date: 2013-01-01 20:48:03 +0000
categories: ["htpc"]
permalink: /new_year_htpc_woes
---
(Happy new year!)

We have a home theatre PC dating back to about 2006 running Windows
Vista and Windows Media Centre with a FreeView DTB card. It was working
perfectly. But, for some reason, [Microsoft have stopped providing
electronic program guide (EPG) data from 1st Jan
2013](http://www.thegreenbutton.tv/forums/viewtopic.php?f=5&p=38483). So
we can't see the programme guide (hence we can't schedule recordings,
which is one of the main functions of our HTPC). It's not clear if MS
have decided to kill off the service deliberately (they seem to have
gone off WMC) or if it's just a bug.

UPDATE 3/1/2013: MS have just fixed their EPG data. It's working again!

Here are some notes for alternatives I've tried:

<!--break-->

-   [EPG Collector](http://sourceforge.net/projects/epgcollector/) can
    extract EPG data from the DBV over-air streams and process it ready
    for Windows Vista WMC. But to install this I need .NET 4, which in
    turn requires 2.5GB of HDD space free. The Windows partition has
    less than 1GB free because Windows Vista, in its infinite wisdom,
    has put over 25GB of [crap in
    winsxs](http://www.winvistaclub.com/f16.html).
-   I tried XBMC 12 RC2 in Windows. It looks good. It plays DVDs fine
    but video stutters when playing MPEG files recorded by WMC (even
    though VLC and WMC play these files fine). The standard response on
    the forums seems to be "install the latests GFX card drivers" but I
    can't to that because my old on-board ATI R390 graphics card is
    considered "legacy" by AMD. Also, it looks like the best PVR backend
    is tvheadend, but that only runs on Linux.
-   I tried booting XBMCbuntu 12 RC2 but it wouldn't even boot.

Possible short-term plan:
=========================

The plan I went for:
--------------------

Turns out Win 7 is still quite expensive. So I "just" re-installed Vista
along with TV Pack (which enables MHEG for over-the-air 7-day listings),
using (and updating) [my old notes as a
guide](/reinstalling_windows_vista_x64_media_center). (Installing Vista
SP1 turned out to be a right PITA but I got there in the end)

Old short-term plan:
--------------------

Buy and install Windows 7 Home Premium. I have to re-install Windows
Vista or 7 (because of the winsxs issue) so I might as well go for Win7.
And there are some hints that Win 7 WMC can decode at least the EIT
over-the-air EPG (7 days) and possibly also the MHEG EPG. If not then I
can use EPG Collector. My [Cinergy 2400i
DT](http://www.terratec.net/en/driver-and-support/driver_21269.html?selectproduct=Cinergy%202400i%20DT)
is supported under Win 7 SP1 and Windows 8. The ATI Radeon X1250 Series
[driver](http://support.amd.com/us/gpudownload/windows/Legacy/Pages/radeonaiw_vista32.aspx)
says "AMD’s DirectX 9 ATI Radeon graphics accelerators are not
officially supported under Windows 7. If the user chooses to, they can
install the ATI Catalyst Windows Vista graphics driver under Windows 7.
Please be aware that none of the new Windows 7 graphics driver (WDDM
1.1) features are supported (as the Windows Vista level graphics driver
is limited to WDDM 1.0 level support). Using the ATI Catalyst Windows
Vista driver under Windows 7 is not officially supported by AMD, and as
such AMD will not provide any form of customer support for users running
in this configuration"

[](){#long_term_plan}

Longer-term plans (aiming to minimise power consumption whilst getting a modern media center)
=============================================================================================

Current favourite:
------------------

-   Wait until early 2014 before upgrading.
-   Build a Linux Atom PC to be placed in the living room and run
    several duties including data logging, PVR backend and
    XBMC front-end. Should be HD-capable. BUT! Current Atoms (Cedar
    Trail 32nm) use [PowerVR-based
    graphics](http://en.wikipedia.org/wiki/Intel_GMA#PowerVR_based)
    which have very poor Linux support. Some older Atoms have good Linux
    GMA support but [don't have enough power to run PVR backend and
    frontend
    together](http://www.gossamer-threads.com/lists/mythtv/users/478424#478424).
    So my plan is to wait for the [next gen of
    Atoms](http://hexus.net/tech/news/cpu/44385-intel-atom-soc-roadmap-leaked-details-bay-trail-valleyview/)
    (22nm, Bay Trail Atom with 1-4 Silvermont cores running on the
    Valleyview platform) will use "4 Intel Ivy Bridge Gen 7 Graphics
    Engines" similar to HD4000 and HD25000 GPUs but cut down. Decode for
    H.264, MPEG1/2/4, VC1/WMV9. Target for release in 2013Q4. 1080p
    HD 60fps.
-   Either make a cable to run the VGA from the Atom platform to our CRT
    TV over RGB SCART (as [Dave Cunningham has done for his Atom
    330](http://www.gossamer-threads.com/lists/mythtv/users/478208#478208)
    for ) or, if that doesn't work, consider buying a new TV. LED LCD
    sets should have lower power consumption than our existing CRT
    TV (\~100W). OLED TVs might be available cheap enough (but some
    people claim that OLED TVs won't be cheap enough or good enough
    quality for many years yet).
    [Apparently](http://www.guardian.co.uk/environment/2011/jul/29/flat-screen-tv-electricity)
    "A new 32-inch LED TV uses about 75% less energy than a 32-inch
    cathode ray tube". I suspect that's comparing the most power-hungry
    CRT against the most energy-efficient LED LCD TV (and I suspect our
    34" Panasonic CRT is pretty energy efficient for a CRT, drawing
    about 100W on average... here's a [32" Samsung Series 5 ES5500 32"
    Full HD Smart LED TV which uses
    39W](http://www.cclonline.com/product/90385/UE32ES5500KXXU/Televisions/Samsung-Series-5-ES5500-32-inch-Full-HD-Smart-LED-Television/PLA0340/)).

Old plans:
----------

-   For my smart meter research, I will have a headless Atom PC running
    all day long collecting smart meter data. Instead of wasting power
    running a second HTPC to record TV, I should use this data logging
    PC as the PVR backend, possibly using tvheadend. The only problem is
    that I'll have to get an aerial to it and CAT5. I could put it
    behind the TV and run the CT connection from the fuse box to the
    living room. Or put it in the cupboard under the stairs and cut into
    the aerial connection running to the living room. Or maybe just use
    the living room HTPC as both the PVR backend and frontend,
    especially if I upgrade to low-power Atom platform (but beware: the
    D2700MUD motherboard appears to have little Linux support for the
    on-board GFX).
-   Use XBMC on Linux on the main HTPC using a modern graphics card.
    Need either out-of-the-box Component support or a VGA/DVI-A to RGB
    component (but must check that both the GFX hardware and the Linux
    driver can support PAL RGB component). Or, perhaps even better, just
    use a single Atom-based machine running in the living room as my
    data logger, PVR backend and XMBC front-end. Just need to run cables
    from the CT clamps and "pro" smart meter to the livingroom.


