---
title: "udev rules for Current Costs"
date: 2012-08-10 07:44:56 +0000
categories: ["udev", "PhD", "Ubuntu", "linux", "CurrentCost"]
permalink: /udev_rules_for_current_costs
---
### Update Oct 11th 2012

It may not be necessary to add a new udev rule to access a CurrentCost
(or program a Nanode). Instead it may just be necessary to add yourself
to the <span class="geshifilter">`dialout`{.text
.geshifilter-text}</span> group. Haven't tested this on a new
installation yet.

------------------------------------------------------------------------

[<span class="geshifilter">`udev`{.text
.geshifilter-text}</span>](http://linux.die.net/man/7/udev) manages the
<span class="geshifilter">`/dev/`{.text .geshifilter-text}</span>
filesystem on a modern Linux machine. When you first connect a Current
Cost USB cable to a Linux machine, you may find that the relevant <span
class="geshifilter">`/dev/ttyUSB[0-9]`{.text .geshifilter-text}</span>
file has not got the correct permissions to allow you to access it as a
normal user.

These are the steps that allowed me to connect my Current Cost to my
Ubuntu Server 12.04 machine:

1.  I added my username, <span class="geshifilter">`jack`{.text
    .geshifilter-text}</span>, to the <span
    class="geshifilter">`fuse`{.text .geshifilter-text}</span> group
    with the command <span
    class="geshifilter">`sudo usermod -a -G fuse jack`{.text
    .geshifilter-text}</span>. (The <span class="geshifilter">`-a`{.text
    .geshifilter-text}</span> (append) is ESSENTIAL! If you forget the
    <span class="geshifilter">`-a`{.text .geshifilter-text}</span> then
    your username will *only* be in the fuse group. If you accidentally
    forget the <span class="geshifilter">`-a`{.text
    .geshifilter-text}</span> then boot into Ubuntu recovery mode, then
    run a disk check (to mount the filesystem as read/write), then drop
    into root command line mode, then issue the comman <span
    class="geshifilter">`usermod -a -G sudo username`{.text
    .geshifilter-text}</span> as per the instructions
    [here](http://maketecheasier.com/fixing-sudo-error-in-ubuntu/2012/01/03)
    and then you can add yourself to the default groups listed
    [here](http://ubuntuforums.org/showthread.php?t=1970991).)
2.  Log out and log back in again for the group changes to take effect
    (it isn't sufficient to close the terminal and open it again).
3.  I created a new file <span
    class="geshifilter">`/etc/udev/rules.d/current-cost.rules`{.text
    .geshifilter-text}</span>. This file contains the following text:
    <div class="geshifilter">

    ``` {.text .geshifilter-text style="font-family:monospace;"}
    SUBSYSTEM!="usb_device", ACTION!="add", GOTO="currentcost_rules_end"
     
    # Current Cost (the following rule should be all on one line)
    ATTRS{idVendor}=="067b", ATTRS{idProduct}=="2303", MODE="660", GROUP:="fuse" 
     
    LABEL="currentcost_rules_end"
    ```

    </div>

4.  After saving this file, I unplugged all Current Cost EnviR monitors
    from my machine and plugged them in again. (Note that running <span
    class="geshifilter">`sudo service udev restart`{.text
    .geshifilter-text}</span> doesn't appear to be sufficient or
    necessary to start using the new <span
    class="geshifilter">`udev`{.text .geshifilter-text}</span> rules.)
5.  Check that the permissions have been set correctly by running <span
    class="geshifilter">`ls -ld /dev/ttyUSB?`{.text
    .geshifilter-text}</span>. The result should be something like this:
    <span
    class="geshifilter">`crw-rw---- 1 root fuse 188, 0 Aug 10 08:43 /dev/ttyUSB0`{.text
    .geshifilter-text}</span> (the crucial things to check are that
    group has read and write permissions and that the group is set to
    <span class="geshifilter">`fuse`{.text .geshifilter-text}</span>)

### A quick explanation of the <span class="geshifilter">`udev`{.text .geshifilter-text}</span> rules

Each line is a rule. <span class="geshifilter">`udev`{.text
.geshifilter-text}</span> checks the truth of all <span
class="geshifilter">`==`{.text .geshifilter-text}</span> and <span
class="geshifilter">`!=`{.text .geshifilter-text}</span>; if those
checks all succeed then it evaluates the assignment operators <span
class="geshifilter">`=`{.text .geshifilter-text}</span> and <span
class="geshifilter">`:=`{.text .geshifilter-text}</span> (the second of
which ensures that the value assigned to that key isn't changed by a
subsequent rule). Let's consider the line which starts <span
class="geshifilter">`ATTRS...`{.text .geshifilter-text}</span>. This
will set <span class="geshifilter">`MODE="660"`{.text
.geshifilter-text}</span> (owner and group have read and write
permissions) and will set <span
class="geshifilter">`GROUP:="fuse"`{.text .geshifilter-text}</span>
(<span class="geshifilter">`:=`{.text .geshifilter-text}</span> ensures
that the group will not be changed later) for all devices where <span
class="geshifilter">`ATTRS{idVendor}=="067b"`{.text
.geshifilter-text}</span> and <span
class="geshifilter">`ATTRS{idProduct}=="2303"`{.text
.geshifilter-text}</span>.

How do we which attributes to check for? If we only care about <span
class="geshifilter">`idVendor`{.text .geshifilter-text}</span> and <span
class="geshifilter">`idProduct`{.text .geshifilter-text}</span> then
plug the device in and run <span class="geshifilter">`lsusb`{.text
.geshifilter-text}</span>

<div class="geshifilter">

``` {.text .geshifilter-text style="font-family:monospace;"}
jack@lenovo:~/workingcopies/iam_logger$ lsusb
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 002 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
Bus 003 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
Bus 004 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
Bus 005 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
Bus 001 Device 004: ID 5986:0241 Acer, Inc BisonCam, NB Pro
Bus 001 Device 006: ID 0bda:0158 Realtek Semiconductor Corp. USB 2.0 multicard reader
Bus 002 Device 026: ID 067b:2303 Prolific Technology, Inc. PL2303 Serial Port
Bus 003 Device 002: ID 0a5c:2150 Broadcom Corp. BCM2046 Bluetooth Device
```

</div>

</p>
The line <span
class="geshifilter">`Bus 002 Device 026: ID 067b:2303 Prolific Technology, Inc. PL2303 Serial Port`{.text
.geshifilter-text}</span> is my Current Cost USB cable. If we want finer
control then run <span
class="geshifilter">`udevadm info --name=/dev/ttyUSB0 --attribute-walk`{.text
.geshifilter-text}</span> to see a long list of key, value pairs you
could use in your <span class="geshifilter">`udev`{.text
.geshifilter-text}</span> rules.

### More info:

-   [udev man page](http://linux.die.net/man/7/udev)
-   [udev on the Debian wiki](http://wiki.debian.org/udev)

<!--break-->

