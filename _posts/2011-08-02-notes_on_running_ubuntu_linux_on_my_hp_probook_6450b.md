---
title: "Notes on running Ubuntu Linux on my HP ProBook 6450b"
date: 2011-08-02 14:13:00 +0000
categories: ["linux", "laptop"]
permalink: /notes_on_running_ubuntu_linux_on_my_hp_probook_6450b
---
### WiFi

To get the wifi to work correctly, I had to do <span
class="geshifilter">`sudo apt-get remove --purge bcmwl-kernel-source`{.text
.geshifilter-text}</span> 
[source](https://bugs.launchpad.net/ubuntu/+source/bcmwl/+bug/1112751/comments/23)

### Network driver problems when installing 11.04

The system wouldn’t boot.  I got it to boot by disabling wifi in the
bios.  I think all I had to do was to re-install <span
class="geshifilter">`bcmwl-kernel-source`{.text
.geshifilter-text}</span> twice (and reboot twice).  Network Manager
then complained that the wifi was disabled by hardware switch so I
turned off “WiFi switch state” in bios (but leave “LAN/WiFi switch”
enabled in bios)\
\
Network controller: Broadcom Corporation BCM4313 802.11b/g/n Wireless
LAN Controller (rev 01)\
\
https://help.ubuntu.com/community/WifiDocs/Driver/bcm43xx\
\
Note that my card is covered by the STA drivers, NOT the b43 drivers.

### reset monitor preferences

<span class="geshifilter">`rm ~/.config/monitors.xml`{.bash
.geshifilter-bash}</span>

### Reset gnome panel

<div class="geshifilter">

``` {.bash .geshifilter-bash style="font-family:monospace;"}
~/$ gconftool --recursive-unset /apps/panel
~/$ rm -rf ~/.gconf/apps/panel
~/$ pkill gnome-panel
```

</div>

### \
Fixing vertical scroll bars in Eclipse

<span
class="geshifilter">`sudo apt-get remove overlay-scrollbar liboverlay-scrollbar-0.1-0`{.bash
.geshifilter-bash}</span>

