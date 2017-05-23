---
title: "UK Patents, Copyright and disaggregation"
date: 2013-07-01 15:04:57 +0000
categories: ["PhD", "disaggregation", "patents"]
permalink: /uk_patents_copyright_and_disaggregation
---
During my PhD one key aim is to design, implement and validate a
software system which can disaggregate a smart meter signal.
Disaggregation is definitely something which has commercial potential.
Several people who have told me: "make sure you protect your IP".

I am rather sceptical of the worth of patents in general and software
patents in particular but I also appreciate that I don't know much about
IP. To try to find out more, I just attended a lecture on "Intellectual
Property and its Importance to Researchers". In particular, I want to
figure out:

-   Is it *desirable* to protect a disaggregation system?
-   Is it *possible* to protect a disaggregation system?

Let's take these questions in reverse order: <!--break-->

Is it possible to protect the IP of a disaggregation system in the UK?
----------------------------------------------------------------------

"IP" is an umbrella term for several distinct concepts:

-   Copyright
-   Patents
-   Secret "know-how"
-   Design rights
-   Trade marks

Software can be protected by copyright. But copyright just protects
against the literal copying of the program; copyright doesn't protect
the *ideas* implemented in the software. In order to protect the ideas,
you need a patent.

In the UK, it appears that software *can* be patented but *only if it
has a "technical effect"*. The following example was given in the
lecture: the software running on a car engine's Electronic Control Unit
(ECU) *is* patentable because it has the "technical effect" of
controlling the engine. On the other hand, a word processor is not
patentable because it does not produce a technical effect.

What counts as a "technical effect"? "Technical" can't just be a synonym
for "physical", can it? *All software* necessarily produces a *physical*
effect: the software stack that I'm currently using to write this blog
post busily switches the alignment of liquid crystals in my display as
well as, of course, changing the state of billions of transistors; the
magnetisation of my hard disk; the charge carried in my network cable;
the power consumed from the wall socket etc etc. All computers are
physical objects; and all running software modifies the state of
computers; therefore all running software produces physical effects. Why
are these effects any less "technical" than changing the amount of
petrol injected into an engine's cylinder?

