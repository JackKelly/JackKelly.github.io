---
title: "Simulating disaggregated electricity data"
date: 2016-11-03 12:31:10 +0000
categories: ["nilm", "nilmtk", "metrics", "competition"]
permalink: /simulating_disaggregated_electricity_data
---
To do rigorous NILM research, we need lots of high-quality disaggregated
electricity data. This is especially true if we want to run a good NILM
competition.

There are now [20 public datasets listed on the NILM
wiki](http://wiki.nilm.eu/index.php?title=NILM_datasets). But *all* real
data suffers from problems which make it problematic for use in a NILM
competition. These problems include:

<!--break-->

-   Incorrectly labelled sub-meters. e.g. a channel labelled "washing
    machine" actually records the kitchen radio. Or: the "washing
    machine" channel starts off recording the washer but, half way
    through the dataset, the homeowner accidentally swaps smart plugs
    and the channel labelled "washer" starts recording the tumble
    drier instead. There are many more ways in which channels can be
    incorrectly labelled.
-   Some appliances within each home in the dataset are not sub-metered.
    Indeed, very few datasets even *attempt* to rigorously sub-meter
    every appliance.
-   Little consistency across homes with respect to which appliances
    are metered. e.g. House 1 might have PV panels and an EV but none of
    the other homes in the dataset have these. How do we split this
    dataset up into separate "training" and "testing" datasets if we
    want to test generalisation across homes?
-   Sampling bias. For example, in my dataset (UK-DALE), the five homes
    were homes of Imperial MSc / PhD students. Hardly a representative
    sample from the UK! In general, NILM datasets have a lack of
    geographical diversity (for example, there are no public datasets
    from Russia, China, Africa or Brazil) and a lack of
    demographic diversity.
-   No ground-truth labels for important NILM use-cases. For example,
    one important NILM use-case might be to tell people when their
    fridge's door seal needs replacing. But how can we measure the
    performance of NILM algorithms at detecting failing fridges if
    "failing fridges" aren't labelled in the ground truth? (See [Batra,
    Singh & Whitehouse
    2016](http://nilmworkshop.org/2016/proceedings/Paper_ID08.pdf) for a
    thought-provoking discussion of whether NILM can detect
    failing fridges.)
