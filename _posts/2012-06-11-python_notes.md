---
title: "Python notes"
date: 2012-06-11 14:03:47 +0000
categories: ["python", "programming", "PhD"]
permalink: /python_notes
---
### Installing Emacs on Ubuntu and Python in 2017

-   The aim is to use python3 and virtualenv for python development.
-   `sudo apt install emacs25-lucid python-pip python3-dev`
-   [Install
    elpy](https://elpy.readthedocs.io/en/latest/introduction.html)
    -   copy `elpy-profile.el` as described in [this elpy
        issue](https://github.com/jorgenschaefer/elpy/issues/1129)
-   Now install Python packages required by `elpy`. The idea is to
    deliberately keep these "elpy requirements" separate from the
    packages required by each python project. This way, we can update
    the "elpy packages" across the entire system in one go; and we can
    list just the packages required by each project using
    `pip freeze --local`.
    -   `pip3 install --user jedi flake8 importmagic autopep8 virtualenvwrapper`
    -   `pip3 install --user 'ipython<5'` (ipython &gt;= 5 does not work
        well on emacs. See
        [here](https://emacs.stackexchange.com/questions/24750/emacs-freezes-with-ipython-5-0-0)
        and [here](https://github.com/jorgenschaefer/elpy/issues/935))

Add this to the end of `~/.profile`:

    # Python virtualenvwrapper
    export PATH="$PATH:$HOME/.local/bin"
    export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
    export WORKON_HOME=$HOME/.virtualenvs
    export PROJECT_HOME=$HOME/workingcopies
    export VIRTUALENVWRAPPER_VIRTUALENV_ARGS='--system-site-packages'

Add this to the end of `~/.bashrc`:

    # Python virtualenvwrapper
    source $HOME/.local/bin/virtualenvwrapper.sh

Logout. Log back in.

`~/.emacs` should contain this:

    (require 'package)
    (add-to-list 'package-archives
                 '("elpy" . "http://jorgenschaefer.github.io/packages/"))

    (custom-set-variables
     ;; custom-set-variables was added by Custom.
     ;; If you edit it by hand, you could mess it up, so be careful.
     ;; Your init file should contain only one such instance.
     ;; If there is more than one, they won't work right.
     '(package-selected-packages (quote (elpy)))
     )

    ;; eply
    (package-initialize)
    (elpy-enable)
    (elpy-use-ipython)

### Documenting code

-   [sphinx-apidoc](http://sphinx-doc.org/man/sphinx-apidoc.html) "is a
    tool for automatic generation of Sphinx sources that, using the
    autodoc extension, document a whole package in the style of other
    automatic API documentation tools."
-   [Math support in Sphinx](http://sphinx-doc.org/latest/ext/math.html)
-   [Example documentation markup from An Example PyPi
    project](http://pythonhosted.org/an_example_pypi_project/sphinx.html)

### Python libraries

-   [Monary](https://monary.readthedocs.org/#) - need to install [these
    Ubuntu
    packages](https://gist.github.com/chergert/4bb50c11f2a51212d50b),
    then install
    [mongo-c-driver](https://github.com/mongodb/mongo-c-driver), then
    create `/etc/ld.so.conf.d/libmongoc.conf` and write `/usr/local/lib`
    in that file. Then run `sudo ldconfig`. Then run `make test`. Then
    do `pip install pkgconfig monary`.
-   [Theano](http://deeplearning.net/software/theano/) - “Theano is a
    Python library that allows you to define, optimize, and evaluate
    mathematical expressions involving multi-dimensional arrays
    efficiently.”
-   [Pandas](http://pandas.pydata.org/) - “an open source, BSD-licensed
    library providing high-performance, easy-to-use data structures and
    data analysis tools for the Python programming language… Time
    series-functionality: date range generation and frequency
    conversion, moving window statistics, moving window linear
    regressions, date shifting and lagging. Even create domain-specific
    time offsets and join time series without losing data;”
-   [GPUStats](https://github.com/dukestats/gpustats) - "gpustats is a
    [PyCUDA](http://pypi.python.org/pypi/pycuda)-based library
    implementing functionality similar to that present in scipy.stats.
    It implements a simple framework for specifying new CUDA kernels and
    extending existing ones. Here is a (partial) list of target
    functionality: Probability density functions (pdfs). These are
    intended to speed up likelihood calculations in particular in
    Bayesian inference applications, such as in PyMC, Random variable
    generation using CURAND"
-   [PyOpenCL](http://pypi.python.org/pypi/pyopencl)
-   [PyMC](http://pymc-devs.github.com/pymc/README.html) - “PyMC is a
    python module that implements Bayesian statistical models and
    fitting algorithms, including Markov chain Monte Carlo. Its
    flexibility and extensibility make it applicable to a large suite
    of problems. Along with core sampling functionality, PyMC includes
    methods for summarizing output, plotting, goodness-of-fit and
    convergence diagnostics.”
-   [SciKits](http://scikits.appspot.com/) - “Welcome to SciKits! Here
    you’ll find a searchable index of add-on toolkits that complement
    SciPy, a library of scientific computing routines. The SciKits cover
    a broad spectrum of application domains, including financial
    computation, audio processing, geosciences, computer vision,
    engineering, machine learning, medical computing and
    bioinformatics.”

    -   [sckikit-learn](http://scikit-learn.org/stable/): machine
        learning in Python
-   [NetworkX](http://networkx.lanl.gov/) - “NetworkX is a Python
    language software package for the creation, manipulation, and study
    of the structure, dynamics, and functions of complex networks.”

### Python 2 versus 3

-   [jakevdp:
    will-scientists-ever-move-to-python-3](http://jakevdp.github.com/blog/2013/01/03/will-scientists-ever-move-to-python-3/)

### GUIs

-   From some very superficial searching, it looks like wxPython is the
    prefered Python GUI for use with matplotlib (I could be
    wrong though). One big disadvantage is that wxPython isn’t packaged
    as standard with Python, whilst tkInter is.
-   [wxPython screenshots](http://wxpython.org/screenshots.php)
-   [list of Python GUI
    toolkits](http://wiki.python.org/moin/GuiProgramming)

### Plotting

-   [Nice examples by Eli
    Bendersky](http://eli.thegreenplace.net/2008/08/01/matplotlib-with-wxpython-guis/)
    (including live data and interactivity) of using matplotlib with
    wxPython GUIs
-   [embedding matplotlib plots in GUI
    apps](http://www.scipy.org/Cookbook/Matplotlib#head-ec4b41af700df8990616bcefb312461c8a8891e3)

### Tutorials & videos

-   [Advanced Statistical Computing at Vanderbilt University's
    Department of Biostatistics by Chris Fonnesbeck (lead dev.
    PyMC)](http://nbviewer.ipython.org/github/fonnesbeck/Bios366/tree/master/notebooks/)
-   [Probabilistic-Programming-and-Bayesian-Methods-for-Hackers](https://github.com/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers)
-   [Python Scientific Lecture Notes](http://scipy-lectures.github.com/)
-   [goatbar’s iPython “research tools”
    videos](http://www.youtube.com/playlist?list=PL7E11B34616530F5E)
-   [Data analysis in Python with
    Pandas](http://www.youtube.com/watch?v=w26x-z-BdWQ&feature=fvwp&NR=1)
    (3hr video)
-   [Ubuntu tutorial videos on using Python with GTK and GObject and
    Glade](http://developer.ubuntu.com/showdown/workshops/)

### Optimised compilers

-   [Numba](https://github.com/ContinuumIO/numba): a NumPy-aware
    optimised compiler for Python (and here's a [Numba vs Cython blog
    post by
    jakevdp](http://jakevdp.github.com/blog/2012/08/24/numba-vs-cython/))

### Development tools

-   [Using iPython from within
    PyDev](http://pydev.blogspot.co.uk/2011/08/ipython-pydev.html) (Eclipse)

### Statistics and graphical models

-   [pebl](http://code.google.com/p/pebl-project/) - Python Environment
    for Bayesian Learning

### Installing an up-to-date scientific Python stack on Ubuntu when you do have root permissions

    sudo apt-get install python-dev python-pip python-sphinx libzmq-dev python-matplotlib python-scipy
    sudo pip install cython pandas pyzmq jinja2  ipython sphinx

libzmq-dev, pyzmq and jinja2 are all required for iPython notebook.

#### For scipy:

    sudo apt-get install libatlas-base-dev gfortran python-pip
    sudo pip install scipy

If you get the following error when trying to import scipy
`libatlas.so.3: cannot open shared object file: No such file or directory`
then run

    sudo update-alternatives --config libblas.so.3

and select `/usr/lib/atlas-base/atlas/libblas.so.3` (this tip taken from
[Daniel Nouri's blog post on
libblas](http://danielnouri.org/notes/2012/12/19/libblas-and-liblapack-issues-and-speed,-with-scipy-and-ubuntu/))

### Installing Python when you don’t have root permissions

-   `./configure --prefix=/data/usr`
-   Then edit `Makefile` and add `-fPIC` to the end of the line that
    starts `CC=` (as per [this SO
    answer](http://stackoverflow.com/a/637048)) (`-fPIC` is required so
    `xmllib2` compiles correctly)
-   `make -j8`
-   `make install`

### Install stuff for GTK+ development (when you don’t have root permissions)

-   Compile Python as above
-   Install libxml2:
    -   download `libxml2-2.X.Y.tar.gz` from
        [xmlsoft.org/libxml2](ftp://xmlsoft.org/libxml2/)
    -   `./configure --prefix=/data/usr`
    -   `make -j8`
    -   `make install`
    -   `cd python`
    -   `setenv LD_LIBRARY_PATH "/data/usr/lib"`
    -   `python setup.py build`
    -   `python setup.py install`
-   ​Make sure `LD_LIBRARY_PATH` is set as above
-   Follow “Installing from Source” instructions from
    [here](http://python-gtk-3-tutorial.readthedocs.org/en/latest/install.html)
    (install jhbuild, then install pygobject using jhbuild). Some notes
    on that process:
    -   I added the following two lines to `~/.config/jhbuildrc:`
        -   `prefix = "/homes/dk3810/.local/opt"`
        -   `modulesets_dir = "/homes/dk3810/.local/modulesets"`
    -   I copied the `*.modules` files from
        [releng](http://ftp.gnome.org/pub/GNOME/teams/releng/) to
        `/homes/dk3810/.local/modulesets`

### Profiling

-   add the following to `~/.bash_aliases`:
    `alias profile='python -m cProfile -s time'` (from
    [SO](http://stackoverflow.com/a/582337/732596))

Packaging
=========

-   [`distribute`](http://packages.python.org/distribute/setuptools.html)
    aims to supercede `setuptools`. `distribute` is compatible with
    Python 3, `setuptools` isn't. My `setup.py` files are sufficiently
    simple to mean that I don't need to modify anything to allow users
    to use either `setuptools` or `distribute`.
-   [Building and Distributing Packages with
    Distribute](http://packages.python.org/distribute/setuptools.html)
-   See
    [here](http://python4astronomers.github.com/installation/packages.html#where-do-packages-get-installed)
    for details of where files are installed by `pip`
-   Official Python documentation on [modules and packages and directory
    layout](http://docs.python.org/2/tutorial/modules.html)
-   [pip documentation](http://www.pip-installer.org)
-   [Non-recursive upgrades using
    pip](http://www.pip-installer.org/en/latest/cookbook.html#non-recursive-upgrades)

Integrating git workflow with the Python package publishing process
-------------------------------------------------------------------

-   [SO: How to configure setup.py to have pip install from GitHub
    master?](http://stackoverflow.com/questions/9949420/how-to-configure-setup-py-to-have-pip-install-from-github-master)
-   [SO: Automatic version number both in setup.py (setuptools) AND
    source
    code?](http://stackoverflow.com/questions/6786555/automatic-version-number-both-in-setup-py-setuptools-and-source-code)
-   Blog post on cberner.com on [Git revision numbers for setuptools
    packages](http://cberner.com/2012/02/26/git-revision-numbers-for-setuptools-packages/)
    using a simple bash script.
-   Blog post on dcreager.net on [Extracting setuptools version numbers
    from your
    git](http://dcreager.net/2010/02/10/setuptools-git-version-numbers/)
    using a small Python script
-   [setuptools manual on using
    "tagging"](http://peak.telecommunity.com/DevCenter/setuptools?action=highlight&value=setuptools#tagging-and-daily-build-or-snapshot-releases)
    (but this doesn't integrate directly with git)

### Notes for creating a package

#### Aims & Overview:

-   Upload just description of project to `pypi` using
    `python setup.py register`.
-   Don't upload code to `pypi`. Instead use `download_url` in
    `setup.py` to point to github. e.g.:
    `download_url = "https://github.com/JackKelly/rfm_ecomanager_logger/tarball/master#egg=rfm_ecomanager_logger-dev"`
-   Use git tags to track version numbers.
-   Automatically suck these version numbers into Python's packaging
    system and also into the project's `__version__` attribute.

#### Details:

-   Setup directory structure etc. as described in [The Hitchhiker's
    Guide to Packaging](http://guide.python-distribute.org/) and ["Dive
    Into Python 3: Chapter 16, Packaging Python
    Libraries"](http://docs.activestate.com/activepython/3.1/diveintopython3/html/packaging.html)
-   Use `git -s tag VERSION.NUMBER` for version numbers and push these
    tags to github with `git push --tags` (read
    [tagging](http://gitready.com/beginner/2009/02/03/tagging.html) to
    learn how to use git tagging)
-   Read blog post on dcreager.net on [Extracting setuptools version
    numbers from your
    git](http://dcreager.net/2010/02/10/setuptools-git-version-numbers/)
    using a small Python script
-   Figure out how to use these version numbers for **version** as well
    as for setuptools. See [SO: Automatic version number both in
    setup.py (setuptools) AND source
    code?](http://stackoverflow.com/questions/6786555/automatic-version-number-both-in-setup-py-setuptools-and-source-code)
-   Might need to use ConfigParse to parse setup.cfg (see [this
    example](http://pydoc.net/hgtools/1.0.1dev/hgtools.plugins)) to
    extract the version number from `setup.cfg`
-   Figure out how to point `download_url` to the correct tag
-   It appears that two things are necessary to get upgrading to work
    correctly: `version` (in `setup.py`) needs to incremement and
    `download_url` needs to point to a URL with `#egg=PROJECT-VERSION`
    appended to it (or upload all the files to `pypi` instead of
    downloading from `github`, but that feels rather ugly to duplicate
    lots of files)


