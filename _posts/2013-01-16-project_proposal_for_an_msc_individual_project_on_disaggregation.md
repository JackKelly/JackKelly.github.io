---
title: "Project proposal for an MSc individual project on disaggregation"
date: 2013-01-16 16:35:26 +0000
categories: ["PhD", "MSc", "student project"]
permalink: /project_proposal_for_an_msc_individual_project_on_disaggregation
---
Imperial MSc Computing Science students do [a 3-month individual project
over summer](http://www.doc.ic.ac.uk/lab/msc-projects/). Below is a
proposal I and my Ph.D. supervisor have just submitted. Of course, there
are no guarantees that any students will be interested...

"Inferring appliance-by-appliance energy consumption from whole-house
electricity meter readings"

By the end of the decade, every house in the UK will have a "smart
meter" installed. Each smart meter will record the electricity
consumption for the whole house once every ten seconds.

There is good evidence that people find appliance-by-appliance
information to be considerably more useful than whole-house aggregate
information when making decisions about saving energy. Hence it would be
very useful to be able to disaggregate whole-house electricity meter
signals into appliance-by-appliance information.

The aim of this project is to implement a disaggregation algorithm and
evaluate its performance against real data. The design of the
disaggregation algorithm can be your own invention or an algorithm
already described in the literature. There are many approaches to this
problem and you will be free to choose an approach.

We have a dataset recorded from multiple houses over several months (for
each house we recorded the whole-house current and voltage waveforms at
8kHz as well as the "ground truth" of how much power individual
appliances are actually using). We also have funding to install meters
in your own home, if you wish.

Further reading:

For the "classic" paper on this topic, see:

G. W. Hart, ‘Nonintrusive appliance load monitoring’, Proceedings of the
IEEE, vol. 80, no. 12, pp. 1870–1891, Dec. 1992.
[DOI:10.1109/5.192069](http://dx.doi.org/10.1109/5.192069)

For a recent review of the literature, see:

K. C. Armel, A. Gupta, G. Shrimali, and A. Albert, ‘Is disaggregation
the holy grail of energy efficiency? The case of electricity’, Energy
Policy, vol. 52, pp. 213 – 234, 2013.
[DOI:10.1016/j.enpol.2012.08.062](http://dx.doi.org/DOI:10.1016/j.enpol.2012.08.062)
<!--break-->

