---
title: "Rotate iPhone video 90 degrees on Ubuntu"
date: 2012-01-28 10:17:33 +0000
categories: ["video", "Ubuntu"]
permalink: /rotate_iphone_video_90_degrees_on_ubuntu
---
A very quick note about rotating .MOV videos shot on an iPhone 90
degrees clockwise on Ubuntu.  The first tool I tried was <span
class="geshifilter">`ffmpeg`{.text .geshifilter-text}</span> but it
turns out that the Ubuntu version of <span
class="geshifilter">`ffmpeg`{.text .geshifilter-text}</span> isn't
compiled with the <span class="geshifilter">`-vf`{.text
.geshifilter-text}</span> command-line option enabled. You could
re-compile <span class="geshifilter">`ffmpeg`{.text
.geshifilter-text}</span> from source but it's easier to use <span
class="geshifilter">`mencoder`{.text .geshifilter-text}</span>:

<div class="geshifilter">

``` {.bash .geshifilter-bash style="font-family:monospace;"}
sudo apt-get install mencoder
mencoder -vf rotate -o Input.MOV -oac copy -ovc copy Output.MOV
```

</div>

(I was using <span class="geshifilter">`-oac lavc -ovc lavc`{.text
.geshifilter-text}</span> but any anonymous commenter suggested the much
better idea of using <span class="geshifilter">`copy`{.text
.geshifilter-text}</span>)

<!--break-->

