---
title: "Which software license for disaggregation code?"
date: 2013-07-31 14:28:48 +0000
categories: ["PhD", "disaggregation", "licenses"]
permalink: /which_software_license_for_disaggregation_code
---
I have finally started writing my smart meter disaggregation code! I'll
keep the code private until we publish a paper on our disaggregation
system, and then I'll open up the repository on github.

I spent a while worrying about which software license to use. I've just
finished reading "[Free as in Freedom: Richard Stallman's Crusade for
Free
Software](http://www.amazon.co.uk/gp/product/B006GCNP5S/ref=oh_d__o05_details_o05__i00?ie=UTF8&psc=1)"
so I was very tempted to use
[GPL](http://choosealicense.com/licenses/gpl-v2/). The GPL forces people
who modify your code to release their modifications in the hopes that
everyone can benefit from every improvement. This has worked very well
for projects like the Linux kernel; but there does seem to be good
evidence that some software companies and developers are "allergic" to
the GPL because it limits their freedom to modify the code, hence some
companies would rather re-write GPL'd code or go with an alternative
project.

One of my main motivations for doing a PhD on smart meter disaggregation
is the rather idealistic hope that my work might, in some very small
way, *help people to reduce their energy consumption*. As such, the
priority must be to allow as many people as possible to use any
disaggregation software I write. So I've gone for a very simple and
permissive license: [the MIT
license](http://choosealicense.com/licenses/mit/).

(Of course, I rather suspect that my code won't be used much, so all
this worrying about licenses might be somewhat premature ... but it's
worth getting it right from the start).

I considered a number of different names for my Python disaggregation
code: nilmpy, pynilm, nilmtk, disaggpy. I went with "slicedpy" because
it makes me smile ;) (the idea being that smart meter disaggregation is
a little like taking a pie (representing your whole-home energy
consumption) and slicing it into its component pieces (each representing
the energy consumed by an individual appliance); hence the name
"SlicedPy". It's spelt "py" not "pie" because the code is mostly written
in Python).

Update 1/8/2013
---------------

[@OpenTRV](https://twitter.com/OpenTRV) suggested [that I
use](https://twitter.com/OpenTRV/status/362890261908566019) the [Apache
v2.0](http://choosealicense.com/licenses/apache/) software license
because it has some patent protection. It won't protect against patent
trolls but it seems better than no patent protection. I am now using the
Apache v2.0 license.

Useful links
------------

-   [ChooseALicense.com](http://choosealicense.com/)
-   [Long discussion on slashdot about GPL vs other open source
    license](http://developers.slashdot.org/story/13/04/18/1550246/most-projects-on-github-arent-open-source-licensed)
-   [Licensing of Software on Github: A Quantitative
    Analysis](http://www.softwarefreedom.org/resources/2013/lcs-slides-aaronw/#/begin)
-   [An Introduction to Modern Open Source Licence Patent
    Clauses](http://blog.gerv.net/2013/02/an-introduction-to-modern-open-source-licence-patent-clauses/)
-   [Frequently used OSI approved
    Licenses](http://www.osscc.net/en/licenses.html) <!--break-->


