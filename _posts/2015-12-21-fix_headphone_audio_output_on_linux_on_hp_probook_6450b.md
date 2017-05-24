---
title: "Fix headphone audio output on Linux on HP ProBook 6450b"
date: 2015-12-21 21:21:08 +0000
categories: ["laptop", "linux"]
permalink: /fix_headphone_audio_output_on_linux_on_hp_probook_6450b
---
The headphone output on my HP ProBook 6450b on Ubuntu Linux stopped
working a few updates ago and I think I've found how to fix it:


```
cd /usr/share/pulseaudio/alsa-mixer/paths
sudo cp analog-output-headphones.conf analog-output-headphones.bak
gksudo emacs analog-output-headphones.conf
```

Turn on the master volume (it was 'mute'):



```
[Element Master]
switched = on
```

and turn on Speaker+LO:


```
[Element Speaker+LO]
switch = on
volume = merge
```

Save and exit. Then restart also with `sudo alsa force-reload`. Then
remove headphones and re-plug them, That should work :)

