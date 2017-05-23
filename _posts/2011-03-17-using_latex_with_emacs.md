---
title: "Using LaTeX with Emacs"
date: 2011-03-17 16:50:44 +0000
categories: ["LaTeX", "Emacs", "document authoring"]
permalink: /using_latex_with_emacs
---
### Makefile

<div class="geshifilter">

``` {.make .geshifilter-make style="font-family:monospace;"}
FILENAME = MyFile
 
$(FILENAME).pdf: $(FILENAME).tex
    make clean
    pdflatex $(FILENAME).tex
    bibtex $(FILENAME).aux
    pdflatex $(FILENAME).tex
    pdflatex $(FILENAME).tex
 
clean:
    rm -f $(FILENAME).aux $(FILENAME).bbl $(FILENAME).blg $(FILENAME).dvi $(FILENAME).log $(FILENAME).out
```

</div>

### Useful packages

<div class="geshifilter">

``` {.latex .geshifilter-latex style="font-family:monospace;"}
\documentclass[11pt,twoside,a4paper]{article}
\usepackage{a4wide} % make the page wider
\usepackage{listings} % for code listings
\usepackage{amsmath} % for overset{}{}
% \usepackage[tracking=alltext,letterspace=500]{microtype}
\usepackage[bookmarks,pdfdisplaydoctitle,colorlinks,
 pdfauthor={Daniel Kelly},
 pdftitle={DB Coursework 1}]{hyperref}
\lstset{
language=SQL,
basicstyle=\small\sffamily,  %\ttfamily,%\small\sffamily,
%\SetTracking[spacing={600*,-100*,}]{encoding=*}{160},  \scriptsize,
%\bfseries, \sffamily, \footnotesize
% keywordstyle=\sffamily,
frame=tblr,
xleftmargin=3em}
```

</div>

