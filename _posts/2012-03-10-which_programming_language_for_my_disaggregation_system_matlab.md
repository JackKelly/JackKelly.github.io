---
title: "Which programming language for my Disaggregation system? Matlab versus Python; Graphical Models."
date: 2012-03-10 17:20:52 +0000
categories: ["PhD", "MATLAB", "python", "C++", "JavaScript", "HTML5", "SVG", "programming"]
permalink: /which_programming_language_for_my_disaggregation_system_matlab
---
Over the course of my PhD, I intend to write a smart meter
disaggregation system.  Maybe this system will end up as a web service;
maybe not.  At the very least, it will need to play nicely with existing
web services like [Pachube](http://pachube.com).  I've been wondering
which language(s) I should use to build my system.  My current answer to
this question is to write a complete prototype of the "backend" in
Python, with the front-end written in JavaScript, HTML5 and SVG.  It's
likely that parts of the "backend" will run rather slowly in Python; but
luckily it's easy to get Python to play well with C++ code, so I'd plan
to re-write computationally intensive sections in C++.

My initial plan was to use Matlab.  But after writing several thousand
lines of Matlab, I couldn't help but feel uncomfortable with it.  There
are some seriously ugly bits of the language; and in general it has a
rather "hacked together" feel to it.  It turns out I'm not the only one
who feels uncomfortable with Matlab: there's a blog called "[Abandon
MATLAB](http://abandonmatlab.wordpress.com/)" with [gems
like](http://abandonmatlab.wordpress.com/2012/03/07/youre-fixing-the-wrong-thing-4-2/) "*\[Mathworks\]
even updated the docs for “getframe” to clarify that you need to turn
off the fucking screen saver and walk away from the computer like it’s
1992.*".  One especially interesting post in "Abandon MATLAB" links to
the [results of a survey which compares attitudes to MATLAB to attitudes
to Python](http://hammerprinciple.com/therighttool/items/matlab/python).
 Basically, I feel content that I wasn't completely crazy to abandon
Matlab in favor of Python and C++.  I'll admit that I'm struggling a bit
to wrap my head around JavaScript but I'm getting there with the help of
Douglas Crockford's excellent book "[JavaScript: The Good
Parts](http://www.amazon.co.uk/JavaScript-Good-Parts-Douglas-Crockford/dp/0596517742)".

<!--break-->

###  

### Early conclusions regarding implementing PGMs

I think I should go ahead an prototype the backend of my system in
Python, even though there aren't many PGM frameworks for Python.  Python
does have good support for general graphical models.  I can always jump
over to C++(11) for the PGM stuff.  Plus I'm not sure yet that I will be
using "textbook" PGM approaches; I might build my own algorithms based
on "normal" graphical models.  Also of interest, the "[Why Matlab" wiki
page](http://code.google.com/p/pmtk3/wiki/WhyMatlab) for the
Probabilistic Modeling Toolkit states "*In the future we may port to
python. This seems to be growing in popularity within the machine
learning community.*"

[Thesaurus of Mathematical
Languages](http://mathesaurus.sourceforge.net/), which has guides for
translating between Matlab, NumPy and R.

### Update 1/4/2012

OK.  I've gone back to prototyping in Matlab.  The programming
assignments for the Stanford Probabilistic Graphical Models course are
done in Matlab (or Octave) and I'm slowly learning to appreciate Matlab.
 There are some language features which I still find very frustrating
(like not having much control over whether objects are passed by
reference or value into functions; and no proper list data structure)
but it is fast to develop in.

### Update 18/6/2012

For a bunch of reasons, I'm seriously thinking of moving away from
MATLAB to Python + NumPy + matplotlib.  Some pros and cons of the main
languages I'm considering are below:

#### Portability

-   Python should work "out of the box" on Windows, Linux or Mac
-   C++ needs, at the very least, to be re-compiled
-   MATLAB should be pretty portable

#### Processing speed

-   C++ is almost always the fastest, not least because it allows access
    to SIMD and GPU instructions
-   Python can by fast if used with PyPy, NumPy etc (and, of course, can
    use C++ code)
-   MATLAB is fast for a few things but is remarkably slow for loops,
    recursion, OOP and a bunch of other things

#### Tinkering with data during development

-   This is probably where MATLAB excels, although its graphing system
    is far from perfect
-   Python with matplotlib should allow for easy tinkering
-   C++ I'd have to dump data out to gnuplot (as I did for my
    MSc project) or something similar

#### Maintaining a large code base

-   C++ and Python are both great for building large apps
-   MATLAB isn't so good (no namespace; the editor lacks many features
    found in Eclipse like refactoring aids; editor lacks support for
    git; writing unit tests for MATLAB code isn't as easy as it
    should be)

#### Accessability for other developers

-   If I want hobbiests to be able to use and/or modify the system then
    MATLAB is not an option
-   Python is probably better understood by the "hobbiest" community
    than C++
-   But MATLAB seems to be in vogue for academic NILM research

#### GUI development

-   This is probably an area where Python excels.  (Yes, you can build
    GUIs in MATLAB and C++ but it's probably least painful in Python)
-   If I did go with a pure C++ implementation then maybe wxWigets in
    combination with [gpPanel](http://code.google.com/p/gppanel/) would
    be a good strategy

#### Graphical models

##### Python

See "[stackoverflow: Python Graph
Library](http://stackoverflow.com/questions/606516/python-graph-library)".
 [graph-tool](http://projects.skewed.de/graph-tool/) gets some love;
it's is an efficient python module based heavily on the Boost Graph
Library, hence might be a good bet given my experience with the BGL for
my MSc project.  There are others which may be more focussed on
probabilistic graphical models;
like [gPy](http://www-users.cs.york.ac.uk/jc/teaching/agm/gPy/).
 [NetworkX](http://networkx.lanl.gov/index.html) also looks very
attractive and was praised at PyCon2012.

Also, [this "Could anybody recommend a graphical model implementation in
Python"
thread](http://www.reddit.com/r/Python/comments/iq0vv/could_anybody_recommend_a_graphical_model/)
is very useful. Amongst other things, it lists
 [PyMC](http://pymc-devs.github.com/pymc/README.html) which "*is a
python module that implements Bayesian statistical models and fitting
algorithms, including Markov chain Monte Carlo. Its flexibility and
extensibility make it applicable to a large suite of problems. Along
with core sampling functionality, PyMC includes methods for summarizing
output, plotting, goodness-of-fit and convergence diagnostics.*"

Also see this blog post "[Bayes net by example using Python and Khan
Academy
Data](http://derandomized.com/post/20009997725/bayes-net-example-with-python-and-khanacademy)".

##### Probabilistic Graphical Modelling frameworks in C++, Java, R and Matlab

There's [an extensive list of PGM frameworks
here](http://www.cs.ubc.ca/~murphyk/Software/bnsoft.html) written
by [Kevin P Murphy](http://www.cs.ubc.ca/~murphyk/) (who's one of the
major committers to the [Matlab Bayes Net
Toolbox](http://code.google.com/p/bnt/) and the [Probabilistic Modelling
Toolkit](http://code.google.com/p/pmtk3/) amongst [many other
things](http://www.cs.ubc.ca/~murphyk/Software/index.html); and is also
co-teaching the [Stanford Probabilistic Graphical Models course in
Spring 2012](/free_stanford_course_on_probabilistic_graphical_models);
and he has a very interesting-looking book called "[Machine Learning: a
Probabilistic Perspective](http://people.cs.ubc.ca/~murphyk/MLbook/)"
coming out in August 2012) .  The breakdown by language:

-   13 in Java
-   10 in C++
-   5 in Matlab
-   3 in R
-   1 in Python

Of some interest: the [FastInf C++
library](http://compbio.cs.huji.ac.il/FastInf/fastInf/FastInf_Homepage.html) was
developed in the labs of Prof Friedman and Prof Daphne Koller (who
together wrote the "Probabilistic Graphical Models" book I'm reading;
and Koller is giving [a free online course on Probabilistic Graphical
Models from
Stanford](/free_stanford_course_on_probabilistic_graphical_models)).

### Update 20/6/2012

My current plan is starting to look something like this:

-   prototype in Python with NumPy, matlplotlib and wxPython
-   re-write slow bits of code in C++ (see [this StackOverflow
    thread](http://stackoverflow.com/questions/276761/exposing-a-c-api-to-python)
    discussing tools for writing C++ APIs for Python; looks like I
    should probably start with manual wrapping)
-   I'm really having to fight the urge to write my whole thing in C++.
     

I've just done a very quick benchmark on a bit of code to identify
"steady steates" (as defined by Hart 1992).  The test was run on a
dataset with 139,000 samples.  The benchmark included loading the file
from disk.  The results (in seconds):

-   MATLAB 2012a = 0.143
-   Python 2.7.3 = 0.140
-   PyPy = 0.119
-   C++ (g++ 4.6.3, no optimisation) = 0.040
-   C++ (g++ 4.6.3, -O3) = 0.030

So MATLAB and Python are neck-and-neck at 3.5 times slower than C++.
 I'm quite surprised the difference wasn't much larger given that this
test runs a for loop, and MATLAB is notoriously slow at for loops.

