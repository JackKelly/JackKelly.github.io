---
title: "A new language for mathematical computing: Julia"
date: 2012-04-26 12:14:48 +0000
categories: ["programming"]
permalink: /a_new_language_for_mathematical_computing_julia
---
> Julia is a high-level, high-performance dynamic programming language
> for technical computing, with syntax that is familiar to users of
> other technical computing environments. It provides a sophisticated
> compiler, distributed parallel execution, numerical accuracy, and an
> extensive mathematical function library. The library, mostly written
> in Julia itself, also integrates mature, best-of-breed C and Fortran
> libraries for linear algebra, random number generation, FFTs, and
> string processing. 

More info: [The Julia Language](http://julialang.org/) and [Why We
Created
Julia](http://julialang.org/blog/2012/02/why-we-created-julia/) and [A
Matlab Programmer's Take on Julia](http://2pif.info/op/julia.html).
 Sounds pretty awesome.

Incidentally, the third link includes a quote which pretty much exactly
captures my current feelings about Matlab:

> The Matlab language is slow, it is crufty, and has many
> idiosyncracies... I strongly disagree, however, with the opinion,
> common among some circles, that Matlab is to be dismissed just because
> it is crufty or "not well designed". It is actually a very productive
> language that is very well suited to numerical computing and algorithm
> exploration. Cruftiness and slowness are the price we pay for its
> convenience and flexibility.

I fundamentally disagree with the last statement though.  Cruftiness and
slowness *should not be the price we pay* for convenience and
flexibility.  Matlab could've been designed to be *both*
high-performance *and* productive.  For example: one source of slowness
and cruftiness is that objects are usually passed by value, not by
reference (yes, I know MATLAB does copy-on-write... which is great...
until you want to write to an object).  I think that defaulting to
pass-by-value is simply a design mistake.  Pass by reference wouldn't
prevent MATLAB from doing the things it does, and would make it faster.

<!--break-->

