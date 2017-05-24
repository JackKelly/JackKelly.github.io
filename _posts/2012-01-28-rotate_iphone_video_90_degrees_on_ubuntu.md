---
title: "Rotate iPhone video 90 degrees on Ubuntu"
date: 2012-01-28 10:17:33 +0000
categories: ["video", "Ubuntu"]
permalink: /rotate_iphone_video_90_degrees_on_ubuntu
---
A very quick note about rotating .MOV videos shot on an iPhone 90
degrees clockwise on Ubuntu.  The first tool I tried was `ffmpeg` isn't
compiled with the `-vf` command-line option enabled. You could
re-compile `ffmpeg`:



{% highlight bash %}
sudo apt-get install mencoder
mencoder -vf rotate -o Input.MOV -oac copy -ovc copy Output.MOV
{% endhighlight %}


(I was using `-oac lavc -ovc lavc` but any anonymous commenter suggested the much
better idea of using `copy`)

<!--break-->

