---
title: "Simplifying NILMTK"
date: 2016-02-09 09:46:50 +0000
categories: ["nilmtk"]
permalink: /simplifying_nilmtk
---
NILMTK is now over two years old. Having had a chance to use it as a
*user* (rather than a developer), and also having had a chance to take a
step back from NILMTK development, it feels like there are quite a few
opportunities to *simplify* the NILMTK code base, without modifying the
public API much (although the public API probably *could* also do with
some tidying up - but if we were to do that then we'd be careful to
slowly make functions deprecated rather than just strip stuff out
straight away).

The NILM issue queue now has [a 'simplify'
label](https://github.com/nilmtk/nilmtk/labels/simplify) to indicate
which issues are to do with, well, making NILMTK more simple! The two
main ideas are:

1.  [Replace NILMTK's out-of-core code with
    Blaze](https://github.com/nilmtk/nilmtk/issues/248)
2.  [NILMTK should interact with other Python tools more
    smoothly](https://github.com/nilmtk/nilmtk/issues/479)

Please do let me know your thoughts (ideally on the issue queue rather
than on this blog post).

The core NILMTK developers are really busy at the moment so these ideas
definitely won't be implemented any time soon - and may *never* be
implemented. But it would be great to hear your opinions. And, of
course, we'd try very hard not to modify the public API unless it really
needs to be modified.<!--break-->

