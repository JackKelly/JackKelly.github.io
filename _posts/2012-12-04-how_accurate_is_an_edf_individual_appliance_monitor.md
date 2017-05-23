---
title: "How accurate is an EDF individual appliance monitor?"
date: 2012-12-04 17:30:24 +0000
categories: ["PhD", "CurrentCost"]
permalink: /how_accurate_is_an_edf_individual_appliance_monitor
---
To try to get a feel for how accurate the [EDF transmitter
plug](https://shop.edfenergy.com/Item.aspx?id=540&CategoryID=1) is, I
simultaneously recorded our washing machine using a [WattsUp
meter](https://www.wattsupmeters.com/secure/products.php?pn=0&wai=0&more=1),
an [EDF transmitter
plug](https://shop.edfenergy.com/Item.aspx?id=540&CategoryID=1) and an
[EDF whole-house
transmitter](https://shop.edfenergy.com/Item.aspx?id=547&CategoryID=1).
The WattsUp samples once a second, the EDF devices sample about once
every 6 seconds. (data was collected from the EDF devices using my
[Nanode code](https://github.com/JackKelly/rfm_edf_ecomanager/) and my
[logging script](https://github.com/JackKelly/rfm_ecomanager_logger/)).
Here are the results (click on the image for a larger version):

[![Watts Up versus EDF IAM versus whole
house](/files/blog/wm_three_small.png)](/files/blog/wm_three.png)

And here's the same data but this time the EDF IAM and WattsUp are laid
on top of each other. I'm happy that the EDF device is of comparable
accuracy to the WattsUp, at least in this experiment:

[![Watts Up versus EDF
IAM](/files/blog/wm_wattsup_edf_iam_small.png)](/files/blog/wm_wattsup_edf_iam.png)

One thing I need to investigate a little more is that occasionally the
EDF IAM appears to give a reading which is above the theoretical max
wattage an appliance can draw (13 amps x 230 volts = 2990 watts). This
doesn't appear to be an RF corruption issue (because the checksum is
OK). I guess it's possible that our washing machine does sometimes draw
too much (but for a short enough time to mean the fuse doesn't blow). I
was hoping to capture an "overload" event in the data capture I did for
the graphs above but unfortunately it didn't occur. If I get time I
might try recording more WattsUp signals from our washing machine.

I've just ordered another 10 EDF IAMs. When these arrive (in about 10
days) I will have a total of 14 EDF IAMs. I'll run these for a week or
so. If these check out OK then I'll probably order another 15 to get to
a total of 30 to monitor every appliance in my home.

<!--break-->

