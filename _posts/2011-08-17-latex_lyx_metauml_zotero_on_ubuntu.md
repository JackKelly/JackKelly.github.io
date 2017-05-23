---
title: "LaTeX, Lyx, MetaUML & Zotero on Ubuntu"
date: 2011-08-17 13:24:15 +0000
categories: ["LaTeX", "Lyx", "MetaUML", "Zotero", "bibliographies", "document authoring", "UML", "PhD"]
permalink: /latex_lyx_metauml_zotero_on_ubuntu
---
[Lyx](http://www.lyx.org/) is an open-source word processor built on top
of LaTeX and [Zotero](http://www.zotero.org/) is modern, open-source
bibliography management package with "cloud" features.
[MetaUML](http://metauml.sourceforge.net/) is a system for creating UML
diagrams in LaTeX (it's frankly pretty painful to use but it does
produce professional looking results). This post is where I keep my
notes about installing and configuring LaTeX, Lyx and Zotero on my
Ubuntu system at Imperial (where I do not have root access).

### Installation

#### Install TeX Live 2011

First, download and install [TeX Live](http://www.tug.org/texlive) 2011
(which includes LaTeX). Ubuntu 11.04 ships with TeX Live 2009 which
lacks several features I need (specifically for handling graphics and
graphs).

<li>
Download and unpack the [TeX Live
installer](http://www.tug.org/texlive/acquire-netinstall.html). Beware:
a full installation uses almost 3GBytes of disk space and takes a while
to download and install.

</li>
<li>
If, like me, you're installing on a university-supplied Ubuntu machine
to which you do not have root access then change the `TEXDIR` install
directory by pressing `D` on the first screen of the TeX Live
installation program to a directory to which you have write permissions.
I use `/data/usr/local/texlive/2011` as my `TEXDIR` on my Imperial
machine.

</li>
<li>
If you installed to a non-standard directory then you need to add that
directory to your path. If you're using the bash shell then add
`export PATH="$PATH:/install/directory"` to `~/.profile`. If you're
using csh then also add `setenv PATH "$PATH:/install/directory"` to your
`~/.cshrc`. For example, I use csh so I add
`setenv PATH "$PATH:/data/usr/local/texlive/2011/bin/x86_64-linux"` to
my `~/.cshrc` AND I also add
`export PATH=$PATH:/data/usr/local/texlive/2011/bin/x86_64-linux` to my
`~/.profile` file. If I modify `~/.cshrc` only then starting Lyx using
the `ALT-F2` does not load with the correct path settings (the path in
which I installed TeX Live 2011 and the path with the latest version of
Lyx must come before the other path variables).\

#### Install GNU aspell

If you have root permissions then just do
`sudo apt-get install libaspell-dev`. If you do not have root
permissions then:

1.  Download source from <http://aspell.net/>
2.  `./configure --prefix=/homes/dk3810/binaries && make -j9 && make install`

#### Install Lyx 2.0.2

Now download and install the latest version of Lyx.

1.  I have to install the binaries to a directory within my home
    directory because I do not have write access to /usr/bin so I
    run:`./configure --prefix=/homes/dk3810/binaries --with-extra-prefix=/homes/dk3810/binaries`
2.  `make -j8` (replace "8" with the number of CPU cores available)
3.  `make install`
4.  If you installed in a non-standard directory then add that directory
    to your path.

#### Install Zotero

Download and install from [Zotero's download
page](http://www.zotero.org/download/). I'm using 3.0 beta.

#### Install MetaUML

(after installing TeXlive 2011)\
In the install file, change the directory `TEXMF_HOME=/usr/share/texmf`
to `/usr/share/texmf-texlive` (or whatever your TeX Live install
directory is).

### Configuration

#### Lyx configuration

<ul>
<li>
Document &gt; Settings:

-   Bibliography
    -   Processor: bibtex8 (see Lyx manual sec 6.5)
-   PDF Properties
    -   Enable “Use hyperref support”
    -   Add a title and Author
    -   In the “Hyperlinks” tab:
        -   check “no frames around links”
        -   check “color links”
        -   enter
            `urlcolor=BlueViolet, citecolor=CadetBlue,linkcolor=black`
            into Additional Options
-   If using Document Class “book (KOMA-Script) then add
    `,usenames,dvipsnames` (with the leading comma) to “Document
    Class &gt; Class options: custom” else add
    `\usepackage[usenames,dvipsnames]{color}` to LateX Preamble. See
    LaTeX WikiBook for more info on
    [hyperlinks](http://en.wikibooks.org/wiki/LaTeX/Hyperlinks) and
    [colours](http://en.wikibooks.org/wiki/LaTeX/Colors).
-   Listings &gt; add `commentstyle={\color{blue}}` (or DarkOrchid) into
    the bottom box
-   Page Layout &gt; A4
-   Language
    -   English UK
    -   Encoding &gt; “Unicode (utf8)”
-   Output &gt; Default Output Format &gt; PDF (pdflatex)

</li>
<li>
Tools &gt; Preferences:

<ul>
<li>
Output &gt; Default Paper Size A4

</li>
<li>
Output &gt; LaTeX &gt; Uncheck “User LaTeX font encoding”

</li>
<li>
Editing &gt; Shortcuts:

</li>
-   Change bind file to emacs
-   Search for "view". Modify `buffer-view ps`. Delete the `ps` so the
    command is `buffer-view` and change the key binding to
    `Ctrl+Shift+X C`.
-   Search for "update". Modify `buffer-update ps`. Delete the `ps` so
    the command is `buffer-update` and change the key binding to
    `Ctrl+X C`.
-   Search for "buffer-write" (the command to save). Change keybinding
    to `Ctrl+X S`

</ul>
</li>
<li>
Tell Lyx to pass the `-shell-escape` parameter to `pdflatex`. Go to
Tools &gt; Preferences &gt; File Handling. Select "LaTeX (pdflatex)
-&gt; PDF (pdflatex)". Modify the "Converted:" field so it reads:
`pdflatex -shell-escape $$i` . Click "Modify" and "Save". [this forum
thread](http://tex.stackexchange.com/questions/16366/lyx-how-to-add-command-line-option-flag-for-latex-compiling)
gives more details.

</li>
</ul>
LaTeX preamble:\
` \usepackage{a4wide} \usepackage{graphicx} \usepackage{epstopdf} \usepackage[left=2.5cm,right=2cm,top=2cm,bottom=2cm]{geometry} % for dot2tex \usepackage{dot2texi} \usepackage{tikz} \usetikzlibrary{shapes,arrows} \usepackage[margin=10pt,font=small,labelfont=bf]{caption} \usepackage{textcomp} % For MetaUML: % The following is needed in order to make the code compatible % with both latex /dvips and pdflatex. \DeclareGraphicsRule{*}{mps}{*}{}`{language="latex"}

#### Zotero configuration

Preferences &gt; Export &gt; check “display character encoding on
export” and select “UTF8” in the drop -down list.

#### To enable URLs in references

Download and install [urlbst](http://purl.org/nxg/dist/urlbst). Then:

` cp urlbst ~/binaries/bin cp *.bst /data/usr/local/texlive/texmf-local/bibtex/bst/local/ texhash`{language="bash"}

(you'll have to use the correct directories for your setup).

#### To stop duplicated URLs in bibliography

Edit
`/home/USER/.mozilla/firefox/HEX.default/zotero/translators/BibTeX.js`\
Comment out this code around line 2099:

if(item.itemType == "webpage") {\
writeField("howpublished", item.url);\
}

#### To change the colour of the links (not requried if using Lyx)

` \usepackage{hyperref} % required to get URLs into references \hypersetup{citecolor=blue,urlcolor=blue}`{language="latex"}

<http://wiki.lyx.org/BibTeX/Tips>

### Use

#### Bibliography

1.  Export your bibliography from Zotero with Actions &gt; Export
    Library &gt; Format=BibTeX (do not export files). Save to file
2.  In Lyx: Insert &gt; List/TOC &gt; BibTeX Bibliography. Press
    "Add..." and then "Browse" and select your .bib database file.
3.  Now add individual references to your text with
    Insert &gt; Citation.

</li>


