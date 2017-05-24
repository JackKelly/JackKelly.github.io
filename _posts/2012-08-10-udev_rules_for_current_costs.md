---
title: "udev rules for Current Costs"
date: 2012-08-10 07:44:56 +0000
categories: ["udev", "PhD", "Ubuntu", "linux", "CurrentCost"]
permalink: /udev_rules_for_current_costs
---

### Update Oct 11th 2012

It may not be necessary to add a new udev rule to access a CurrentCost
(or program a Nanode). Instead it may just be necessary to add yourself
to the `dialout` group. Haven't tested this on a new
installation yet.

------------------------------------------------------------------------

[`udev`](https://linux.die.net/man/7/udev) manages the `/dev/` filesystem on a modern Linux machine. When you first connect a
Current Cost USB cable to a Linux machine, you may find that the
relevant `/dev/ttyUSB[0-9]` file has not got the correct permissions
to allow you to access it as a normal user.

These are the steps that allowed me to connect my Current Cost to my
Ubuntu Server 12.04 machine:

1.  I added my username, `jack` group
    with the command `sudo usermod -a -G fuse jack` (append) is ESSENTIAL! If you forget the
    `-a` then
    your username will *only* be in the fuse group. If you accidentally
    forget the `-a` then boot into Ubuntu recovery mode, then
    run a disk check (to mount the filesystem as read/write), then drop
    into root command line mode, then issue the comman `usermod -a -G sudo username` as per the instructions
    [here](http://maketecheasier.com/fixing-sudo-error-in-ubuntu/2012/01/03)
    and then you can add yourself to the default groups listed
    [here](http://ubuntuforums.org/showthread.php?t=1970991).)
2.  Log out and log back in again for the group changes to take effect
    (it isn't sufficient to close the terminal and open it again).
3.  I created a new file `/etc/udev/rules.d/current-cost.rules`. This file contains the following text:

    ```
    SUBSYSTEM!="usb_device", ACTION!="add", GOTO="currentcost_rules_end"
     
    # Current Cost (the following rule should be all on one line)
    ATTRS{idVendor}=="067b", ATTRS{idProduct}=="2303", MODE="660", GROUP:="fuse" 
     
    LABEL="currentcost_rules_end"
    ```

    

4.  After saving this file, I unplugged all Current Cost EnviR monitors
    from my machine and plugged them in again. (Note that running `sudo service udev restart` doesn't appear to be sufficient or
    necessary to start using the new `udev` rules.)
5.  Check that the permissions have been set correctly by running `ls -ld /dev/ttyUSB?`. The result should be something like this:
    `crw-rw---- 1 root fuse 188, 0 Aug 10 08:43 /dev/ttyUSB0` (the crucial things to check are that
    group has read and write permissions and that the group is set to
    `fuse` rules

Each line is a rule. `udev` and `!=`; if those
checks all succeed then it evaluates the assignment operators `=` (the second of
which ensures that the value assigned to that key isn't changed by a
subsequent rule). Let's consider the line which starts `ATTRS...` (owner and group have read and write
permissions) and will set `GROUP:="fuse"` ensures
that the group will not be changed later) for all devices where `ATTRS{idVendor}=="067b"` and `ATTRS{idProduct}=="2303"`.

How do we which attributes to check for? If we only care about `idVendor` then
plug the device in and run `lsusb`



```
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


The line `Bus 002 Device 026: ID 067b:2303 Prolific Technology, Inc. PL2303 Serial Port` is my Current Cost USB cable. If we want finer
control then run `udevadm info --name=/dev/ttyUSB0 --attribute-walk` to see a long list of key, value pairs you
could use in your `udev` rules.

### More info:

-   [udev man page](http://linux.die.net/man/7/udev)
-   [udev on the Debian wiki](http://wiki.debian.org/udev)

<!--break-->

