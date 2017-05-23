---
title: "Not currently working on the energy disaggregation competition"
date: 2017-03-29 08:29:16 +0000
categories: ["PhD", "nilm"]
permalink: /not_currently_working_on_the_energy_disaggregation_competition
---
Towards the end of last year, I was lucky enough to have a short postdoc
paid for by EDF Energy. The main focus of the postdoc was on looking at
ways to design a competition to compare the performance of different
disaggregation algorithms. This postdoc finished in January 2017 so I am
not currently working on the disaggregation competition (although I
strongly believe that finding a good way to compare NILM algorithms is
one of the most important unsolved problems in NILM).

Very briefly: the main challenge in designing a NILM competition is
getting enough clean, private testing data. It turns out that the
performance of NILM algorithms can be quite inconsistent across houses:
an algorithm might work well on some houses; but on other houses that
same algorithm might work badly. Also, one of the promising uses of NILM
is to identify "extreme" energy behaviour (such as leaving your electric
oven on constantly just in case you fancy doing some baking).
Identifying "extreme" behaviour is useful because users can save large
sums of money with a single, simple change in behaviour. But - by
definition - "extreme" behaviour is rare. Hence we need a *large*
testing dataset (maybe 100 houses) to be confident that we're accurately
capturing the performance of each algorithm; and that each algorithm can
recognise "extreme" energy behaviour. Recording this quantity of real
data would be very expensive and time consuming. Hence we could consider
building a high-quality simulator to generate realistic data. But this
raises a whole host of additional challenges! <!--break-->

