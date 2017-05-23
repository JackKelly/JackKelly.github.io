---
title: "Convert Reveal.js + D3 to PDF"
date: 2015-11-11 19:38:17 +0000
categories: ["imagemagick", "pdf", "reveal", "d3"]
permalink: /convert_revealjs_d3_to_pdf
---
The last two presentations I've given have been created using
[reveal.js](https://github.com/hakimel/reveal.js/) and
[d3.js](http://d3js.org/). This combination of technologies allows for
some nice data-driven animation. For example, my BuildSys presentation
on Neural NILM is available to view
[here](http://jackkelly.github.io/BuildSys_2015_NeuralNILM) and the
source code is
[here](https://github.com/JackKelly/BuildSys_2015_NeuralNILM). I was
honoured to learn that my BuildSys presentation won joint best
presentation!

The challenge comes when we want to convert these presentations to PDF.
Reveal does have a [PDF
export](https://github.com/hakimel/reveal.js#pdf-export) feature but it
didn't seem to work well for me for the D3 animation slides. So here's
my hacky solution on Ubuntu 15.04:

1.  Set the monitor resolution to 1024x768 (the resolution I designed
    the slides for)
2.  Set the browser to full-screen.
3.  Print-screen each slide (after the animation has completed) using
    alt-printscreen (with the browser selected).
4.  Convert to postscript using imagemagik:
    `convert -level 0%,100%,1.0 -quality 100% *.png presentation.ps`. I
    tried converting directly to PDF using imagemagik but it kept trying
    to squash the grey background to black on some slides, which really
    messed things up. I tried tinkering with imagemagick parameters such
    as
    `level, quality, background, black-threshold, white-threshold, linear-stretch, contrast-stretch, black-threshold, black-point-compensation`
    but I couldn't get imagemagick to output a sensible PDF. But it
    would output a pretty sensible postscript file.
5.  Convert ps to pdf using this command:
    `gs -o presentation.pdf -sDEVICE=pdfwrite -g1024x768 -dPDFFitPage -r72 -dPDFSETTINGS=/printer presentation.ps`

I expect there is a better solution! Let me know if you know of a better
solution, please!

