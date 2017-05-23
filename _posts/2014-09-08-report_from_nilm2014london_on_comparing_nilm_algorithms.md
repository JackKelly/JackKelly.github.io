---
title: "Report from NILM2014@London on comparing NILM algorithms"
date: 2014-09-08 16:02:59 +0000
categories: ["PhD", "nilm"]
permalink: /report_from_nilm2014london_on_comparing_nilm_algorithms
---
The first "[NILM in
London](http://blog.oliverparson.co.uk/2014/09/post-nilm-2014-london.html)"
workshop was held on Wednesday 3rd September. In this blog post, I'd
like to try to summarise the discussion around comparing NILM
algorithms.

<!--break-->

At present, it is very hard (if not impossible) to objectively compare
any two NILM algorithms. This is true for both academia and industry.
The problem is that each research paper tends to use a different
dataset, different metrics, different appliances etc. The situation
improved considerably in 2011 with the release of the [REDD
dataset](http://redd.csail.mit.edu). But we are still some distance from
being able to directly compare the performance of any pair of NILM
algorithms.

[Oli Parson](http://blog.oliverparson.co.uk/) lead a brief session on
NILM evaluation. He presented a great summary of the [Belkin Energy
Disaggregation competition on
Kaggle](https://www.kaggle.com/c/belkin-energy-disaggregation-competition).

Several points were raised during the discussion:

-   Dominik Egarter raised the point: How do we compare NILM algorithms
    with fundamentally different assumptions and inputs? For example,
    say algorithm A requires that the use list every appliance in the
    home but algorithm B requires no information from the user.
    Algorithm A gives an accuracy of 85% whilst algorithm B gives an
    accuracy of 75% percent. Which is better? Should the algorithm which
    requires more information be penalised in some way? Is it even fair
    to directly compare them? Should we define a set of 'NILM algorithm
    classes' and only compare algorithms within their own class? We
    could come up with a set of 'NILM algorithm classes' by considering
    specific scenarios and use-cases. For example, most domestic users
    probably won't be bothered to enumerate every appliance in their
    home, so we could have a 'zero user input' class (which does not
    necessarily mean 'unsupervised' in the machine learning sense
    because the system could access generic appliance models trained
    from, say, the public datasets).

-   Companies offering NILM are focussed on offering a NILM service
    which is satisfies their particular users' needs. They might see
    very little value in having a global 'leader board' of performance.
    For example, when you hire a builder to modify your house, you don't
    consult some regional league table of builders. Instead you find the
    local builder who can offer you everything you need, and you really
    don't care if they are a few percentage points behind some other
    local builders on some particular metric.

-   Which metric(s) to use to compare NILM algorithms? We probably need
    to use multiple metrics

-   Do we need to spend lots of money collecting a 'validation dataset'.
    The idea being that, if we are trying to validate commercial NILM
    services, then we probably need to keep the test data private (so
    people don't cheat!) But collecting a large dataset is
    very expensive. If companies are not interested in a 3rd party NILM
    validation tool then perhaps we do not need to bother to collect a
    new dataset. Instead, if only academics are interested in competing
    on a public 'leader board' then we probably don't need a private
    dataset, especially if academics are encouraged to release
    their code. Computer Vision competitions like the [ImageNet Large
    Scale Visual Recognition
    Challenge](http://www.image-net.org/challenges/LSVRC/) use public
    data (I think).

-   However, companies might well be interested in privately assessing
    how well their algorithms perform relative to some benchmark (and/or
    the academic state of the art).

-   In terms of 'benchmarks', it might be nice to explore how each
    metric responds to 'naive' approaches. e.g. some metrics will give
    surprisingly high 'marks' if you just predict that all appliances
    are 'off' all the time! Or using simple 'simulation' using just
    probability density functions of each appliance for each time
    of day.

(I didn't take notes at the meeting so I have probably forgotten some
points. Please add anything I've missed / garbled to the comments!)

