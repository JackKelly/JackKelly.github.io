---
title: "Setting up Emacs for Python development"
date: 2012-06-28 15:02:20 +0000
categories: ["PhD", "python", "programming"]
permalink: /setting_up_emacs_for_python_development
---
-   Ubuntu packages to install: `emacs autocutsel texinfo git mercurial`
    (git and texinfo are required by el-get; mercurial is required to
    install pymacs)
-   To set the font size for just this session: press `M-:` and then
    type `(set-face-attribute 'default nil :height 100)` (taken from
    [stack overflow](http://stackoverflow.com/a/296316))

(If you're using an old version of Ubuntu then you might need to use
this PPA to get Emacs 24.3: Get the [latest version of Emacs from this
Ubuntu PPA](https://launchpad.net/~cassou/+archive/emacs))

-   Basic [.emacs](http://www.doc.ic.ac.uk/~wjk/UnixIntro/.emacs) from
    Imperial
-   [A good, recent guide to installing Python tools in
    Emacs](http://caisah.info/emacs-for-python/). Some tweaks:

    -   To use flycheck with Python:
        `sudo pip install --upgrade logilab-common pylint`. Then disable
        warnings and conventions as per [this SO
        post](http://stackoverflow.com/a/19118976/732596).
    -   you can also install pymacs with `el-get-install pymacs` and
        `el-get-install ropemacs`

Plug ins I use:
---------------

First configure `package.el` to use
[MELPA](http://melpa.org/#/getting-started) and
[marmalade](https://marmalade-repo.org/). This is what I put in my
`.emacs` file:

<div class="geshifilter">

``` {.text .geshifilter-text style="font-family:monospace;"}
(require 'package)
(add-to-list 'package-archives
             '("melpa" . "http://melpa.org/packages/") t)
(add-to-list 'package-archives
             '("marmalade" . "http://marmalade-repo.org/packages/") t)
(when (< emacs-major-version 24)
  ;; For important compatibility libraries like cl-lib
  (add-to-list 'package-archives '("gnu" . "http://elpa.gnu.org/packages/")))
(package-initialize)
```

</div>

</p>
This allows you to easily install all these other plug ins:

-   [highlight-symbol](http://www.emacswiki.org/emacs/HighlightSymbol)
-   `zenburn-theme`
-   [magit](https://github.com/magit/magit) (better git support)
-   [buffer move](http://www.emacswiki.org/cgi-bin/wiki/buffer-move.el)
    (easily move buffers around)
-   [FlySpell](http://www.emacswiki.org/emacs/FlySpell)
-   [FlyCheck](https://github.com/flycheck/flycheck) - "flymake done
    right"; just do `package-install` `flycheck`. Then do the 'verify
    setup' trick mentioned in the
    [manual](http://www.flycheck.org/manual/0.23/Quickstart.html#Quickstart).
    I use `flake8`.
-   [goto-last-change](http://www.emacswiki.org/cgi-bin/wiki/goto-last-change.el)
-   [ropemacs](http://rope.sourceforge.net/ropemacs.html) - refactoring,
    go to definition etc for python.
    -   `pip install rope ropemacs`
    -   in emacs, do`package-install` then `pymacs` to install
        from marmalade.
    -   [here](http://www.saltycrane.com/blog/2010/05/my-emacs-python-environment/)
        (section "Edit \~/.emacs to use Ropemacs") are some important
        additions to `.emacs`
    -   [here's](http://stackoverflow.com/a/2855895) a quick guide to
        using ropemacs

Other plugins which come with Emacs but require some configuration:
-------------------------------------------------------------------

-   [recently used files](http://www.emacswiki.org/RecentFiles)
-   [80 column rule](http://www.emacswiki.org/emacs/EightyColumnRule)
-   [setup emacs python mode to use
    ipython](http://www.emacswiki.org/emacs/PythonProgrammingInEmacs#toc5)
-   [emacs-jedi](https://github.com/tkf/emacs-jedi) (autocomplete,
    go-to-source etc)
-   [matlab-emacs](http://sourceforge.net/projects/matlab-emacs/) -
    trying to install this with `el-get` failed. So I checked out
    `matlab-emacs` into `.emacs.d` and added the two required lines to
    my `.emacs`

Some commands
-------------

-   see [this answer about setting the shell
    colours](http://stackoverflow.com/a/6550683/732596)
-   `M-q` reformat comment test. From
    [SO](http://stackoverflow.com/a/2214213).
-   [emacs-jedi keybinds](http://tkf.github.io/emacs-jedi/#keybinds)
-   [EIN
    keybinds](http://tkf.github.io/emacs-ipython-notebook/#commands-keybinds)
    (also see the
    [screenshots](https://github.com/tkf/emacs-ipython-notebook/wiki/Screenshots)
    for more examples)
-   `C-z` undo (or `C-_`)
-   `C-g C-_` or `C-g C-z` redo
-   `C-c C-u` browse URL
-   If you modify `.emacs`, you don't need to restart Emacs for the
    changes to take effect. See [this SO
    post](http://stackoverflow.com/questions/2580650/how-can-i-reload-emacs-after-changing-it).
-   [reload changes recursively in
    IPython](http://stackoverflow.com/a/5399339/732596)
-   [magit cheat sheet](http://daemianmack.com/magit-cheatsheet.html)
-   [debugging Python in
    Emacs](http://twistedmatrix.com/documents/current/core/howto/debug-with-emacs.html)
-   `C-<number>-x tab` rigidly indent region by <number> spaces. e.g.
    `C-4-x tab` or `C-minus-4-x tab`
-   `C-x C-v RET` reload file
-   `C-c C-t` insert `import ipdb; ipdb.set_trace()`
-   `M-%` [incremental search and
    replace](http://www.gnu.org/software/emacs/manual/html_node/emacs/Query-Replace.html)
-   `M-=` show word and character count
-   `C-c g` go to definition (using Rope)

Make errors into clickable links in iPython
-------------------------------------------

-   `cd /usr/share/emacs/24.3/lisp/progmodes`
-   `sudo gunzip python.el.gz`
-   `sudo gedit python.el`
-   Remove <span class="geshifilter">`line-start (1+ (any " \t"))`{.text
    .geshifilter-text}</span> from line 1609
-   `sudo emacs -batch -f batch-byte-compile *.el`

Config .emacs for ipdb.
-----------------------

Code is [adapted from
PedroKroger.net](pedrokroger.net/2010/07/configuring-emacs-as-a-python-ide-2/)

<div class="geshifilter">

``` {.text .geshifilter-text style="font-family:monospace;"}
;;----------------------------------------------------------------------------
;; ipdb
;; from: pedrokroger.net/2010/07/configuring-emacs-as-a-python-ide-2/
;; Highlight ipdb lines:
(defun annotate-pdb ()
  (interactive)
  (highlight-lines-matching-regexp "import pdb")
  (highlight-lines-matching-regexp "pdb.set_trace()"))
 
(add-hook 'python-mode-hook 'annotate-pdb)
 
;;----------
;; Keybinding to add breakpoint:
(defun python-add-breakpoint ()
  (interactive)
  (newline-and-indent)
  (insert "import ipdb; ipdb.set_trace()")
  (highlight-lines-matching-regexp "^[ ]*import ipdb; ipdb.set_trace()"))
 
(define-key python-mode-map (kbd "C-c C-t") 'python-add-breakpoint)
```

</div>

</p>
Notes for using Emacs with C++
------------------------------

-   FlyCheck: To get `clang` to work correctly on Ubuntu 13.10 for
    checking C++ I had to install clang-3.4 using [these
    sources](http://llvm.org/apt/) because 13.04 currently ships with
    clang 3.2 which gives the error:
    `/usr/include/stdio.h:33:11: fatal error: 'stddef.h' file not found`.
    The [bug has been reported on
    launchpad](https://bugs.launchpad.net/ubuntu/+source/llvm-defaults/+bug/1242300).
-   Two candidates for autocompletion appear to be
    [AutoComplete](http://www.emacswiki.org/emacs/AutoComplete) and
    [company-mode](http://company-mode.github.io/).

Some plug-ins I have used in the past but no longer use:
--------------------------------------------------------

-   [flymake config for
    Python](http://www.plope.com/Members/chrism/flymake-mode) (i.e.
    enable on-the-fly checking of Python code) - I now use
    [flycheck](https://github.com/flycheck/flycheck) instead.
-   Many (if not all) of the extensions below could be installed using
    Emacs24's package manager `M-x list-packages`
-   [color themes](http://stackoverflow.com/a/2205968)
-   [iSwitch buffers](http://www.emacswiki.org/emacs/IswitchBuffers)
    (switch buffers by typing any part of the buffer name)
-   [Browse URL](http://www.emacswiki.org/emacs/BrowseUrl). I set
    `(setq browse-url-browser-function 'browse-url-firefox)` and
    `(global-set-key "\C-c\C-u" 'browse-url-at-point)`
-   [Emacs IPython
    Notebook (EIN)](https://github.com/tkf/emacs-ipython-notebook)
    -   [tell emacs-jedi and EIN to work
        together](http://tkf.github.io/emacs-ipython-notebook/#ein:jedi-setup)
    -   [set `ein:console-args` as per this
        commen](https://github.com/tkf/emacs-ipython-notebook/issues/86#issuecomment-11099988)
-   [Collection of Emacs Development Environment
    Tools (CEDET)](http://www.emacswiki.org/emacs/CollectionOfEmacsDevelopmentEnvironmentTools). 
    [SpeedBar](http://cedet.sourceforge.net/speedbar.shtml) is
    especially cool. (CEDET is installed by default with ubuntu's
    emacs24 package, but you need to manually install CEDET to get the
    latest versions)

------------------------------------------------------------------------

### Alternative editors

-   [spyder](http://code.google.com/p/spyderlib/) (scientific
    dev environment)

------------------------------------------------------------------------

### Update 2nd July 2012

I've gone back to using [PyDev](http://pydev.org/) (an
[Eclipse](http://www.eclipse.org/) plug-in) for my Python development.
 I do enjoy Emacs but PyDev is simply too pleasurable and powerful to
ignore.  Plus [PyDev appears to be receiving increasing amounts of
development effort](http://pydev.blogspot.co.uk/), in contrast to some
of the Emacs tools I experimented with.   And Eclipse offers enough
configuration options to mean that I can get Eclipse to feel pretty
"Emacs-like".  The notes below are only about two thirds complete but
they might still be useful...

------------------------------------------------------------------------

So, I've settled on using Python 2.7 for the development of my
disaggregation system.  I'm very happy with Python so far.  The more I
learn about Python, the more excited I get; which is the oposite to the
situation I experienced with MATLAB: the more I learnt about MATLAB, the
more repulsed I became.

So, the next question becomes: which IDE to develop in?  I spent a few
days using the Eclipse plugin PyDev but several things started to bug
me; notably the fact that [the interactive console doesn't respect the
correct Eclipse
keybindings](https://sourceforge.net/tracker/?func=detail&aid=3049914&group_id=85796&atid=577329).
 Plus Eclipse requires lots of messing about with the mouse which can
slow you down a bit.  So I started thinking seriously about using my old
friend Emacs to develop Python in.  Pedro produced an *excellent* [blog
post](http://pedrokroger.com/2010/07/configuring-emacs-as-a-python-ide-2/)
describing how to install a bunch of add-ons to Emacs to make it a
powerful Python IDE.  Unfortunately things have changed a bit since 2010
when that blog post was produced.  Hence this blog post is a list of
modifications to Pedro's blog post to bring it up to date.  I certainly
don't intend to replicate Pedro's excellent work; I'm just producing a
"diff" to bring his blog post up to date. There's also [some good notes
on vanguard33's
blog](http://hide1713.wordpress.com/2009/01/30/setup-perfect-python-environment-in-emacs/).

1.  Install iPython
2.  Install [python-mode](https://launchpad.net/python-mode) into
    `~/.emacs.d/` as per the instructions in the `README` and `INSTALL`
    files
3.  Don't bother manually putting `(setq py-shell-name "ipython")` into
    your `~/.emacs` file. Instead, in emacs, type
    `M-x customize-variable py-shell-name` and change it to `ipython`
4.  `easy_install rope ropemacs`. Modify `.emacs` to get ropemacs to
    work as described in the [ropemacs
    readme](https://bitbucket.org/agr/ropemacs). Install
    [Pymacs](https://github.com/pinard/Pymacs) (there's a bug in the
    install at the time of writing; to get the install to work follow
    the step described in the bug report [fix install of Pymacs on
    Python 2.7 (issue \#28)](https://github.com/pinard/Pymacs/pull/29)).
    You might also need to add `(setq py-load-pymacs-p 'nil)` to your
    `.emacs`
5.  [Magit is now hosted on github](https://github.com/magit/magit).

### Useful resources

-   [emacswiki.org/emacs/PythonProgrammingInEmacs](http://emacswiki.org/emacs/PythonProgrammingInEmacs)

### Tools I tinkered with but am not using

[emacs-for-python](http://gabrielelanaro.github.com/emacs-for-python/)
looks like a quick and easy way to install lots of useful stuff. But I
decided to install individual packages.

**ipython.el**:  I'm not certain if `ipython.el` is required or not (the
latest version can be found in the [ipython repository on
github](https://github.com/ipython/ipython/tree/master/docs/emacs)).
There's lots of discussion about `ipython.el` on
[StackOverflow](http://stackoverflow.com/questions/8226493/ipython-emacs-integration)
and [github](https://github.com/ipython/ipython/pull/1015). There's also
some discussion in the [ipython editors.txt
file](https://github.com/ipython/ipython/blob/master/docs/source/config/editors.txt#L40)
(which I need to read). [this recent comment by Andreas
Röhler](http://pedrokroger.com/2010/07/configuring-emacs-as-a-python-ide-2/#comment-1030)
suggests that `ipython.el` should no longer be necessary. My assumption
for the time being is that `ipython.el` is not required.

#### Autocompletion

The [anything](http://www.emacswiki.org/emacs/Anything) project has been
superceded by the [helm](https://github.com/emacs-helm/helm) project.
You can get the files using something like
`cd ~/.emacs.d; git clone git://github.com/emacs-helm/helm.git` and then
read the `README.md` file. There is also
a [helm-ipython](https://github.com/emacs-helm/helm-ipython) project.
**HOWEVER**, helm-python requires ipython.el (I submitted [a bug
report](https://github.com/emacs-helm/helm-ipython/issues/2)); and I'm
fairly sure that ipython.el is now redundant.

[auto-complete](https://github.com/m2ym/auto-complete/) works pretty
well. I grabbed the latest [auto-complete from
github](https://github.com/m2ym/auto-complete/). Before installing, it's
necessary to also grab [popul-el](https://github.com/m2ym/popup-el) and
[fuzzy-el](https://github.com/m2ym/fuzzy-el) and put these two files in
the `auto-complete` directory prior to installing. (It looks like the
author has split fuzzy-el and popup-el from auto-complete but hasn't
updated the documentation yet.) I like autocomplete to only offer help
when I explicitly ask for help so I added
`(ac-set-trigger-key "TAB") (setq ac-auto-start nil)` to my `.emacs`

