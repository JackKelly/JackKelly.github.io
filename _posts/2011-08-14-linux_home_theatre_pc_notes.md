---
title: "Linux Home Theatre PC notes"
date: 2011-08-14 21:10:00 +0000
categories: ["htpc", "xbmc", "mythtv", "video"]
permalink: /linux_home_theatre_pc_notes
---
We have had a HTPC as our main source of TV content since about 2006. 
We started with MediaPortal but I couldn't get that stable so we
switched to Vista Media Center which does actually work quite well but
I've always wanted to try to put Linux on our HTPC.  Below are my notes.

### Current status - 14 Sept 2011 {#current-status---14-sept-2011 dir="ltr"}

Cable worked but seems faulty. To get the system to boot with Dell 24”
monitor, remove the GRAPHICS line in 2nd grub menu. Myth 0.24.1,
XBMC-PVR and tvheadend are all installed. MythTV, for whatever reason,
feels buggy, slow performance. XBMC-PVR plus tvheadend looks like it
might work really well; but unfortunately time-shifting isn’t working
yet. There’s a feature request
[here](http://www.lonelycoder.com/redmine/issues/446); and also check
the [XBMC-PVR devs on
timeshifting](https://github.com/opdenkamp/xbmc/issues/search?q=timeshift)
(not sure if it will be implemented in XBMC or backend).  Let’s keep
checking and come back to this solution when timeshifting is working.
XMBR-PVR plus MythBackend might also be an option, but I can’t get that
to work yet, and would have much slower channel changes than tvheadend.

### Next steps {#next-steps dir="ltr"}

1.  Wait for timeshift to be implemented in XBMC-PVR / tvheadend
2.  Fix Radio Times XML grabber in tvheadend (see below)
3.  [ACPI switch off](http://www.mythtv.org/wiki/ACPI_Wakeup)
4.  Try XBMC-PVR + Tvheadend ([simple
    how-to](http://forum.xbmc.org/showthread.php?t=91716))
5.  [Fix overscan using
    modelines](http://www.mythtv.org/wiki/Working_with_Modelines#Getting_rid_of_overscan_and_centering_the_image)
6.  Try XBMC (see below).  But the priority for 2011 should probably be
    to get MythTV working well.  XBMC 11 (due end of 2011) should
    support MythTV a bit better (?)
7.  Check the logs when the system freezes

\
\

RadioTimes XMLTV grabber in tvheadend

Gave this error:

\

> Make sure that the grabber is properly configured before saving
> configuration.
>
>  
>
> To configure manually execute the following command in a shell on the
> server:
>
> \$ /usr/bin/tv\_grab\_uk\_rt --configure
>
>  
>
> Note: It is important to configure the grabber using the same userid
> as tvheadend since most grabbers save their configuration in the users
> home directory.
>
>  
>
> Grabber version: XMLTV module version 0.5.59 This is tv\_grab\_uk\_rt
> version 1.331, 2010/11/19 11:31:00

\

### Installing tvheadend {#installing-tvheadend dir="ltr"}

-   stopped mythbackend using “sudo stop mythtv-backend”
-   installed tvheadend as per [wiki
    instructions](http://wiki.xbmc.org/index.php?title=HOW-TO_watch_TV_in_XBMC_%28aka_XBMC-PVR%29#TVHeadend)
-   user: username “tv”; password “gad...”

### System Configuration {#system-configuration dir="ltr"}

-   Networking: use “nm-connection-editor”. Give the system a static
    IP address. Set this IP address in the Myth backend setup

\
\

### Myth backend Config {#myth-backend-config dir="ltr"}

-   Video Sources
    -   New Video source
    -   Call it “RadioTimes”
    -   Select Listings Grabber UK/IR RadioTimes (xmltv)
    -   Check “Perform EIT scan”
    -   Click “configure”
-   Input Connections
    -   Bind both DVB cards to RadioTimes
    -   Scan channels for just one card

\
\

### Myth Frontend Config {#myth-frontend-config dir="ltr"}

-   TV Settings
    -   Playback
        -   Action on playback exit: Save position and exit

\
\

HD freeview\
I think I need a card capable of DVB-T2 to receive HD. Crystal palace
does broadcast HD on [DVB-T2](http://www.freeview.co.uk/freeview/HD).

\

### Researching alternatives {#researching-alternatives dir="ltr"}

#### [Boxee](http://www.boxee.tv/) {#boxee dir="ltr"}

-   XBMC plus “social media” proprietry add-ons.
-   Apparently the iPlayer module doesn’t work ATM
-   No native PVR functionality.  Can be made to work with MythTV,
    although not sure which version?
-   Not sure I see the point.  XBMC has some social media functionality
    (see below)

\
\

#### XBMC {#xbmc dir="ltr"}

XBMC does not have native PVR functionality.  Dharma 10.1 supports
MythTV 0.23 NOT 0.24 (althought there appears to be a patch ). The XBMC
“[unified PVR](https://github.com/dteirney/xbmc)” thing is due for
proper release until XBMC 12 (due end of 2012). Maybe, just maybe,
getting 10.1 to work with MythTV 0.24 will be as simple as swapping out
the libcmyth file for [the one in
trunk](https://github.com/tsp/xbmc/blob/e99e5552805e45a8d4271ca13a3fd3291f4a5cf9/xbmc/pvrclients/mythtv-cmyth/libcmyth.h).
 [Although some people do report that MythTV 0.24 + XBMC “unified PVR”
functionality in trunk
works](http://forum.xbmc.org/showthread.php?t=102757).

-   [Social recommendation using](http://trakt.tv/downloads/xbmc)
    [trakt.tv](http://trakt.tv/)
-   [iPlayerv2](http://code.google.com/p/xbmc-iplayerv2/)
-   <http://trac.xbmc.org/roadmap>
-   [Aeon MQ2](http://forum.xbmc.org/forumdisplay.php?f=68)Skin looks
    gorgeous
-   Wake-up links: [Enable Wake on
    Device](http://wiki.xbmc.org/?title=Enable_Wake-On-Device), [How to
    install XMBC on Ubuntu, Power Management
    section](http://wiki.xbmc.org/index.php?title=HOW-TO_install_XBMC_for_Linux_on_Ubuntu_with_a_minimal_installation,_an_unofficial_Step-by-Step_Guide#Power_Management),
    [Mythbuntu frontend build - XBMC, MythTV, suspend/resume with
    remote](http://www.pcmediacenter.com.au/forum/topic/39679-mythbuntu-frontend-build-xbmc-mythtv-suspendresume-with-remote/)

\
\
\

### Teaching XBMC to play DVB\
[XBMC Wiki: HOW-TO watch TV in XBMC (aka XBMC-PV)](http://wiki.xbmc.org/index.php?title=HOW-TO_watch_TV_in_XBMC_%28aka_XBMC-PVR%29#Backends)

\

#### Using Myth backend {#using-myth-backend dir="ltr"}

2 options: [MythBox](http://code.google.com/p/mythbox/)script (no live
TV under 0.24 ATM) and XBMC’s Unified PVR frontend (under active
development but is the future of PVR in XBMC):

-   [XBMC Wiki: MythTV how-to](http://wiki.xbmc.org/?title=MythTV)
-   [XBMC PVR Development
    forum](http://forum.xbmc.org/forumdisplay.php?f=136)
-   On 29th May, 2 Myth TV patches
    ([1](https://github.com/xbmc/xbmc/commit/3287e381bf02461b6d571d6250fb68f7bfa713b3),
    [2](https://github.com/xbmc/xbmc/commit/b2738b7785c4f045896342f217eafe2610c51d9f))
    were pushed to the [main git repo of
    XBMC](https://github.com/xbmc/xbmc).  I should try this before
    trying the repos from the PVR devs.
-   Best web backend of the 3, apparently
-   slowest channel change of the 3
-   most features and the most mature (although also very complex
    to setup).  Best scheduling features

\
\

#### tvheadend {#tvheadend dir="ltr"}

<https://www.lonelycoder.com/redmine/projects/tvheadend/wiki/Faq>\
<https://www.lonelycoder.com/hts/tvheadend_overview.html>\
<https://github.com/andoma/tvheadend>

-   pros: simple to install, rapid dev, web interface, stable support on
    XBMC, rapid channel changes, [standby using similar techniques to
    MythTV](http://www.lonelycoder.com/redmine/projects/tvheadend/wiki/Wakeup)
-   cons: (channel skipping may now be possible) no built-in commercial
    skipping (although [might be able to do this using a rather clunky
    hack to use MythTV’s commercial
    skipping](http://www.lonelycoder.com/redmine/projects/tvheadend/wiki/Tvheadend_post_recording_scripts)),
-   mutliple recording from a single multiplex (although [MythTV can now
    do this - called
    multirec](http://www.mythtv.org/wiki/Record_multiple_channels_from_one_multiplex))

\
\

#### The Video Disk Recorder {#the-video-disk-recorder dir="ltr"}

http://www.tvdr.de/features.htm

-   Stable, apparently
-   No built-in commercial skipping
-   Lots of the documentation is in German, apparently

\
\

### May 2011 attempt {#may-2011-attempt dir="ltr"}

#### Thoughts on how to install from fresh: {#thoughts-on-how-to-install-from-fresh dir="ltr"}

1.  Install MythBuntu 11.04 (using a VGA monitor)
2.  Install Kernel 2.6.37 (download from Kernel.org and then
    follow[these
    instructions](https://wiki.ubuntu.com/KernelTeam/GitKernelBuild),
    make sure lirc\_mceusb AKA ir\_mceusb and lirc\_dev are enabled
    as modules)
3.  Install [latest Radeon X11 open source
    driver](http://wiki.x.org/wiki/radeonBuildHowTo) and to the xrandr
    stuff mentioned below
4.  Install the Cinergy Card as discussed below
5.  [Configure MythTV](http://www.mythtv.org/docs)
    1.  I can’t get RadioTimes to work so I’ve gone with Over The Air,
        although OTA only seems to provide 1 week in advance and little
        info about repeats etc.  Beeb XML might work.

\

### Getting X to start after upgrading to 11.04 {#getting-x-to-start-after-upgrading-to-11.04 dir="ltr"}

X wouldn’t start (the system booted straight to the terminal login and
gave lots of errors about EDID).  I fixed this by installing the [latest
Radeon X11 open source driver](http://wiki.x.org/wiki/radeonBuildHowTo).
 

\
\

#### Making the cable {#making-the-cable dir="ltr"}

I built a cable as per
[jwexqm](http://idiots.org.uk/vga_rgb_scart/index.html), including the
simple transistor circuit to composite vsync and hsync into a single
composite sync([source
1](http://www.mythtv.org/wiki/RGB_Scart#Nvidia_Cable), [source
2](http://www.nexusuk.org/projects/vga2scart/circuit)), and a 3v battery
on pins 16 and 18 of the SCART.  (I originally thought my ATI R390 could
do composite sync on its own but then I noticed a message in dmesg
saying “composite sync not supported”)  I used thick 75 ohm cable and
this was a right PITA.  Apparently shielded CAT5 works very well and is
far easier to solder.  \
\
A [more detailed cable construction guide is
available](http://translate.google.com/translate?prev=hp&hl=en&u=http%3A%2F%2Fdigilander.libero.it%2Fventuri1975%2F&sl=it&tl=en),
and [a Linux program for calculating
modelines](http://sourceforge.net/projects/lrmc/) are available but I
didn’t really need either.

\
\

#### xrandr {#xrandr dir="ltr"}

To do xrandr over ssh:

\
\

xrandr -d :0.0 --newmode "768x576pali" 14.76 768 789 858 944 576 580 583
625 -hsync -vsync interlace

\

xrandr -d :0.0 --addmode VGA-0 768x576pali

\

xrandr -d :0.0 --output VGA-0 --mode 768x576pali

\

To make these changes persistent, edit /etc/gdm/Init/Default and put the
above 3 lines before /sbin/initctl -q emit login-session-start
DISPLAY\_MANAGER=gdm

\
\

Cinergy Card {#cinergy-card dir="ltr"}
------------

The driver appears to NOT work with 2.6.38 because that’s when V4L1 was
completely removed in favour of V4L2 which I’m guessing the ngene driver
does not support (there has been some discussion of this on the German
forum so there’s a chance someone will get round to fixing the driver).
 Ubuntu 11.04 comes with 2.6.38 so it’s necessary to either install a
previous version of Ubuntu or downgrade the kernel.\
\
Once Kernel 2.6.37 is installed, I think all that is necessary is to
download the
[ngene.tar.gz](http://media.cdn.ubuntu-de.org/forum/attachments/2770455/ngene.tar.gz)file
(from [page 4 of the
forum](http://translate.google.com/translate?hl=en&ie=UTF8&prev=_t&rurl=translate.google.com&sl=de&tl=en&twu=1&u=http://forum.ubuntuusers.de/topic/terratec-cinergy-2400i-laeuft-unter-ubuntu/))
and untar, and then:

-   make
-   sudo make install
-   sudo depmod -a
-   sudo modprobe ngene

\
\

Then do lspci -vvvnn to see if the module has loaded

\
\

Installing a new kernel {#installing-a-new-kernel dir="ltr"}
-----------------------

Install Kernel 2.6.37 (download from Kernel.org and then follow[these
instructions](https://wiki.ubuntu.com/KernelTeam/GitKernelBuild), make
sure lirc\_mceusb AKA ir\_mceusb and lirc\_dev are enabled as modules).
 Make sure you read the section titled “Using Ubuntu Kernel Config”
first. I didn’t do this so it’s not essential but probably is a good
idea.\
\
Use the program startupmanager to configure grub.\
\
There is a
[ppa:kernel-ppa/ppa](http://www.ubuntuupdates.org/ppa/kernel-ppa?dist=natty)
but I think that only provides the latest kernels for your distribution
rather than previous kernels.

\

#### Required Kernel modules {#required-kernel-modules dir="ltr"}

lirc\_dev\
lirc\_mceusb AKA ir\_mceusb (search for mceusb)   ←- my 2.6.37 is
missing this module!

\
\

IR {#ir dir="ltr"}
--

Remote is Windows Media Center Transeiver\
MythTV uses [LIRC](http://www.lirc.org/html/table.html) (Linux Infrared
Remote Control) which requires irc\_mceusb AKA ir\_mceusb and lirc\_dev
 kernel modules.  LIRC should be installed automatically.  There is some
mention of LIRC in MythTV Front End’s log and Xorg.0.log.  [Here’s how
to test the IR system](http://www.lirc.org/html/install.html#testing).

\

DisplaySize {#displaysize dir="ltr"}
-----------

Trying to get MythTV to understand that our TV is 16:9.  As per
[this](http://www.mythtv.org/wiki/Display_Size), I first did the
following:

\
\

jack@jack-htpc:\~\$ cat /usr/share/X11/xorg.conf.d/05-monitor.conf

Section "Monitor"

    Identifier  "&lt;default monitor&gt;"

\# For 1280x720 at 100dpi  (16:9)

    DisplaySize  325 182 \# in millimeters

EndSection

\

Xorg swallows this (according to the logs) but it makes no difference.
 So I found that in the Appearance tab of Myth Front End, it’s possible
to ask it to use separate modes for GUI and Video and here you can set
it to 16:9.

\
\

Loading Videos {#loading-videos dir="ltr"}
--------------

<http://www.mythtv.org/wiki/MythVideo#Setting_up_Video_and_Image_Folders>

\
\

Things to record {#things-to-record dir="ltr"}
----------------

-   Inside the Human Body
-   Grand Designs
-   Family Guy
-   Misbehaving Mums
-   The Apprentice
-   The Apprentice You’re Fired
-   Brother and Sisters
-   Ugly Betty
-   Outnumbered
-   The Graham Norton Show
-   Doctor Who
-   The Sky At Night
-    

\

old notes... {#old-notes... dir="ltr"}
============

\

Things to try:

-   Build a prototype, [see here for
    modelines](http://www.nexusuk.org/projects/vga2scart/)
-   a DVI-I to RGB component cable
    ([TVCables,](http://www.tvcables.co.uk/cgi-bin/tvcables/dvi-to-component-video-adapter.html)
    open again on 4th Jan) or
    [this](http://www.kenable.co.uk/product_info.php?products_id=3202)
    (also open 4th Jan); the MythTV wiki page says my card should work
    with Radeon drivers:
-   get the legacy driver to install (use an old version of Ubuntu
    if necessary) but this probably wont support standby very well?
-   [buy a card which
    works](http://www.mythtvtalk.com/best-pci-express-video-card-component-output-6980/)!

\
\

TV-out not working is a known bug:
<https://bugs.freedesktop.org/show_bug.cgi?id=21948>\
\
I’ve also started a thread on ubuntu’s forum:
<http://ubuntuforums.org/showthread.php?p=10258386#post10258386>\
\
I’ve tried installing [the latest
kernel](https://wiki.ubuntu.com/Kernel/MainlineBuilds?action=show&redirect=KernelTeam%2FMainlineBuilds)
but that didn’t help

\
\

### Notes {#notes dir="ltr"}

If I go the nVidia route: http://www.x.org/wiki/NVIDIAProprietaryDriver\
\
wouldn’t boot so added clocksource=jiffies to boot
([source](http://ubuntuforums.org/showthread.php?t=1040026#4))\
\
UK is PAL-I\
\
Remote is Windows Media Center Transeiver\
\
it may be necessary to [chroot into the newly installed system to add
clocksource=jiffies to grub2’s startup
config](https://help.ubuntu.com/community/Grub2)\
\
ssh into the machine and do:\
sudo apt-get update\
sudo apt-get upgrade\
\
Start the machine without a VGA monitor installed!\
\
ATI Video drivers

-   OpenGL works with Open source drivers, doesn’t seem to work with
    either 10.2 or 9.3 closed source
-   I don’t think component works at all with open source drivers (it
    does work ok with closed-source, although it stutters on playback)

\
\

#### Proprietary drivers\
Installing AMD closed-source drivers, Component out, HD576i\
\
Install the AMD/ATI[drivers 9.3](http://support.amd.com/us/gpudownload/linux/Legacy/Pages/radeon_linux.aspx?type=2.7&product=2.7.2.3.2&lang=English) (the x1250 is a legacy product and so isn’t supported on the latest drivers) and then follow the instructions on: [Unofficial ATI Ubuntu wiki](http://wiki.cchtml.com/index.php/Ubuntu_Maverick_Installation_Guide)(may need to uninstall first as [shown here](https://wiki.ubuntu.com/X/Troubleshooting/FglrxInteferesWithRadeonDriver#Problem:%20%20Need%20to%20fully%20remove%20-fglrx%20and%20reinstall%20-ati%20from%20scratch)) (install with --buildpkg Ubuntu/9.04\
\
May have to do a sudo apt-get -f install to sort out dependencies from old ATI driver\
\
Also have to comment out “driver “fglrx”” in /etc/X11/xorg.conf\
\
ATI open source drivers\
(the [open source drivers](https://help.ubuntu.com/community/RadeonDriver)\
\
Can’t yet get it to work.  Things to try:

-   find exact timings windows uses and add them to linux using xrandr
-   using KMS does work with xrandr, just need to use these commands:
    -   \$ xrandr --output S-video --set "tv standard" pal
    -   \$ xrandr --output S-video --same-as DVI-0
    -   \$ xrandr --addmode S-video 800x600
    -   \$ xrandr --output S-video --mode 800x600
-   Useful commands:
    -   xrandr -q --verbose
    -   xrandr --props
    -   lspci -vvv
    -   cat /var/log/Xorg.0.log
    -   sudo emacs /etc/default/grub
        -   sudo update-grub

\

-   try disabling KMS - [this may be required to get tv\_standard pal to
    work](http://www.phoronix.com/forums/showthread.php?t=25192&page=3)
-   [Option "ATOMTvOut" "TRUE"](http://wiki.x.org/wiki/radeonTV)
-   try xrandr --prop for more info
-   tinker further with [Kernel Mode
    Settings](https://wiki.archlinux.org/index.php/ATI#Force_TV-out_in_KMS),
    and [see here](http://wiki.x.org/wiki/radeonTV) ,
-   tinker further with xorg.conf,
    [eg](https://bbs.archlinux.org/viewtopic.php?id=98795#7) & [see
    examples
    here](http://www.phoronix.com/forums/showthread.php?t=9680), and
    [here](http://www.phoronix.com/forums/showthread.php?t=9680) and
    [here](http://ubuntuforums.org/showthread.php?t=803937)
-   Maybe [try the latests stable ATI
    drivers](http://wiki.x.org/wiki/radeon)and maybe the very latest
    unstable drivers too
-   try [installing latest
    xrandr](http://www.x.org/wiki/Projects/XRandR)

\
\

To stop X:\
CTRL-ALT-F1\
sudo /etc/init.d/gdm stop

\
\

#### Cinergy TV card {#cinergy-tv-card dir="ltr"}

\

[This
driver](http://translate.googleusercontent.com/translate_c?hl=en&ie=UTF-8&sl=de&tl=en&u=http://forum.ubuntuusers.de/topic/terratec-cinergy-2400i-laeuft-unter-ubuntu/&prev=_t&rurl=translate.google.com&twu=1&usg=ALkJrhijaPidIgbyGEt5dVNAK9mSME4HQQ)
for the Cinergy card seems to work\
\
install firmware 1.5 for TV tuner card as per
<http://www.linuxtv.org/wiki/index.php/Media-Pointer_MP-S2%C2%B2#Firmware>

\

-   install V4B-DVB as per
    <http://linuxtv.org/wiki/index.php/How_to_Obtain,_Build_and_Install_V4L-DVB_Device_Drivers>
-   sudo apt-get install linux-source patchutils git libncurses5-dev
-   to get the media tree: git clone git://linuxtv.org/media\_tree.git
-   then, in media\_build/ do make tar DIR=../../media\_tree
-   if this fails, edit media\_build/Makefile and comment out the
    offending file(s)
-   edit v4l/KConfig and add two spaces after the tab on line
    1512 (Add...)
-   edit v4l/.config and set to N any buggy modules

\
\

things to try:

-   Look in the Kernel - is CONFIG\_DVB\_NGENE=m ?  (see
    [here](http://www.linuxtv.org/wiki/index.php/Mystique_SaTiX-S2_Dual))
-   [Investigate](http://www.linuxtv.org/wiki/index.php/NGene_devices)
    “It has been confirmed that the Original driver
    ([\[2\]](http://www.media-pointer.de/WebRoot/Store21/Shops/62290022/4AB0/D7EA/2E65/766B/4B4E/C0A8/28BE/FE04/ngene.tgz))
    does work also for TerraTec Cinergy 2400i DVB-T (confirmed on
    OpenSuse 11.2 64b after few minor corrections due to API changes in
    kernel 2.6.31). Based on the README in the package it should support
    these cards: “
-   Try a new Kernel?


