---
title: "Fixing a waterlogged iPhone 3GS"
date: 2011-11-09 17:40:33 +0000
categories: ["iphone", "electronics"]
permalink: /fixing_a_waterlogged_iphone_3gs
---
About a week ago, my wife's iPhone 3GS found its way into the washing
machine and spent a good 15 minutes being washed before it was rescued. 
We eventually got it to work this morning.  I'll quickly describe what
we tried; what worked and what didn't work.\
\
On retrieving the phone from the washing machine, my wife tried to turn
it on.  The phone gave no signs of life. I would have thought that it's
generally a bad idea to try to fire up an electrical device whilst it's
still wet (because current might flow to places that it's not supposed
to flow) but it doesn't seem to have done any permanent damage on this
occasion (but I'd highly recommend you don't fire up any electrical
device whilst it's wet).\
\
My wife googled for suggestions.  The first resuscitation technique my
wife tried was to leave the iPhone in a bag of rice for a couple of days
(I was sceptical that this was any better than just leaving it to
breath). 

She then decided, after some gentle persuasion from me, to take the
phone apart (which is surprisingly easy when you know how - see below)
and we found that it was still dripping wet inside.  So I'm now
extremely sceptical that leaving an iPhone in a bag of rice is
especially useful.  Unless you enjoy carefully removing grains of rice
from every orifice of the iPhone.

After taking the screen off the body and removing the logic board, we
left the parts to dry on some paper towel for a couple of days. 

I then put the phone back together.  It wouldn't start.  I plugged it
into the charger and it started OK but was locked (i.e. I think the
phone had detected that it had been tampered with and refused to
activate without being plugged into a PC).  It would turn off
*immediately* after the charger was removed.  I plugged the phone into a
PC to activate the phone but the phone refused to start correctly: my
guess is that it couldn't draw enough power from the USB port to start
up.\
\
At this stage it became clear that we had 2 problems:

1.  the battery was totally dead (or had become disconnected) and
2.  the phone was locked (hence we couldn't browse photos or run any
    apps).  To unlock it we needed to plug it into a laptop but the
    phone wouldn't start whilst plugged into a computer.

After leaving the phone plugged into its charger and switched on
overnight it unlocked itself (so we could access photos etc) but the
battery was still completely flat and the phone refused to connect to
the cellular network.\
\
I decided to double-check that the battery was correctly connected.  I
dismantled the phone again.  I cleaned all the relevant contacts with
cotton buds dipped in isoproyl alcohol and then used compressed air to
remove dust.  After careful re-assembly, the phone behaved exactly as
before. Pah.\
\
So we bought a replacement battery for about £6 online.  After
installing the replacement battery, the phone works perfectly (although
the screen is a little damaged). 

My volt meter reported that the old battery was producing only 2.1 volts
across the top two pins (compared to a normal voltage of 3.7 volts).
Lithium Polymer batteries need a lot of pampering (which is usually done
by the charging/discharging circuitry): if they get below a certain
voltage then they are permanently damaged.  2.1 volts is, I suspect,
well below the "safe" voltage for a LiPoly battery ([WikiPedia suggests
that the safe voltage range is 3.0 to 4.23 volts per LiPoly
cell](http://en.wikipedia.org/wiki/Lithium-ion_polymer_battery#Charging)). 
So either the battery shorted out whilst wet, or water got into the
battery and damaged its chemistry.

### Conclusions and advice:

If you get your phone wet, I frankly wouldn't bother putting it in a bag
with rice. Our experience suggests that leaving a phone in a bag of rice
for 2 days totally fails to remove water from the internals.  Instead
take the screen off the phone body (so air can get to the inside of the
phone) and leave it to dry normally for a couple of days.  Taking the
screen off the phone is easy, and [this excellent iFixIt
video](http://www.youtube.com/watch?v=wuaHt_jRSo8&feature=player_embedded)
shows most of the steps.  The basic steps are:

1.  remove the 2 screws at the bottom of the phone, either side of the
    connector. 
2.  remove the sim card from the top of the phone. 
3.  apply a sucker to the screen (towards the bottom of the screen, near
    the home button).  Hold the base of the phone with one hand by
    grasping the connector socket with your thumb and the sim slot with
    your middle finger.  Pull the sucker with your other hand.  Ideally
    you shouldn't let the screen pop off too quickly (as it will
    ungracefully rip the connectors off between the screen and the
    logic board) but I pulled the screen off too quickly twice and it
    doesn't seem to have done any damage: the connectors just pop off
    without breaking.

If you decide to take the logic board out then make sure you keep track
of which screw goes where as there are about 4 different types of screws
used in the phone.  In order to remove the logic board, I had to remove
a screw which was hidden under a little sticky label on which was
written "DO NOT REMOVE". But I removed it.  And now the phone works
fine.  Go figure. Moral of the story: little sticky labels lie.\
\
Good luck!\
\
(A quick disclaimer: this blog post is just a quick description of what
we did to fix my wife's waterlogged phone.  Whilst I've tried not to say
anything really stupid; it is of course your sole responsibility if you
break your phone.)

