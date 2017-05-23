---
title: "HTML5 Canvas versus SVG for interactive charts and graphical models"
date: 2012-02-28 14:10:40 +0000
categories: ["PhD", "graphical models", "graphs"]
permalink: /html5_canvas_versus_svg_for_interactive_charts_and_graphical
---
Some links and notes:

<!--break-->

-   [sitepoint: Canvas vs SVG: How to Choose the Right
    Format](http://www.sitepoint.com/canvas-vs-svg-how-to-choose/)
-   [MSDN Blogs &gt; IEBlog&gt; Thoughts on when to use Canvas and
    SVG](http://blogs.msdn.com/b/ie/archive/2011/04/22/thoughts-on-when-to-use-canvas-and-svg.aspx)
-   [dev.opera.org: SVG or Canvas? Choosting between the
    two](http://dev.opera.com/articles/view/svg-or-canvas-choosing-between-the-two/)
-   [Graphic JavaScript Tree with
    Layout](http://www.codeproject.com/Articles/16192/Graphic-JavaScript-Tree-with-Layout)
    (implements layout algorithm from scratch)
-   [Sencha Touch
    Charts](http://www.sencha.com/blog/introducing-sencha-touch-charts/)
    describing why they went with Canvas not SVG
-   stackoverflow posts:
    -   [What is the difference between SVG and HTML5
        Canvas?](http://stackoverflow.com/questions/4996374/what-is-the-difference-between-svg-and-html5-canvas)
    -   [HTML5 Canvas vs SVG vs
        div](http://stackoverflow.com/questions/5882716/html5-canvas-vs-svg-vs-div)
    -   [Suggestions: Canvas or
        SVG?](http://stackoverflow.com/questions/8573460/suggestions-canvas-or-svg)
    -   [Interactive directed graphs with SVG and
        Javascript](http://stackoverflow.com/questions/7450501/interactive-directed-graphs-with-svg-and-javascript)
    -   [Why do we need the HTML5 Canvas element when the same can be
        achieved through
        SVG?](http://stackoverflow.com/questions/1650415/html5-canvas-element-and-svg)
    -   [Library for Canvas / SVG web-based tree graphs with layout
        algorithm?](http://stackoverflow.com/questions/6337841/library-for-canvas-svg-web-based-tree-graphs-with-layout-algorithm)
    -   [JavaScript charting
        library?](http://stackoverflow.com/questions/119969/javascript-chart-library) -
        recommends SVG over Canvas; and Raphael
    -   [jQuery SVG vs.
        Raphael](http://stackoverflow.com/questions/588718/jquery-svg-vs-raphael) -
        vast majority of support is for Raphael

### Toolkits and Frameworks

-   [JavaScript InfoVis Toolkit](http://thejit.org/)
-   [Paper.js](http://paperjs.org/about/) - Vector Graphics Scripting
    based on Canvas
-   [Raphaël](http://raphaeljs.com/) - based on SVG.  Links to tutorials
    in [this SO
    thread](http://stackoverflow.com/questions/1571016/raphael-js-tutorial).
     Makes animation and interaction easy.  Good support.  MIT License.
     [Draggable graphical model is one of the
    examples](http://raphaeljs.com/graffle.html).  Also see [this SO
    post](http://stackoverflow.com/questions/5659899/raphael-pie-chart-putting-dynamic-data)on
    using dynamic data with Raphael. Some libraries built on Raphaël:
    -   [gRaphaël](http://g.raphaeljs.com/) - charting library
        (apparently no docs though)
    -   [Morris.js](http://oesmith.github.com/morris.js/#examples) -
        timeseries library
    -   [Ico](https://github.com/uiteoi/ico) - an API to create complex
        charts; name-drops [Edward
        Tufte](http://en.wikipedia.org/wiki/Edward_Tufte). A fork
        = [Grafico](http://grafico.kilianvalkhof.com/)
    -   [Dracular](http://www.graphdracula.net/) - framework for
        displaying interactive graphical models.
-   [Really good comparison between Raphaël, Paper.js and
    Processing](http://coding.smashingmagazine.com/2012/02/22/web-drawing-throwdown-paper-processing-raphael/)
-   [ExtJS](http://www.sencha.com/products/extjs/): very, very powerful
    JavaScript framework for building web app UIs; with a good charting
    module
-   Dojo (another powerful JavaScript web app framework) has
    <http://livedocs.dojotoolkit.org/dojox/charting>dojox.charting

### Tutorials and demos

-   [HTML5 graph slider using canvas and
    jQuery](http://www.anxioussilence.co.uk/blog/2010/04/27/html-5-graph-slider/)
-   [2D function glotter using
    canvas](http://www.snappymaria.com/canvas/FunctionPlotter.html)
    (full screen; zoom and pan)
-   [HTML5 Canvas Graphic Solutions every web developer must
    know](http://webdesigneraid.com/html5-canvas-graphing-solutions-every-web-developers-must-know/)

### Current conclusions

I should use Raphaël and one of its graphing add-ons.  I need to do more
than just plot a standard line chart; I want lots of interaction.

Canvas is a lower level graphics API than SVG.  Canvas thinks in terms
of individual pixels whilst SVG thinks in terms of vector objects.
 Canvas is good for high performance 2D graphics like games; but SVG is
good for applications which draw objects like boxes, lines etc.  My only
slight concern about using SVG is that  I may run into performance
issues if I want to build a full-screen waveform viewer.
 Also,pre-Honeycomb Android doesn't support SVG (but does support
Canvas).  But I don't care about pre-Honeycomb Android for my specific
application.

<!--break-->

