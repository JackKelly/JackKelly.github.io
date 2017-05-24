---
title: "Notes for producing clean plots in Matlab for LaTeX"
date: 2011-12-06 16:47:22 +0000
categories: ["MATLAB", "LaTeX", "PhD"]
permalink: /notes_for_producing_clean_plots_in_matlab_for_latex
---
Remarkably, MATLAB does not have in-built support for exporting figures
as EPS files with placeholders plus a TEX file (hence allowing LaTeX to
do the typesetting).  But there are some user-submitted scripts.  The
most promising looks to
be [matlabfrag](http://www.mathworks.de/matlabcentral/fileexchange/21286).

After producing a figure in MATLAB, output an  `.eps` file like
this:


{% highlight matlab %}
% FORMAT TICK MARKS
set(gca, 'TickDir', 'out', 'XColor', [0.25 0.25 0.25], 
    'YColor', [0.25 0.25 0.25]);
set(gca, 'YLim', [0 200], 'YTick', [0 100 200], 'YTickLabel', []);
box off; % remove axes on right and top
 
% SET SIZE OF FIGURE
set(gcf,'units','centimeters');
pos = get(gcf, 'position');
set(gcf, 'position', [pos(1:2),5 ,5]); % make figure 5cm x 5cm
 
% OUTPUT
matlabfrag('filename'); % export a .tex and a .eps file using matlabfrag
                        % do not specify a suffix
{% endhighlight %}


And then in the LaTeX document use `\psfragfig{filename}` (no suffix; just the base of the filename) to
insert the figure. You'll also need to add `\usepackage{graphicx}` and `\usepackage{pstool}` to the LaTeX file's preamble.

### Links

-   [MATLAB printing and
    exporting](http://www.mathworks.co.uk/help/techdoc/creating_plots/f3-140348.html).

