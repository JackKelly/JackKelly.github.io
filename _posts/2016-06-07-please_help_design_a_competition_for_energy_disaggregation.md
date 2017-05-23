---
title: "Please help design a competition for energy disaggregation algorithms!"
date: 2016-06-07 14:55:59 +0000
categories: ["nilm"]
permalink: /please_help_design_a_competition_for_energy_disaggregation
---
Has disaggregation accuracy improved since the 1980s? Which algorithms
are most accurate for a given use-case? Which (if any) use-cases are
well served by NILM already?

It's pretty much impossible to answer any of these questions with
confidence (unless you only consider the tiny number of algorithms for
which you have access to executable code). We can't directly compare
published results across papers because, when testing the disaggregation
accuracy of NILM algorithms, each paper uses different datasets,
different metrics, different pre-processing, etc.

This means that we can't measure progress over time. Nor can we decide
which NILM algorithms are most promising and which might be dead-ends.

These are bad problems. Let's work towards fixing them.

Some other machine learning communities have had great success running
yearly competitions. For example, the ImageNet "[Large Scale Visual
Recognition Challenge](http://www.image-net.org/challenges/LSVRC/)" has
been running yearly since 2010. Some regard this competition as having
played a crucial role in the recent dramatic increase in the accuracy of
image classification algorithms.

The idea of running a NILM competition has been rumbling around for
several years. But designing and implementing a NILM competition is
hard. The community uses sample rates ranging from monthly to MHz. No
single metric is informative for all use-cases. Collecting ground truth
data (the power demand of individual appliances) is expensive and
time-consuming.

Maybe we can pull this off. The first step is to decide on a design
which will work for everyone.

To give us something concrete to debate, we'll [outline one way this
could
work](https://docs.google.com/document/d/1CGoiNNkcnAFpo7Lci0Dv7AIliK3xz7Rjq_mBBh0WwrQ/edit).
This is not meant to be definitive! Think of this as the DNA for a
clumsy, inefficient animal 500 million years ago. Together, we need to
evolve this design into an elegant, efficient beast, well adapted to its
environment.

**Please shoot holes in this proposal! What won't work for you? What's
impractical? What's unfair? What opens the competition up to cheating?
How can we make the competition more attractive to researchers? How can
we make the competition more informative for the community? How can we
simplify the process?**

[The draft proposal is available on Google
Docs](https://docs.google.com/document/d/1CGoiNNkcnAFpo7Lci0Dv7AIliK3xz7Rjq_mBBh0WwrQ/edit).
I've linked to a Google Doc rather than copying-and-pasting the proposal
into this post so that we can update the proposal as the discussion
develops. Please add your comments either to [the mailing list
discussion](https://groups.google.com/forum/#!topic/energy-disaggregation/4I9rHMpkMTY);
or to the Google Doc (please sign your comment with your name; unless
you deliberately want to be anonymous); or if you want to keep your
comment private then [email me](http://jack-kelly.com/contact).

Thanks, (in no particular order) Jack, Mario, Oli, Stephen, Grant,
Marco, Peter <!--break-->

