---
title: "Getting LaTeX and Lyx to use ACM SIG class file"
date: 2012-04-19 13:30:27 +0000
categories: ["LaTeX", "Lyx", "conferences", "PhD"]
permalink: /getting_latex_and_lyx_to_use_acm_sig_class_file
---
Installing the ACM SIG LaTeX class file on Ubuntu using tex-live2011 and
using it in Lyx.

First, download the ACM class file and let LaTeX know about it (modified
from [Ubuntu
wiki](https://help.ubuntu.com/community/LaTeX#User_install)):

<div class="geshifilter">

``` {.bash .geshifilter-bash style="font-family:monospace;"}
mkdir -p ~/texmf/tex/latex/sig-alternate/
cd ~/texmf/tex/latex/sig-alternate/
wget http://www.acm.org/sigs/publications/sig-alternate.cls
texhash ~/texmf
```

</div>

Check that it's installed correctly by running something like:

<div class="geshifilter">

``` {.bash .geshifilter-bash style="font-family:monospace;"}
cd ~kpsewhich sig-alternate.cls
```

</div>

More info [about the ACM SIG class file is available on the ACM
website](http://www.acm.org/sigs/publications/proceedings-templates#aL2).

Now we have to tell Lyx to play nicely.  First download my
[sig-alternate.layout](https://raw.github.com/JackKelly/LaTeX/master/Lyx/sig-alternate.layout)
file and place it in \~/.lyx/layouts.  Fire up Lyx.  Go to Tools &gt;
Reconfigure.  Quit Lyx.  Restart Lyx.  Start a new file.  Go to Document
&gt; Settings &gt; Document class &gt; Local Layout and select
\~/.lyx/layouts/sig-alternate.layout. (please note that I've given up
trying to use Lyx to write ACM SIG papers; instead I've gone back to
using Emacs and LaTeX directly; I don't think my .layout file works
correctly.  I'd recommend [Googling for
"sig-alternate.layout"](https://www.google.co.uk/search?ie=UTF-8&q=%22sig-alternate.layout%22))

Be sure to read the [ACM's Authors
Guide](http://www.acm.org/sigs/publications/sig-alternate-v1.1)!

### bst files

Save your .bst file somewhere in your home directory, say <span
class="geshifilter">`~/texmf/tex/bibtex.`{.text
.geshifilter-text}</span>  Now run <span
class="geshifilter">`locate abbrv.bst`{.text .geshifilter-text}</span>
to find the directory where most of your bst files are installed; for me
most of my bst files are stored
in /usr/local/texlive/2011/texmf-dist/bibtex/bst/

We now have to set the BSTINPUTS environment variable to include both
your custom path and the path where most bst files are stored.

I edited <span class="geshifilter">`~/.bashrc`{.text
.geshifilter-text}</span> and added <span
class="geshifilter">`export BSTINPUTS=/usr/local/texlive/2011/texmf-dist/bibtex/bst//:/home/jack/texmf/tex/bibtex//`{.text
.geshifilter-text}</span>

(The <span class="geshifilter">`//`{.text .geshifilter-text}</span> at
the end of each path says "*search this path and all subdirectories*")

