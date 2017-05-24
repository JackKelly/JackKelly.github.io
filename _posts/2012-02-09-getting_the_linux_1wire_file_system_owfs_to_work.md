---
title: "Getting the Linux 1-wire file system owfs to work"
date: 2012-02-09 22:28:56 +0000
categories: ["1-wire", "owfs"]
permalink: /getting_the_linux_1wire_file_system_owfs_to_work
---
I followed the installation instructions on the [Ubuntu
wiki](https://help.ubuntu.com/community/1wireSoftware) but got stuck on
the line where we try to get owfs to talk to the 1-wire network.  This
worked for me:


```
sudo /opt/owfs/bin/owfs u -m /var/lib/1wire
```


I have a Dallas Semiconductor DS1490F 2-in-1 Fob, 1-Wire adapter.  Also,
after installing, I found that the Navitron forum has [a discussion on
owfs](http://www.navitron.org.uk/forum/index.php/topic,12604.0).

All I want to be able to do is log temperature data to a text file.  I
think I'll write a simple C++ app to log the temperature data to a text
file and then use [gnuplot](http://www.gnuplot.info/) to plot graphs.

<!--break-->

In Python, I found I was getting the following error:



```
​>>> import ow
>>> ow.init('u')
DEFAULT: ow_ds9490.c:(255) Unclear what <> means in USB specification, 
         will use first adapter.
DEFAULT: owlib.c:(201) Cannot open USB bus master
DEFAULT: owlib.c:(54) No valid 1-wire buses found
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python2.6/dist-packages/ow/__init__.py", line 224, in init
    raise exNoController
ow.exNoController
```


This turned out to be a permissions issue.  Running python as sudo fixed
the problem, but this clearly isn't a good solution.  Luckily, [a kind
person gave a guide on how to make the 1-wire USB adapter usable for
non-root users](http://owfs.org/index.php?page=udev-and-usb).  I
modified the file very slightly.  All you have to do is to create a file
called `/etc/udev/rules.d/owfs.rules` which looks something like this:


```
SUBSYSTEM!="usb_device", ACTION!="add", GOTO="owfs_rules_end"
 
# DS2490 1-Wire adapter
SYSFS{idVendor}=="04fa", SYSFS{idProduct}=="2490", MODE="660", GROUP="fuse"
 
LABEL="owfs_rules_end"
```


Unplug and plug your USB adapter back in.  If that doesn't work then
check that you're a member of the `fuse` and
`idVendor` with
`GROUP:="fuse"`.  If that still doesn't work then try
replacing `SYSFS`).  For more info on udev, and for a
description of how I got udev to work with my Current Cost USB cable,
see [this blog post](/udev_rules_for_current_costs).

Here's a simple little Python script for logging every temperature
sensor reading once a minute:



{% highlight python %}
#! /usr/bin/env python
print "running..."
import ow
import time

ow.init( 'u' )

# We're accessing the 1-wire bus directly from python but
# if you want to use owserver:
# ow.init( 'localhost:3030' ) # /opt/owfs/bin/owserver -p 3030 -u -r

sensors = ow.Sensor("/").sensorList()

# We're only interested in temperature sensors so remove
# any 1-wire devices which aren't temperature sensors
for sensor in sensors[:]:
    if sensor.type != 'DS18B20':
        sensors.remove( sensor ) 

# Print column headers
for sensor in sensors:
    print sensor.r_address + "\t",
print "\n",

# Print temperatures
while 1==1:
    print int(time.time()), "\t",
    for sensor in sensors:
        print sensor.temperature, "\t",
    print "\n",
    time.sleep(60)
{% endhighlight %}



And here are some handy links to the owfs documentation:
[owpython](http://owfs.sourceforge.net/owpython.html) and
[owserver](http://owfs.sourceforge.net/owserver.1.html).

The next things to do are to connect up some more temperature sensors so
I can see the temp drop across our UFH, and tinker with some graphing
utilities like [matplotlib](http://matplotlib.sourceforge.net/) and
[Google's Chart Tools API](http://code.google.com/apis/chart/); and
tinker with sending data to [pachube](https://pachube.com/).

### Update 24th Feb 2012

My owfs Python code (including code to send the data to Pachube) is [now
on github](https://github.com/JackKelly/owfsPachubeTX) - please see
github for the latest code.

