---
title: "Eclipse with SVN and NXJ"
date: 2011-03-10 19:54:00 +0000
categories: ["eclipse", "robotics", "nxj", "svn"]
permalink: /eclipse_with_svn_and_nxj
---
One of the most enjoyable courses I took during the Imperial MSc in
Computing Science I did from 2010-2011 was the [Robotics
course](http://www.doc.ic.ac.uk/%7Eajd/Robotics/index.html). Every week
we learnt about a cool new technique in a lecture and then we put that
new technique into practice. My group decided to abandon "Robot-C"
compiler and instead use a Java implementation called NXJ.  Below are my
notes on configuring Eclise, SVN and NXJ to work on the Imperial Ubuntu
Linux machines.

### <span style="font-size:18pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:bold;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">Install Subclipse (Eclipse’s SVN client)</span> {#internal-source-marker_0.5452003090684711 dir="ltr"}

1.  <span
    style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">Help &gt;
    Install New Software</span>
2.  <span
    style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">Enter
    this URL: </span>[<span
    style="font-size:11pt;font-family:Arial;color:#000099;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:underline;vertical-align:baseline;">http://subclipse.tigris.org/update\_1.6.x</span>](http://subclipse.tigris.org/update_1.6.x)
3.  <span
    style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">Add
    Subclipse</span>
4.  <span
    style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">Once
    Subclipse is installed, you’ll also need to </span>[<span
    style="font-size:11pt;font-family:Arial;color:#000099;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:underline;vertical-align:baseline;">install
    the javaHL
    library</span>](http://subclipse.tigris.org/wiki/JavaHL#head-7498d204a5be83e0e97d196ba75fc797d5f0c822)

<span style="font-size:18pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:bold;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">Install leJOS NXJ plugin for Eclipse</span> {#install-lejos-nxj-plugin-for-eclipse dir="ltr"}
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[<span
style="font-size:11pt;font-family:Arial;color:#000099;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:underline;vertical-align:baseline;">http://lejos.sourceforge.net/nxt/nxj/tutorial/Preliminaries/UsingEclipse.htm</span>](http://lejos.sourceforge.net/nxt/nxj/tutorial/Preliminaries/UsingEclipse.htm)

\

<span style="font-size:18pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:bold;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">Eclipse configuration</span> {#eclipse-configuration dir="ltr"}
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### <span style="font-size:12pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:bold;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">Making Eclipse indent code in an Emacs-compatible way (so other team members can continue to use Emacs)</span> {#making-eclipse-indent-code-in-an-emacs-compatible-way-so-other-team-members-can-continue-to-use-emacs dir="ltr"}

<span
style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">Set
Eclipse to use spaces instead of tabs (so the code generated by Eclipse
looks OK in Emacs).  Go to Window &gt; Preferences &gt; Java &gt; Code
Style &gt; Formatter.  Edit the code style and set “tab policy” to
“spaces only” and set “tab size” to 8.  Save the code style with a new
name.</span>\
\
<span
style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:bold;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">Tell
Eclipse not to automatically import</span>\
<span
style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">Windows
&gt; Preferences &gt; Java &gt; Editor &gt; content Assist</span>\
<span
style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">uncheck
“add import instead of qualified name”</span>

\

#### <span style="font-size:12pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:bold;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">NXJ JavaDocs within Eclipse</span> {#nxj-javadocs-within-eclipse dir="ltr"}

<span
style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">Within
Eclipse, right-click on your Robotics project and go to:</span>

\
\

<span
style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">Properties
&gt; Java Build Path &gt; Libraries</span>

\

<span
style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">Click
on the "&gt;" icon to the left of "classes.jar" and select "Javadoc
location".  Click "edit" and enter:</span>[<span
style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">
</span><span
style="font-size:11pt;font-family:Arial;color:#000099;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:underline;vertical-align:baseline;">http://lejos.sourceforge.net/nxt/nxj/api/</span>](http://lejos.sourceforge.net/nxt/nxj/api/)\
\
<span
style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">Eclipse
should now be able to give you useful information about NXJ classes and
member functions if you hover over the functions (note that if you click
on "Validate" then it'll claim the URL doesn't validate... but it still
seems to work)</span>

\

### <span style="font-size:14pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:bold;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">Environment variables (for our Imperial DoC machines running the tcsh shell)</span> {#environment-variables-for-our-imperial-doc-machines-running-the-tcsh-shell dir="ltr"}

<span
style="font-size:11pt;font-family:Courier New;color:#000000;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">setenv
PATH "/homes/USERNAME/binaries/lejos\_nxj/bin:\$PATH"</span>\
<span
style="font-size:11pt;font-family:Courier New;color:#000000;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">setenv
LD\_LIBRARY\_PATH "/homes/USERNAME/binaries/lejos\_nxj/bin"</span>\
<span
style="font-size:11pt;font-family:Courier New;color:#000000;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">setenv
NXJ\_HOME "/homes/USERNAME/binaries/lejos\_nxj"</span>\
<span
style="font-size:11pt;font-family:Courier New;color:#000000;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">setenv
JAVA\_HOME "/usr"</span>

<span style="font-size:18pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:bold;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">Check out SVN repository into Eclipse workspace</span> {#check-out-svn-repository-into-eclipse-workspace dir="ltr"}
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1.  <span
    style="font-size:10pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">File &gt;
    Import</span>
2.  <span
    style="font-size:10pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">SVN &gt;
    Checkout Projects from SVN</span>
3.  <span
    style="font-size:10pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">Create
    a new repository location</span>
4.  <span
    style="font-size:10pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">Enter
    repository URL</span>
5.  <span
    style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">Select
    </span><span
    style="font-size:11pt;font-family:Courier New;color:#000000;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">trunk</span>
6.  <span
    style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">“Check
    out as a project configured using the New Project Wizard”</span>
7.  <span
    style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">Select
    “Java Project”</span>
8.  <span
    style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">Give
    it a project name (e.g. “robotics") and set “Project layout” to “Use
    project folder as root for sources and class files”</span>
9.  <span
    style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">Use
    project folder as root for sources and class files</span>
10. <span
    style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">“Then
    select Libraries and then "Add external JARs". Browse for
    classes.jar in your lejos\_nxj/lib installation and select it. As
    classes.jar replaces the standard Java run time library, you should
    remove it by selecting "JRE System Library" and clicking "Remove".
    You will now see classes.jar (and not JRE System Library) under
    "Referenced Libraries" in org.me.myproject.” (</span>[<span
    style="font-size:11pt;font-family:Arial;color:#000099;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:underline;vertical-align:baseline;">source</span>](http://lejos.sourceforge.net/nxt/nxj/tutorial/Preliminaries/UsingEclipse.htm#6)<span
    style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">)</span>

<span style="font-size:18pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:bold;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">Creating new files and packages</span> {#creating-new-files-and-packages dir="ltr"}
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<span
style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">Create
a new package for each sub-question.  e.g.</span>

\

<span
style="font-size:11pt;font-family:Courier New;color:#000000;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">package
practicals.p2.q2\_3; // practical 2, question 2, part 3</span>

\

<span
style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">Create
a new file inside a new / existing package by right-clicking on the
package and selecting New &gt; Class.  Once you’ve created a new class,
convert it to a leJOS file by right-clicking on the file and selecting
“leJOS NXJ” &gt; “Convert to leJOS NXJ project”.  Right-click again on
your robotics folder in Eclipse and select “Properties &gt; Java Build
Path &gt; Order and Export” and make sure the JRE library is below the
lejos\_nxj/lib/classes.jar.</span>\
\
<span
style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">Add
the following text immediately below the package line to you .java
file:</span>

\

<span
style="font-size:11pt;font-family:Courier New;color:#000000;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">import
lejos.nxt.\*;</span>

<span
style="font-size:11pt;font-family:Courier New;color:#000000;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">import
fritzlib.\*;</span>

<span style="font-size:18pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:bold;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">Compile and upload to robot</span> {#compile-and-upload-to-robot dir="ltr"}
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<span
style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">Run:</span>

\

<span
style="font-size:11pt;font-family:Courier New;color:#000000;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">nxj
PACKAGE.CLASSNAME --classpath /PATH/TO/ROBOTICS --verbose</span>

\

<span
style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">e.g.:</span>

\
\

<span
style="font-size:11pt;font-family:Courier New;color:#000000;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">nxj
practicals.p2.q2\_3.SonarDisplay --classpath
/home/USERNAME/workspace/robotics --verbose</span>

\

<span
style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">(given
that some of the team want to work on Eclipse and some in Emacs then we
may be better off using </span>[<span
style="font-size:11pt;font-family:Arial;color:#000099;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:underline;vertical-align:baseline;">Ant</span>](http://ant.apache.org/)<span
style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">
files to configure classpaths etc, </span>[<span
style="font-size:11pt;font-family:Arial;color:#000099;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:underline;vertical-align:baseline;">as
per these instructions on the leJOS
website</span>](http://lejos.sourceforge.net/nxt/nxj/tutorial/Preliminaries/UsingEclipse.htm#6)<span
style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">)</span>\
\
<span
style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">Other
useful flags for nxj</span>

-   <span
    style="font-size:11pt;font-family:Courier New;color:#000000;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">-u</span><span
    style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">
    (upload by USB)</span>
-   <span
    style="font-size:11pt;font-family:Courier New;color:#000000;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">-b</span><span
    style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">
    (upload by Bluetooth).</span>
-   <span
    style="font-size:11pt;font-family:Courier New;color:#000000;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">-r</span><span
    style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:normal;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;">
    to automatically run the program after transferring to robot.</span>


