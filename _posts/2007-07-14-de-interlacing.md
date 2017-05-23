---
title: "de-interlacing"
date: 2007-07-14 15:08:43 +0000
categories: ["notes", "filmmaking"]
permalink: /notes/de-interlacing
---
### Tests and thoughts about de-interlacing footage using Premiere Pro and aviSynth

I've made quite a few notes over on [this thread on
DVinfo.net](http://dvinfo.net/conf/showthread.php?t=97455). The main
observations are:

<ul>
<li>
Tests with a resolution chart show that Premiere Pro 2 does indeed
reduce the vertical resolution (as expected). However, I'm hard pressed
to see a difference in "real" footage.

</li>
<li>
It is possible to import aviSynth scripts into Premiere Pro 2 but
playback is non-real-time with HDV footage and the system becomes a
little unstable. Playback judders a little even if the aviSynth script
does nothing cleverer than simply loading a video (even if the Premiere
Pro aviSynth importer is set to "fastest")

</li>
<li>
My preferred work flow for dealing with interlaced footage destined for
non-CRT screens is this:

</li>
-   Shoot 1080/50i
-   Edit 1080/50i
-   Export from PPro as "Microsoft AVI", compressor=none, don't
    de-interlace - alternatively [frameserver from PPro to
    aviSynth](http://avisynth.org/mediawiki/AviSynth_FAQ_Section_2)
-   Use aviSynth to de-interlace to produce either 1080/50p, 1080/25p or
    720/50p
-   Import into PPro to render out as WMV9

</ul>
### Notes on installing aviSynth

-   Install aviSynth
-   Install the MT mod (to allow multi-threading on some filters
-   Install the Premiere Pro import plug-in
-   install yadif, MVbob and MCbob

### Some sample aviSynth scripts

    Load_Stdcall_plugin("C:\Program Files\AviSynth 2.5\plugins\yadif.dll")

    # export from PPro as "Microsoft AVI", compressor=none

    DirectShowSource("interlaced.avi", fps=25, audio=false, video=true)

    # AviSource("uncompressed_50i_none.avi")
    # AviSource seems buggy

    # http://avisynth.org/mediawiki/Convert
    # I still have to test the colour matrix settings

    ConvertToYUY2(matrix="PC.709", interlaced=true)

    # DGDecode_mpeg2source("resolution_tests.d2v")

    # http://avisynth.org.ru/yadif/yadif.html
    mt("yadif(mode=0)",threads=4)

