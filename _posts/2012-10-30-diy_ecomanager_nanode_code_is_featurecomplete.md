---
title: "DIY EcoManager Nanode code is feature-complete!"
date: 2012-10-30 19:19:10 +0000
categories: ["PhD", "CurrentCost"]
permalink: /diy_ecomanager_nanode_code_is_featurecomplete
---
Hurray! At long, LONG last the embedded C++ code for my [DIY
EcoManager](https://github.com/JackKelly/rfm_edf_ecomanager) is
feature-complete! It's hard to believe that it's been a full two months
since [I started](/hacking_the_current_cost) on this mission to build a
DIY Current Cost receiver. Back then I thought it'd only take a couple
of weeks! The last two months have been spent writing over 3,000 lines
of C++, scratching my head lots over the EcoManager protocol and how to
use the RFM12b wireless module. Oh, and [blowing up my
laptop](/blew_up_my_laptop_sniffing_spi_bus_of_iam) of course. And I've
met some really smart folks who are trying to do similar projects;
without whom I honestly wouldn't have been able to get this project
done. I've also really gotten into using the wiki and issue tracker
features on github: the integration between commits, the issue tracker
and the wiki is great.

The next step is to write a Python script to log the data coming from
the Nanode and keep track of which IAMs are connected to which
appliance. And then either build an Open Energy Monitor to measure both
real and reactive power for my whole house, or pester Ecotricity to get
me on their smart meter trial.

And then, once I've got all my data logging kit quietly collecting data,
I'll finally be able to get cracking with my "proper" work of doing
smart meter disaggregation!

<!--break-->

