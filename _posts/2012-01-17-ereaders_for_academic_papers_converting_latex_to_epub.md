---
title: "E-readers for academic papers & converting LaTeX to EPUB"
date: 2012-01-17 11:48:41 +0000
categories: ["LaTeX", "epub", "e-books", "e-readers", "PhD"]
permalink: /ereaders_for_academic_papers_converting_latex_to_epub
---
I currently read academic papers by downloading the PDF and printing;
and the tiny collection of LaTeX documents I've authored are output as
PDFs. It feels like I should embrace e-readers for academic reading and
writing. I have a Kindle Keyboard which does handle PDFs but reading
PDFs is not especially pleasant on the Kindle because of its small
screen, relatively sluggish refresh rate and clunky note-taking feature.

### Alternative e-readers

-   The Kindle DX (a large-format Kindle) and the Kindle Touch both do a
    better job of displaying PDFs than the Kindle Keyboard. But neither
    are available in the UK.
-   Asus makes several e-readers. The most interesting for my purposes
    are:
    -   The [Asus
        DR-900](http://www.asus.com/Eee/Eee_Reader/Eee_Reader_DR900/): a
        9" touch screen e-reader.
    -   The [Asus Eee Note
        EA800](http://www.asus.com/Eee/Eee_Note/Eee_Note_EA800/): an 8"
        e-reader with a stylus for hand-writing notes.

If I bought an alternative e-reader, could I still read my Amazon
ebooks? It looks like Calibre can convert from the Kindle's .azw format
to .epub.  I should also look into converting PDFs to a format which is
more suitable for a Kindle Keyboard: I've tried a few tools but none
produce a satisfactory output.

### Converting LaTeX to HTML and/or EPUB

I write my academic stuff in LaTeX largely because it has excellent
support for typesetting maths, cross-references and for bibliography
management. PDFs are great for printing but not quite so good for
displaying on the web or e-readers.

The latest epub format, epub 3, is based on HTML5 and supports MathML.
Outputting LaTeX to HTML5 with MathML support sounds like a good
solution, except that legacy browsers don't support HTML5 and, at the
time of writing, I think few (if any) e-readers support epub3. Some
links:

-   Forum discussing [Mathematics in
    EPUB](http://www.mobileread.com/forums/showthread.php?t=73914)
-   [Linked in group on ebooks for math and
    science](http://www.linkedin.com/groups?home=&gid=1945452&trk=anet_ug_hm&goback=.gmr_1945452)
-   [Overview of the epub 3
    specification](http://www.digitalbookworld.com/2011/breaking-it-down-the-epub-3-spec/)
-   ["How to post mathematics?" on the web using HTML5, LaTeX and
    MathML](http://knol.google.com/k/stef-mot/mathematics-and-web-html5-latex-mathml/2fdyfc9mft4ir/1#)
-   [List of tools for converting from LaTeX to
    HTML](http://www.charlietanksley.net/philtex/converting-from-latex/)
-   [10 recommendations for the future of scholarly
    publishing](http://blog.publishingtechnology.com/semantic-web/12-step-plan-scholarly-publishing/)

### Academic publishing in Drupal

Drupal has some interesting modules for rendering LaTeX in web pages,
for example [MathJax](http://drupal.org/project/mathjax) and
[DruTeX](http://drupal.org/project/drutex). And a [Bibliography
module](http://drupal.org/project/biblio) with discussion about
[integrating Zotero](http://drupal.org/node/211102). 

*Update 4/2/2012*: I've tried the Drupal Biblio module and it's not for
me.  I just want something which will pull references from my Zotero
library or from a DOI number.  I really don't want to have to maintain
two biblio DBs.  So I'm just going to manually hyperlink references like
this ([Hart,
1992](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=192069 "G. W. Hart, ‘Nonintrusive appliance load monitoring’, Proceedings of the IEEE, vol. 80, no. 12, pp. 1870-1891, Dec. 1992. ")).
This is easier to maintain, easier to read and generally easier for
everyone.  The MathJax module, on the other hand, is great!

### Originating content as XML

Instead of authoring content as LaTeX, perhaps I should consider
authoring it as HTML/XML? Some links:

-   WordPress has a pluging called
    [Zotpress](http://wordpress.org/extend/plugins/zotpress/) for
    displaying Zotero citations on WordPress.
-   [dompdf](http://code.google.com/p/dompdf/) is an HTML to
    PDF converter.
-   [ePub export](http://wordpress.org/extend/plugins/epub-export/)
    published Wordpress docs as ePub
-   The [NLM DTD](http://dtd.nlm.nih.gov/) (National Library of Medicine
    Document Type Definition) defines academic XML files.
-   [Annotum](http://annotum.org/) is a promising sounding project
    ([detailed article](http://www.ncbi.nlm.nih.gov/books/NBK63828/)).
    It's a WordPress plugin which adds the following features (amongst
    others):
    -   WYSIWYG for equations, figures, tables, citations and references
        (import from Zotero [is
        coming](http://annotum.org/2012/01/14/annotum-roadmap/))
    -   coauthoring, comments, version tracking and revision comparisons
    -   export to PDF and XML
    -   Articles can be cited
    -   It's not clear how I'd do (I haven't looked into this yet): code
        highlighting (there are lots of code-highlighting
        plugins), cross-references.
-   [Why I Switched From Drupal to
    WordPress](http://eagereyes.org/blog/2012/why-i-switched-drupal-wordpress)
-   [Scholarly HTML](http://scholarlyhtml.org/)
-   [jiscPUB](http://jiscpub.blogs.edina.ac.uk/)
-   Arstechnica: "[Apple to announce tools, platform to "digitally
    destroy"
    textbook publishing.](http://arstechnica.com/apple/news/2012/01/apple-to-announce-tools-platform-to-digitally-destroy-textbook-publishing.ars)"
    Probably based on ePub3.

 

