---
title: "Size of Arduino number types"
date: 2012-12-14 11:03:29 +0000
categories: ["Arduino", "software engineering"]
permalink: /size_of_arduino_number_types
---
The size (in bytes) of some number types on an Arduino (some of these
are obvious):

<pre>
  ----------------------
  char                1
  byte                1
  int                 2
  size_t              2
  unsigned int        2
  short int           2
  long int            4
  long long int       8
  unsigned long int   4
  float               4
  double              4
  ----------------------
</pre>

<!--break-->

