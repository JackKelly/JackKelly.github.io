---
title: "Re-installing Windows Vista x64 Media Center"
date: 2011-11-21 09:18:47 +0000
categories: ["htpc"]
permalink: /reinstalling_windows_vista_x64_media_center
---
**update 13/11/2014** We got the dreaded "component registration
failure" message again. [stream-recorder.com has a few good ideas on how
to fix this
issue](http://stream-recorder.com/forum/repair-windows-media-center-files-windows-vista-t4568.html?s=8d6691354121e176b875988444833a5e&).
The fix that worked for me was to delete `recordings.xml`. No need to
re-install Vista. Phew! The old post is below.

------------------------------------------------------------------------

Just as we were settling down to watch TV on Sunday night, our HTPC
(which runs Vista Media Center) decided to stop working. After
installing some updates, Media Center gave a “component registration
failure” error whenever we tried to watch either live or recorded TV.
After several attempts at fixing it, I decided to re-install Windows
Vista (this was something I’d been planning to do for a while because
Vista had swallowed up almost all of the system drive on which it was
installed). Here are some notes on installing Vista on my HTPC. Our
hardware includes:

-   TerraTec Cinergy 2400i DT dual DVB-T tuner card
-   [Biostar TA690G AM2
    motherboard](http://206.108.48.60/app/en/mb/introduction.php?S_ID=17&tab=2)
    with AMD 690G chipset, PCI-E, Realtek RTL8111B ethernet, ATI Radeon
    X1250 integrated graphics with composite (YPbPr) video output and
    Realtek ALC888 audio (with digital S/PDIF output)
-   PAL Panasonic CRT TV connected to HTPC via YPbPr component
    (interlaced not progressive)

Here’s what worked:

-   I wouldn’t bother saving anything from the previous install; except
    perhaps making a note of which TV programs you want to automatically
    record (I had saved everything from
    `C:\ProgramData\Microsoft\eHome\` (about 600 MBytes) but I didn’t
    need any of this data. All of our TV recordings are on a separate
    partition and I just told MCE to add that folder to its “Recorded TV
    folder watch list”. We manually re-entered all the programs we want
    to record.)
-   Do a clean re-install from the Vista DVD. Tell automatic updates to
    not install anything.
-   [Disable password at
    startup](http://superuser.com/questions/405933/can-i-set-my-windows-to-boot-without-stop-on-password-verification-even-when-hav)
-   Install SP1 (download from MS, not using windows update). If it
    doesn't work then try copying the file to Desktop (not a directory
    within Desktop) (I know, I know... sounds crazy but seems to work).
    If you're using a saved version of SP1 then try downloading it again
    from MS to your Desktop. If it still doesn't work then try to ideas
    listed by [Magon Liu on
    technet](http://social.technet.microsoft.com/Forums/uk/itprovistasp/thread/4120f8ff-ae6c-437f-a40d-8d48794d9841).
-   Install [Vista Media Centre TV
    Pack](http://trumphurst.blogspot.co.uk/2013/01/windows-vista-media-centre-program.html).
    This procedure worked for me (I actually installed this on top of
    SP2 and the 2010 WMC update but that's not best practice. Probably
    better to install the TV pack after installing SP1):
    -   Install
        [MediaCentreTVPack2008](http://digiex.net/guides-reviews/guides-tutorials/media-guides/699-windows-media-center-tv-pack-2008-download-installation-guide.html)
    -   Install PlayReadyPC
    -   Reboot
    -   Install [MCETVPack-Windows6.0 update 956147 for TV
        Pack](http://support.microsoft.com/kb/956147)
    -   Reboot
-   Install SP2 using a similar procedure as SP1.
-   Let automatic updates download all available updates. Then install
    these updates by shutting down. Repeat until all updates have
    been installed.
-   Install [the
    hack](http://andrewblock.net/2009/06/08/how-to-enable-remote-desktop-on-windows-vista-home-premium/)
    to enable remote desktop on Vista Home Premium. (Note to self: I
    need the Non-Americal English version)
-   For the ATI Radeon, ethernet and audio, I just let Automatic Update
    install the relevant drives from the “recommended updates”. ([In the
    past I spent a while tinkering with various ATI
    drivers](http://xlk.org.uk/wiki/index.php?title=Configuring_ATI_x1200_to_output_SD_component_TV_without_annoying_deinterlacing)
    to get the best signal on our YPbPr component output. It turns out I
    needn’t have bothered: the driver installed by Automatic Update
    appears to work fine for YPbPr).
-   For the TerratTec Cinergy 2400i tuner, I installed [driver
    1.1.0.284](http://www.terratec.net/en/driver-and-support/driver_21269.html?selectproduct=Cinergy%202400i%20DT)
-   Setup the “sleep settings” so that the machine goes to sleep after,
    say, 20 minutes (it wont sleep while you’re watching TV but it will
    sleep if you leave it idle for 20 minutes… good for saving power).
-   Setup WMC TV channels. I had to edit several channels to get access
    to the full 14-day listings for those channels (edit listings)
-   Install Avast Free Antivirus


