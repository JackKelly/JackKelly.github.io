---
title: "Concrete example of floating point arithmetic behaving in unexpected ways"
date: 2012-04-04 08:20:38 +0000
categories: ["programming"]
permalink: /concrete_example_of_floating_point_arithmetic_behaving_in
---
I've heard lots of people say that it's best to use a floating point
number only when you really need to.  During my MSc we learnt about how
floating point numbers are encoded and did little pencil-and-paper
exercises to demonstrate how decimal fractions are converted into
surprisingly odd floating point representations.  I've read
about[computer arithmetic errors causing the failure of a patriot
missile](http://www.ima.umn.edu/~arnold/455.f96/disasters.html).  But
the following little problem that I've just bumped into seems to be a
very clean, concrete way to demonstrate that floating point numbers are
to be handled with care.   Here's the example... if I subtract 0.8 from
1, the remainder is 0.2, right?  So let's try asking Matlab or C++.  Try
evalating the following:

<span class="geshifilter">`(1 - 0.8) == 0.2`{.cpp
.geshifilter-cpp}</span>

This expression will return a boolean.  It's simply subtracting 0.8 from
1 and then asking if the answer is equal to 0.2.   Rather surprisingly,
it returns false.  Why?  Because 0.2 cannot be precisely represented in
binary floating point; the significand is 1100 recurring.  0.2 decimal =
3E4CCCCD in 32-bit floating point (hex representation). Now if we
convert from binary floating point back to decimal, we get: 3E4CCCCD
= 2.0000000298023223876953125E-1   (You can learn more about [floating
point
arithmetic](http://en.wikipedia.org/wiki/Floating_point#Floating-point_arithmetic_operations) on
WikiPedia and to tinker with this nifty [floating point converter
applet](http://www.h-schmidt.net/FloatApplet/IEEE754.html).)  The bottom
line is: if the quantity you're trying to represent *can* easily be
represented using integers, then it's probably best to do so.  e.g. if
you're trying to represent monetary values in C++, and you know you'll
only be interested in values of a specific precision (like 0.1 pence)
then you could build a simple Money class which internally represents
money as integers.

There's lots of good discussion (and links) of the limitations of
floating point
here: <http://en.wikipedia.org/wiki/Floating_point#Accuracy_problems>

**Update 18/6/2012**

I've just learnt that Python can cope with decimal numbers if you <span
class="geshifilter">`import decimal`{.text .geshifilter-text}</span>:

<span class="geshifilter">`1 - 0.8`{.text .geshifilter-text}</span>

<span class="geshifilter">`0.19999999999999996 `{.text
.geshifilter-text}</span>

<span class="geshifilter">`(1-0.8)==0.2 `{.text
.geshifilter-text}</span>

<span class="geshifilter">`False `{.text .geshifilter-text}</span>

<span class="geshifilter">`import decimal `{.text
.geshifilter-text}</span>

<span class="geshifilter">`1-0.8 `{.text .geshifilter-text}</span>

<span class="geshifilter">`0.2 `{.text .geshifilter-text}</span>

<span class="geshifilter">`(1-0.8)==0.2 `{.text
.geshifilter-text}</span>

<span class="geshifilter">`True`{.text .geshifilter-text}</span>

Update 21/11/2013

This is a good explanation of the "leakyness" of FP:[John D. Cook:
Floating point numbers are a leaky
abstraction](http://www.johndcook.com/blog/2009/04/06/numbers-are-a-leaky-abstraction/).

<!--break-->

