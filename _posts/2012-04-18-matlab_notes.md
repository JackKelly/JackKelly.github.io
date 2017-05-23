---
title: "MATLAB notes"
date: 2012-04-18 08:42:15 +0000
categories: ["MATLAB", "PhD", "programming"]
permalink: /matlab_notes
---
Just some random notes about MATLAB.

### Curve fitting toolbox GUI hangs

If I try to use the [curve fitting
toolbox](http://www.mathworks.co.uk/help/toolbox/curvefit/) by typing
<span class="geshifilter">`cftool`{.text .geshifilter-text}</span> into
the MATLAB prompt, the cftool GUI loads but it hangs before allowing me
to do anything.  I'm on Ubuntu 11.10 64-bit and I've tried Matlab R2011b
and R2012a.  This problem has been [discussed on Matlab
Central](http://www.mathworks.de/matlabcentral/answers/22040-cftool-crashes-matlab)
and the solution seems to be to start matlab with <span
class="geshifilter">`matlab -softwareopengl`{.text
.geshifilter-text}</span> (which works for me).

