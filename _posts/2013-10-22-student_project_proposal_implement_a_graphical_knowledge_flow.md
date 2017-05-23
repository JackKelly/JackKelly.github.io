---
title: "Student project proposal:  Implement a graphical \"knowledge flow\" interface for the Python machine learning toolkits scikit-learn and/or PyLearn2"
date: 2013-10-22 21:05:31 +0000
categories: ["PhD", "student project"]
permalink: /student_project_proposal_implement_a_graphical_knowledge_flow
---
The Java machine learning toolkit
[Weka](http://www.cs.waikato.ac.nz/ml/weka/) includes a "knowledge flow"
editor which allows users to very quickly assemble data processing
"circuits":

![](http://www.siliconafrica.com/wp-content/themes/directorypress/thumbs//weka.png)
<!--break--> Similarly, the machine learning toolkit
"[Orange](http://orange.biolab.si/features/)" includes an interface they
call "Canvas" for graphically wiring together machine learning
components:

![](http://orange.biolab.si/screenshots/snp-schema-selection-evaluation.png)

The aim of this project would be to implement a similar "graphical
programming" interface for either
[scikit-learn](http://scikit-learn.org/stable/) (a general-purpose
machine learning library for Python) or
[PyLearn2](http://deeplearning.net/software/pylearn2/) (focussed on
efficient GPU implementations of deep neural networks). For example, it
might be nice to be able to graphically specify a deep neural network
that is then run on the GPU. Perhaps your interface could integrate with
the [iPython Notebook](http://ipython.org/notebook.html).

