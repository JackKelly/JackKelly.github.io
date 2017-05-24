---
title: "Eclipse notes"
date: 2011-07-28 14:11:00 +0000
categories: ["eclipse", "software engineering"]
permalink: /eclipse_notes
---
### Manually install Eclipse on Ubuntu and add Eclipse to Ubuntu Unity launcher

-   [Manually install
    Eclipse](https://help.ubuntu.com/community/EclipseIDE#User_installation)
-   [Add launcher](http://askubuntu.com/a/80139)

### Build Project shortcut not working in Eclipse 4.2

There is a problem with Eclipse 4.2 and 4.2.1 whereby the "build
project" keyboard shortcut does not work when editing text. The bug
report is [here](https://bugs.eclipse.org/bugs/show_bug.cgi?id=383497)
with a candidate patch, which works for me.

### Git diff not working in Eclipse

After manually installing Eclipse 4.2.1 on a fresh install of Ubuntu
12.04 I found that the `Team -> Commit` command complained that it couldn't launch a
browser to display the git diff. I've documented the (simple) fix [on
the Ubuntu
Wiki](https://help.ubuntu.com/community/EclipseIDE#A.22Failed_to_create_a_browser_control_to_display_diff..22_error).

### Setup Eclipse for use with Arduino

[Great guide for setting up Eclipse for use with
Arduino](http://horrorcoding.altervista.org/arduino-development-with-eclipse-a-step-by-step-tutorial-to-the-basic-setup/).
Some slight modifications for Ubuntu 12.04 and Eclipse Juno:

-   arduino\_base\_path is `/usr/share/arduino/`. So the two directories to add to the
    ArduinoCore are

    ```
    /usr/share/arduino/hardware/arduino/cores/arduino/
    /usr/share/arduino/hardware/arduino/variants/standard/
    ```

-   in the step which starts "In Eclipse right click on the
    “ArduinoCore” project, select “Properties” and then “C/C++ Build”
    you need to then click on "Settings" and you'll find the
    "Directories" setting within the "Tool Settings" tab
-   Some code includes pre-processor directives like `#ifdef ARDUINO`
    to check whether the user is using the Arduino IDE. If you want add
    this `ARDUINO` symbol then right click on the Arduino
    project go to C/C++ build -&gt; Settings and add "ARDUINO=100" to
    "Symbols" under both AVR Compiler and AVR C++ Compiler.
-   My "Olimex AVR-ISP500-TINY" programmer settings in the "Edit AVRDude
    Programmer Configuration New Configuration": Programmer Hardware
    (-c)=Amtel STK500 Version 2.x firmware; override dafault port (-P) =
    /dev/ttyACM0
-   If you need the SPI library: Create a new C++ project in a similar
    way to the ArduinoCore library, with the same include paths. In your
    actual project, make sure that the ArduinoCore library comes last in
    C/C++ Build -&gt; Settings -&gt; AVR C++ Linker -&gt; Libraries.
-   On avr-gcc 4.7 (default on Ubuntu 12.10) I had to remove the `--cref` option.
    Seems to work fine. With the `--cref` option
    in place, the linker exits with an error `avr-g++: error: unrecognized command line option ‘–cref’`. I’ve struggled to find what the “–cref”
    option does. The only hint of an explanation is that it tells the
    linker to “add cross reference to map file”. looking at the
    Eclipse (4.2.1) console after I build my project, I see this still
    includes “-Wl,-Map,.map,–cref” which seems to work fine. So I guess
    it is still using the –cref option, it’s just that the syntax for
    the –cref option is slightly different.
-   The Arduino IDE 1.0.1 creates significantly smaller binaries
    compared to the Eclilpse setup. I examined the arguments the Arduino
    IDE sends to g++ (turn on "show verbose output during compilation")
    and found some differences. To create smaller binaries on Eclipse,
    do this on every AVR project (including ArduinoCore): go to C/C++
    Build -&gt; Settings -&gt; AVR Compiler -&gt; Optimization and add
    `-ffunction-sections -fdata-sections` to "Other Optimization Flags". Do the same
    for the AVR C++ compiler. In all AVR *application* projects (i.e.
    not static libraries) go to AVR C++ Linker -&gt; General and add
    `-Wl,--gc-sections` to "Other Arguments". Clean and re-build.
    My binary went from 26kbytes (81% full) to 14kbytes (43% full). For
    more info on what these switches are doing, see ["function sections"
    on elinux.org](http://elinux.org/Function_sections) and [Stack
    Overflow: Query on -ffunction-section & -fdata-sections options of
    gcc](http://stackoverflow.com/questions/4274804/query-on-ffunction-section-fdata-sections-options-of-gcc)

### Eclipse incorrectly claims things cannot be resolved

If Eclipse claims that includes and classes cannot be resolved (but the
project compiles fine) then take a look at the StackOverflow question
[Eclipse CDT: Symbol 'cout' could not be
resolved](http://stackoverflow.com/questions/10803685/eclipse-cdt-symbol-cout-could-not-be-resolved)
and [my answer about fixing this for projects with two target
architectures](http://stackoverflow.com/a/12951817/732596) each with
their own build configuration.

### Eclipse code checking does wierd stuff but code compiles fine

I was finding that sometimes Eclipse would claim there were issues with
my code (e.g. incorrect arguments being supplied to functions) even
though the compiler was entirely happy. This seems to be fixed by
deleting the project from Eclipse (but leave it on disk) and then
re-importing the project.

### User dictionary woes

See [the comment on this SO
post](http://stackoverflow.com/questions/13072554/eclipse-juno-not-recognizing-user-defined-dictionary-has-been-specified)
about using a user dictionary with C++

#### UPDATE 2nd July 2012

The notes below are now out of date.  I now use [Workspace
Mechanic](http://code.google.com/a/eclipselabs.org/p/workspacemechanic/)
to record and synchronise my Eclipse settings.  My [Eclipse settings are
on github](https://github.com/JackKelly/mechanic).  Settings which can't
be stored on Workspace Mechanic are in a file called
"[prefs\_which\_need\_to\_be\_manually\_installed.txt](https://github.com/JackKelly/mechanic/blob/master/prefs_which_need_to_be_manually_installed.txt)".

------------------------------------------------------------------------

#### Keyboard shortcut for building

1.  Window &gt; Preferences &gt; General &gt; Keys
2.  Select “Build All”
3.  Change “When” to “C/C++ Editor”

#### Save automatically before build

General &gt; Workspace &gt; Save automatically before build

#### Configuring Eclipse to parse Boost.Test output:

<http://stackoverflow.com/questions/2491380/boost-test-and-eclipse>

#### Colour preference settings

-   Line / selection background colours: General &gt; Editors &gt; Text
    Editors &gt; Appearance color options
-   General &gt; Appearance &gt; Colors and Fonts
-   Aptana Studio &gt; Themes (I like Sunburst; and make sure "Apply to
    all (non-Studio) editors" is checked to apply these colours to PyDev

### Aptana Studio

[Aptana Studio](http://www.aptana.com/products/studio3) is an Integrated
Development Environment (IDE) for building web apps. It's based on
Eclipse and is free.  This blog post is simply a list of configuration
options that I use to make Aptana Studio 3 comfortable for me:

### Settings:

-   Aptana Studio → Editors → JavaScript → Indentation → Tab policy =
    Use Spaces, Tab size = 4
-   Aptana Studio → Editors → HTML → Content Assist → Unselect
    "Automatically insert closing tags"
-   Aptana Studio → Themes → Suburst (change "selection" colour to
    something a little brighter so you can see the results of a
    'find' operation)
-   Aptana Studio → Content Assist → Unselect "Insert single proposals
    automatically" and set "Auto-display content assist" to off
-   General → Editors →  Text Editors → unselect "Highlight current
    line"; select "Insert spaces for tabs"; tab width = 4
-   General→ Keys → Scheme = Emacs

### Keyboard shortcuts (by no means exhaustive!):

-   alt + / = content assist
-   ctrl + shift + f = indent entire file
-   Add comment block = Ctrl+Shift+/
-   Toggle comment = Ctrl+/
-   Undo = Ctrl+X+u
-   Redo = Ctrl+C+r
-   Format (correct indentation) = Ctrl+I (this needs setting manually)

#### Quietening down content assist

-   uncheck PyDev &gt; Editor &gt; Code Completion (ctx insensitive and
    common tokens) &gt; "Use common tokens auto code completion"