[Wikipedia suggests
that](http://en.wikipedia.org/wiki/Software_patents_under_the_European_Patent_Convention)
a technical effect "*goes beyond the normal physical interaction between
the program and the computer*". OK. That sounds reasonably clear. But
then the waters become muddied again by a subsequent paragraph:
"*According to the jurisprudence of the Boards of Appeal of the EPO, a
technical effect provided by a computer program can be, for example, a
reduced memory access time, a better control of a robotic arm or an
improved reception and/or decoding of a radio signal. It does not have
to be external to the computer on which the program is run; reduced hard
disk access time or an enhanced user interface could also be a technical
effect.*"

So, to be honest, I don't understand if a pure-software disaggregation
system could be patented or not. Disaggregation shares little in common
with a car engine's ECU, which suggests that disaggregation can't be
patented. But disaggregation has quite a lot in common with decoding a
radio signal (e.g. [one can interpret turbo codes from a machine
learning
perspective](http://en.wikipedia.org/wiki/Turbo_code#Bayesian_formulation)),
which suggests that disaggregation can be patented.

There certainly are a fair few patents currently pending in the UK which
do discuss disaggregation. But, as far as I can tell, these patents
involve some hardware; I don't think they are pure-software solutions
(although I'm not totally confident about this assertion). And, of
course, [George Hart patented his disaggregation
approach](http://www.google.co.uk/patents/US4858141), but that was in
the US and his patent had a significant hardware component, IIRC.

Taking out a patent on your work doesn't prevent you from publishing.
But if you want patent protection then you have to apply for the patent
prior to publishing.

Do I *want* to patent my disaggregation system (assuming it works)?
-------------------------------------------------------------------

One of my ultimate aims for my PhD is to help reduce energy consumption
for as many people as possible. I'm also very keen that disaggregation
be made freely available to individuals rather than just to large energy
companies.

In general, I'm rather uncomfortable with anything which limits
competition. (Just to be clear: I'm definitely not a free-market
economic libertarian; I strongly believe that regulations are required
to create an ethical economic system because the basic free-market
objective to minimise economic cost bares little relation to maximising
societal "good" (I'm deliberately being vague about what "societal good"
means because we're already way off topic here!)). I take the view that
an important reason why capitalism is the least worst of all economic
models is because it forces companies to evolve. Competition is
essential to evolution. Patents, it seems to me, unquestionably limit
competition. Inhibiting competition is basically the primary aim of the
patent system. (Proponents of patents would probably argue that patents
limit *unfair* competition but, still, that's limiting competition.
Biological evolution doesn't distinguish between "fair" and "unfair"
competition.)

Creeping even further up my own arse:

Why are humans so successful as a species? Surely our ability to
disperse ideas rapidly and effectively is key to our success. Think
agriculture, cooking, house building, field irrigation, the scientific
method etc etc. Patents *explicitly try to retard the wide dispersal of
ideas*. (Yes, patents are nominally a contract whereby the inventor gets
protection from the state in return for disclosing their ideas to the
public but what good is the information in the patent if you can't act
on it?! And, of course, patents are deliberately written to obscure as
much implementation detail as possible so patents are pretty useless as
"how-to" documents.)

Let's get a little more concrete:

Say that Jim invents a useful bit of software. Jim does this on his own,
without stealing key ideas from someone else. Lots of people start using
Jim's code. A year later, some company (let's call it Ptroll Ltd) tries
to take Jim to court for infringing their patent. Jim didn't steal
anything from Ptroll Ltd. Why is it Jim's problem that Ptroll Ltd
invested loads of cash in R&D and lawyers' fees for something that Jim
built in his bedroom? Jim doesn't "owe" Ptroll Ltd anything. If Ptroll
Ltd didn't exist then Jim would have still invented his system. By
taking Jim's product "off the shelves", users are undeniably worse off.
As is Jim. As are future innovators working in the same space. *The
only* group of individuals who benefit are Ptroll and the lawyers. In
what way does that maximise societal good? Jim's only crime was that he
produced a system which *competes* with Ptroll's.

Ok, that's a rather extreme example. Here's a less extreme example:

Ada uses a software product. She thinks it sucks. From scratch, she
writes a better version, implementing a superset of the features in the
first software product. Users benefit. Ada benefits. Future innovators
benefit. Of course, this does happen a lot already; but my point is that
software patents seem to explicitly try to prevent this scenario, and
that feels utterly unfair to me. If someone can figure out a better way
of doing something; they should be free to create and distribute that
system. Tough cookies if you spent loads of cash producing an inferior
product. Maybe spend more time and money on development and less on
lawyers.

I accept that patents are vital for some things like big pharma. It
might cost £500M to develop a drug but only 1p to manufacture each pill.
The pharma companies would never invest that £500M if a generics company
could reverse-engineer the drug (hence benefiting from £500M of R&D they
didn't pay for) and sell it for a fraction of the price. But software is
fundamentally different to big pharma (not least because implementation
is often at least as important as the initial idea. Why did Facebook
wipe the floor with MySpace?)

Anyway... this is quickly getting into a long rant. We haven't even
touched on the entirely arbitrary concept of "non-obviousness"
(non-obvious to whom?) or "novelty" (every invention builds on prior
ideas). Let's just say that I have a lot of respect for folks like
[Richard Stallman](https://en.wikipedia.org/wiki/Richard_Stallman) and
[Donald Knuth](http://en.wikipedia.org/wiki/Donald_Knuth) and I'm yet to
be convinced that software patents have any societal value at all (feel
free to try to convince me!)

In the specific case of disaggregation... if I'm successful in producing
a state-of-the-art disaggregation system then I want as many people to
use that system as possible (because I'm an environmentalist in computer
scientists' clothing). That aim seems incompatible with taking out a
patent (and it's not even clear if I *could* take out a patent even if I
wanted to). So the bottom line is that I still plan to open-source my
code under a permissive license like the MIT license.

Of course, I'm fully aware that, as a PhD student whose income is
completely independent from how marketable my code is, I might have a
rather distorted view of the patent system. Maybe if I go into industry
after my PhD then my views may change substantially ;)

