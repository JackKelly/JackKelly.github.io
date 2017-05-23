---
title: "Using iPhone photo GPS coordinates in Google Maps"
date: 2012-03-06 17:07:20 +0000
categories: ["iphone", "photography"]
permalink: /using_iphone_photo_gps_coordinates_in_google_maps
---
Say you have a photo taken on an iPhone and you want to find out where
it was taken.  How can this be done?  Easy:

1.  Open in a photo editor which lets you view the metadata.  For
    example, gwenview works well on Ubuntu.
2.  Find the following attributes (I'll give specific values to make
    this example concrete)
    1.  <span class="geshifilter">`GPS Longitude Reference = West`{.text
        .geshifilter-text}</span>
    2.  <span class="geshifilter">`GPS Latitude Reference = North`{.text
        .geshifilter-text}</span>
    3.  <span class="geshifilter">`GPS Longitude = 0deg 3.19000'`{.text
        .geshifilter-text}</span>
    4.  <span class="geshifilter">`GPS Latitude = 51deg 27.72000'`{.text
        .geshifilter-text}</span>

3.  Given the data above, you'd enter <span
    class="geshifilter">`51 27.72', -0 3.19'`{.text
    .geshifilter-text}</span> into Google Maps.  The minus before the
    latitude is there because the latitude reference is "west" instead
    of "east".<!--break-->