-   Little or no coverage of unusual energy behaviours. It's likely that
    "average" domestic users won't reduce their energy consumption when
    given an itemised energy bill ([Kelly & Knottenbelt
    2016](https://arxiv.org/abs/1605.00962)). But one group of users who
    *might* be enabled by NILM to save lots of energy is users who
    accidentally or mistakenly use energy in an unusual way - such as
    using their electric oven as an AGA and leaving it on 24/7 just in
    case they fancy doing some baking. How can we measure NILM
    performance at detecting unusual behaviour if that unusual behaviour
    never happens in our dataset?
-   Little or no data from homes where appliances change over time. e.g.
    the old fridge is moved into the basement and a second, new fridge
    is added. Or the old CRT TV is replaced by a shiny new OLED TV. Or
    grandma moves into the spare room along with a bunch of her
    appliances and the whole home's energy behaviour changes. Or, in a
    rented flat, the tenants change and so almost all the
    appliances change. etc. etc.
-   Little or no labelling of *behaviours* and *individual energy
    users*.
-   Spurious readings / cross-talk / broken meters.
-   Gaps in time.

These problems *aren't* the result of dataset authors being lazy or
careless. It doesn't matter how much money and engineering you throw at
recording a "good" dataset. These problems are pretty much *inherent* in
recording data from real homes. Yet these problems also pose a
significant hurdle to conducting rigorous NILM research.

What if we could *artificially generate* an endless amount of
"near-perfect", realistic disaggregated data. And what if we could
select to generate data for a range of NILM scenarios (e.g. failing
fridges; or data from different countries; or homes where appliances
change over time).

This isn't a entirely new idea, of course. There have been several
papers on simulating appliance electricity data from the ground up
(where the electricity consumption of individual appliances is simulated
using models of the internal components of appliances; for an excellent
and recent example see [Chen, Irwin & Shenoy
2016](https://people.umass.edu/~dongchen/smartgridcomm16.pdf)).

A complementary approach to *simulating* appliances from the ground-up
would be to exploit the fact that we now have 20 datasets of
disaggregated appliance electricity consumption. We could carefully
dismantle these datasets and then re-combine them in endless ways. We'd
extract *real* appliance signatures for single appliance "activations"
and re-combine these real appliance activations in novel but realistic
configurations.

These two approaches have complementary strengths and weaknesses.
Perhaps the "ultimate" simulator would *combine* ground-up appliance
simulation with real appliance activations. For example, perhaps
ground-up models do a near-perfect job of simulating fridges, and would
allow us to simulate failing fridges. But perhaps ground-up simulation
doesn't work so well for washing machines so we'd use real washing
machine data. Or, if we got really clever, we could chop up real washing
machine data for the hard-to-simulate parts (perhaps the motor is hard
to simulate) and combine short samples of real motor data with ground-up
simulations of the washing machine's heating element (which might be
easy to simulate).

As well as simulating the appliance energy usage at high temporal
resolution, we also need to model *when* appliances are used. This is
quite well studied in the literature. The basic approach is to build
simple statistical models which capture patterns such as the time of day
that each appliance is used; and correlations between appliances etc.
These statistical models could be trained from disaggregated electricity
datasets or from high-quality appliance usage diaries. We'd then sample
randomly from these models to generate novel "appliance usage scripts".
Care must be taken to *include* outliers: we mustn't fall into the trap
of only simulating "Mr & Mrs Average".

Finally, we need to model which appliances are installed in each home.
We'd probably want separate models for different countries and different
demographic groups. These models could be trained from appliance
ownership surveys or disaggregated energy datasets.

Once a realistic simulator is built, it could be used to run a NILM
competition (perhaps combined with some *real* data).

The simulator could also enable a "NILM Gym" (inspired by [OpenAI's
Gym](https://gym.openai.com)): an open-source, downloadable tool which
would enable NILM researchers to quickly validate the performance of
their NILM algorithms against a range of scenarios; and to optionally
share results with the community. Kind of a cross between an informal
NILM competition and a unit-testing suite: every time you tweak your
algorithm, you test it against data produced by the "NILM Gym" and
produce a bunch of metrics for whatever range of NILM scenarios you're
currently focused on.

The NILM Gym's list of scenarios could include "failing fridges" or "a
representative sample of UK households" or "new tenant moves into rented
flat and replaces almost all the appliances". Researchers would be able
to easily add or modify scenarios and metrics. Scenarios could be learnt
from real data or specified by hand.

The NILM Gym could be developed rapidly. Hence it might be a good
testing ground to inform the design of a more formal, yearly NILM
competition.

The NILM Gym could also be used as an informal competition: If you want
then you can also upload your results to a common, public website to
allow the community to see your progress.

You'd be free to implement your NILM algorithms however you want: The
NILM Gym would just generate data and run metrics (one of my main
worries about NILMTK is that it's too monolithic (i.e. it locks you into
a walled garden): and I'm allowed to complain about that because it was
largely me who pushed for a monolithic design in the first place! I now
regret that design decision! I suspect NILMTK would have been easier to
use if it were a collection of small, well-defined tools, which could
easily be combined with each user's own code and tools).

I plan to be spend November and December exploring whether we can build
a "data augmentation tool" to generate an effectively infinite amount of
disaggregated electricity data. (I definitely won't be able to implement
all the ideas describe above; but I hope to build a proof-of-concept). I
welcome your thoughts!

(There's more discussion on [NILMTK issue \#26 "Simulator of
disaggregated domestic electricity demand at 1
Hz"](https://github.com/nilmtk/nilmtk/issues/26) and in this [Google
Doc](https://docs.google.com/document/d/1xv7VcQWfVk32BBVOU5gL7LFuqcrSaO_OfLWRYs36slA/edit?usp=sharing).
If you'd like to comment on these ideas then please do so on the NILMTK
issue or on the Google Doc. Thanks!).

