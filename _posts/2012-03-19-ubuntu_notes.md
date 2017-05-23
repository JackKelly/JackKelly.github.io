---
title: "Ubuntu notes"
date: 2012-03-19 09:19:52 +0000
categories: ["Ubuntu", "linux"]
permalink: /ubuntu_notes
---
Just some notes on useful Ubuntu tweaks

### Settings

-   Enable right ALT key (useful for Emacs): To set just for the current
    session: `setxkbmap -option altwin:meta_alt` (inspired from a
    [thread on AskUbuntu](http://askubuntu.com/a/29734)). To make
    permanent: run `dconf-editor`, find (CTRL-F) `xkb-options` and set
    it to `['altwin:meta_alt']` and hit enter. From [this SO
    comment](http://askubuntu.com/questions/451945/permanently-set-keyboard-layout-options-with-setxkbmap-in-gnome-unity#comment765161_451945).
-   PDF highlighting: first, `sudo apt-get install qpdfview`. Then
    `sudo emacs /etc/gnome/defaults.list` and change
    `application/pdf=evince.desktop` to
    `application/pdf=qpdfview.desktop`
-   [Put a window from one monitor to another using keyboard
    shortcut](http://askubuntu.com/questions/152304/send-or-move-a-window-from-one-monitor-to-another-with-a-shortcut-key-under-ubun).
-   [.emacs](http://www.doc.ic.ac.uk/~wjk/UnixIntro/.emacs)
-   [Remove Amazon
    ads](http://lifehacker.com/5953180/how-to-remove-amazon-ads-from-ubuntu-1210)
    by typing `sudo apt-get remove unity-lens-shopping`
-   Get "normal" menus back in Unity (see [this forum
    post](http://askubuntu.com/questions/10481/how-do-i-disable-the-global-application-menu#133005))
-   [Get ctrl-alt-numpad function back for positioning windows in
    12.04](http://askubuntu.com/questions/116744/restore-the-ctrl-alt-num-pad-windows-positioning-commands)
-   [Using Emacs keybindings across the entire
    system](http://askubuntu.com/a/181671)
-   [Nautilus open terminal](http://askubuntu.com/a/207448)
-   To add a folder to "Places" (kind of) open the folder in Nautilus
    and hit CTRL+D to bookmark it

#### Gnome 3

-   Set workspaces to use both monitors - install `gnome-tweak-tool`
    and, under "Workspaces", change "Workspaces only on primary display"
    ([source](https://askubuntu.com/a/558723)).

### Packages

-   General stuff:
    `sudo apt-get install git emacs24 autocutsel openjdk-7-jre openssh-server texlive-latex-base texlive-latex-recommended pandoc nautilus-open-terminal`
-   Python:
    `sudo apt-get install python-scipy python-matplotlib python-numpy python-pandas python-pip ipython ipython-notebook pyflakes`
-   Stuff which is rather out of date in the Ubuntu repos:
    -   `sudo pip install cython`
    -   `sudo pip install -update pandas` (or, if you want the dev
        version, do
        `pip install -e git+git://github.com/pydata/pandas.git#egg=pandas`)
-   I used to use pip to install stuff but you have to install lots of
    build dependencies which takes up hundreds of megabytes of space,
    plus pip doesn't automatically keep your system up to date,
    unlike aptitude. Here's what I used to do:

    -   `sudo pip install numpy`
    -   `sudo apt-get install libpng-dev libjpeg8-dev libfreetype6-dev python-gtk2-dev`
        (required for pip install of matplotlib); or do
        `sudo apt-get build-dep matplotlib`
    -   `sudo pip install matplotlib`
    -   `sudo pip install pandas`
-   [Ubuntu restricted
    extras](https://help.ubuntu.com/community/RestrictedFormats)
    (enables playback of Coarsera videos in Chromium)

### Files and directories to back up before doing a re-install

-   /data/
-   /home/jack/  (make sure to copy all the hidden files like .bashrc)

### Directory shortcuts

Use case: from the command line, you want a quick and easy way to jump
to frequently used directories.

Method one: use the `source` operator.  For example, I want a shortcut
to `~/Documents/imperial/PhD`. So I create a file called `p` which just
contains the text `cd '~/Documents/imperial/PhD'`.  On `bash` I type
`. p` to execute the code in the file (if I used a bash script then the
change directory would only affect the script and would not be
persistent when the script terminates).  `csh` doesn't have a "`.`"
operator.  Instead you have to type "`source p`".  Or alias `.` to
`source` by adding the line`alias . 'source'` to `~/.cshrc`

Method two: just add an alias to change directory.  e.g.
add `alias p 'cd ~/Documents/imperial/PhD ` to `~/.cshrc`

### Network Time Protocol client

To set up NTP, I followed the instructions
[here](http://rbgeek.wordpress.com/2012/04/30/time-synchronization-on-ubuntu-12-04lts-using-ntp/).
 I commented out the lines in `/etc/ntp.conf` for Ubuntu's own NTP
servers and instead used `ntp.plus.ne`,  `ntp2d.mcc.ac.uk`
and `ntp2c.mcc.ac.uk` (`mcc.ac.uk` is Manchester University).  There's
an (out of date) list of public NTP servers
[here](http://www.timetools.co.uk/ntp-servers/ref/ntp-server-uk.htm)
(using `sandvika.net` gives a "host name not found" error) and a longer
list
[here](http://www.galsys.co.uk/time-server/public-ntp-servers.html).

### Permenantly disable a kernel module (without recompiling)

add "`blacklist MODNAME`" to`/etc/modprobe.d/blacklist-local.conf`.
 e.g. "`blacklist ums_realtek`" (note that a newline is required after
the module name) (which was required to stop "Assuming drive cache:
write through" on my Lenovo S10e netbook (running Ubuntu 12.04 server)).
[Blacklist info found on serverfault](http://serverfault.com/a/162010);
[removing ums\_realtek to fix problem on netbook found on
bugs.launchpad](https://bugs.launchpad.net/ubuntu/+source/linux/+bug/925760/comments/8).

### CPU frequency

    sudo apt-get install cpufrequtils
    cpufreq-info

### Temperatures

    sudo apt-get install acpi
    acpi -V

    Battery 0: Full, 100%
    Battery 0: design capacity 2808 mAh, last full capacity 1996 mAh = 71%
    Adapter 0: on-line
    Thermal 0: ok, 55.0 degrees C
    Thermal 0: trip point 0 switches to mode critical at temperature 86.0 degrees C
    Thermal 0: trip point 1 switches to mode passive at temperature 80.0 degrees C
    Cooling 0: LCD 0 of 10
    Cooling 1: Processor 0 of 10
    Cooling 2: Processor 0 of 10

### System info display when you SSH into a machine

To get this displayed when you SSH into a machine:

    ~/$ ssh vaio
    jack@vaio's password: 
    Welcome to Ubuntu 12.04 LTS (GNU/Linux 3.2.0-27-generic i686)

     * Documentation:  https://help.ubuntu.com/

      System information as of Fri Aug 10 11:19:02 BST 2012

      System load:  0.63              Processes:           72
      Usage of /:   6.6% of 19.83GB   Users logged in:     1
      Memory usage: 11%               IP address for eth0: 192.168.1.64
      Swap usage:   0%

      Graph this data and manage this system at https://landscape.canonical.com/

Run `sudo apt-get install landscape-common update-motd`

### Compiz with Unity-2D

Intalling Ubuntu 12.04 on a circa-2004-computer with an nVidia GeForce
PCX 5300, I noticed that Compiz was disabled by default. After lots of
messing around with uninstalling and re-installing compiz, I stumbled
across the following thread: [How to run Compiz on
Unity-2D](http://askubuntu.com/a/130462). I then had to fix some of my
settings, especially re-enabling dBus and animations and window
decorations.

