---
title: "moving photos from Gallery2 to Flickr"
date: 2011-10-18 21:57:51 +0000
categories: ["photography", "flickr", "gallery2"]
permalink: /moving_photos_from_gallery2_to_flickr
---
From about 2003 until today, I kept my photos in a variety of places.
Most of my photos were on my old website's photo gallery which ran the
excellent [Gallery2](http://gallery.menalto.com/) software. For a number
of reasons, I decided to move all my photos to [my Flickr
account](http://www.flickr.com/photos/37816297@N06/). (I wanted to make
use of the community features on flickr, I was failing to keep my
Gallery2 install updated and my Android phone makes it really easy to
upload photos direct to Flickr). Moving the photos is pretty easy using
the [Gallery2Flickr plug-in](http://gallery2flickr.sourceforge.net/) for
Gallery2. Transferring photos mostly went smoothly but occasionally it
failed with the following error:
<div class="geshifilter">

``` {.bash .geshifilter-bash style="font-family:monospace;"}
Catchable fatal error:
Object of class GalleryStatus could not be converted to string in modules/Gallery2Flickr/classes/phpFlickr/phpFlickr.php on line 214
```

</div>

After some tinkering, this was fixed by setting the parameter
<div class="geshifilter">

``` {.php .geshifilter-php style="font-family:monospace;"}
$storeConfig['type'] = 'mysql';
```

</div>

in <span class="geshifilter">`config.php`{.text
.geshifilter-text}</span> (it was set as <span
class="geshifilter">`'mysqli'`{.text .geshifilter-text}</span>). This is
a bit of a dirty hack but it works.

