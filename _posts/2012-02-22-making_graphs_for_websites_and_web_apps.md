---
title: "Making graphs for websites and web apps"
date: 2012-02-22 10:34:25 +0000
categories: ["PhD", "web", "data visualisation"]
permalink: /making_graphs_for_websites_and_web_apps
---
I've been doing a little research into creating interactive graphs on
web pages.  Some quick notes from my research (this isn't meant to be an
exhaustive list by any means):

<!--break-->

### [d3.js](http://mbostock.github.com/d3/)

![](http://mbostock.github.com/d3/force.png)

-   Suggested by Aideen in the comments below.
-   Awesomely sexy.
-   Single framework which should work for graphing time series, showing
    the fit of model reconstructions to data timeseries, displaying and
    editing graphical models etc.
-   Is a "visualisation framework" rather than a graphing framework.
     Hence requires more code to produce simple graphs than "pure"
    graphing frameworks.  But is capable of gorgeous animations and,
    importantly for me, is capable of doing gorgeous things with
    graphical models.
-   Requires modern browser with SVG support.  Tested (and
    works) on IE9, Chromium 17, iPad 2 (animation a little sluggish),
    Firefox 3.6, 6 and 10 (animation can be a little sluggish in all
    FF versions).
-   Does not work on Android 2.1 browser or IE6 (because they don't
    support SVG)
-   There also exists a timerseries visualisation tool built on top of
    d3.js called [Cube](http://square.github.com/cube/).
-   [Here's an example line
    chart](http://natescodevault.com/2011/11/28/d3-js-data-visualizations/) and
    [a nice tutorial on making a line graph with
    d3](http://dealloc.me/2011/06/24/d3-is-not-a-graphing-library.html);
    and [lots of basic (but elegant), static charts done in
    d3](http://www.verisi.com/resources/d3-tutorial-basic-charts.htm).
-   Update 29/2/2012: d3 does look awesome.  However, you also have to
    write a *lot* of code to generate fairly simple line graphs, hence I
    may be going off d3 in favour of something
    like [Raphaël](http://raphaeljs.com/).  d3 appears to be able to
    do graphical models fairly simply though.
-   Update 13/3/2012: Back to d3!!! I tinkered with Raphael and it is
    lovely; but I found myself having to do some ugly hacks to get what
    I wanted.  d3, on the other hand, is enormously flexible.

### [Google Chart API](http://code.google.com/apis/chart/)

-   JavaScript
-   Works on IE6, 7 and 8 (I've just tested it)
-   Works on ipad
-   does not work on android 2.1 browser
-   Nice easy API
-   Free
-   Fairly fast, although there can be a noticable delay while the chart
    loads
-   Loads of options.
-   Can trigger events
-   Pachube already has some apps using Google Chart API

### [Highcharts JS](http://www.highcharts.com/products/highcharts)

-   JavaScript
-   Free for non-commercial use (but have to pay for commercial use)
-   Works on IE6 (I've just tested it)
-   works on iPad
-   Claims to work on Android 2.x browser (although it won't load on my
    android 2.1 phone)
-   Loads of options
-   Can trigger events

### [dygraphs](http://dygraphs.com/)

-   zoomable graphs of timeseries

### [Matplotlib](http://matplotlib.sourceforge.net/faq/howto_faq.html?highlight=web#matplotlib-in-a-web-application-server)

-   Matplotlib is a Python plotting framework (which is
    extrememly powerful)
-   It's possible to use Matplotlib to [create static PNG/SVG graphs in
    a web app
    context](http://matplotlib.sourceforge.net/faq/howto_faq.html?highlight=web#matplotlib-in-a-web-application-server)
-   There's an [HTML5 Canvas
    backend](http://code.google.com/p/mplh5canvas/) but it has very
    limited browser support
-   Some [notes from Johannes
    Sasongko](http://sjohannes.wordpress.com/2010/06/11/using-matplotlib-in-a-web-application/)

And here's a list of [5 JavaScript graph plotting
libraries](http://www.1stwebdesigner.com/css/top-jquery-chart-libraries-interactive-charts/).

I've started tinkering with the Google Chart API and it seems nice.

### Current conclusions

-   For plotting relatively simple graphs on my blog I'll probably use
    Google Graph API or export SVGs & PNGs from Matplotlib or gnuplot.
     Google Graph API is easy to use, free and supports most browsers.
-   For plotting graphs which might end up in a LaTeX document, I'll use
    gnuplot or Matplotlib or
    [matlabfrag](/notes_for_producing_clean_plots_in_matlab_for_latex)
-   For building my smart meter disaggregation system, I'll probably
    use d3.js.  It'll enable me to display and edit graphical models,
    display and interact with data, manually fit models to data by
    dragging with a mouse etc.


