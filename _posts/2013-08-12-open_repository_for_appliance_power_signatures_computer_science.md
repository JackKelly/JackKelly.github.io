---
title: "Open repository for appliance power signatures:  computer science group project proposal"
date: 2013-08-12 12:03:15 +0000
categories: ["PhD", "disaggregation", "student project"]
permalink: /open_repository_for_appliance_power_signatures_computer_science
---
Here's another draft proposal for a computer science group project that
I'm thinking of submitting...

------------------------------------------------------------------------

Introduction
------------

As energy costs increase, there is increasing pressure to use energy as
efficiently as possible. The first step towards reducing energy
consumption is often to *measure* your existing consumption. There is
good evidence that people are best able to manage their energy
consumption if they are given an itemised energy bill describing
appliance-by-appliance energy consumption information (e.g. "your fridge
cost you £50 this month and your TV cost you £20").

Automatically estimating an itemised energy bill by "disaggregating" a
whole-house smart meter signal is an active area of research. One
approach to this problem requires that the disaggregation system be
trained on existing appliance "signatures" (recordings of the power
consumption of an individual appliance). A web service which allows for
appliance signatures to be programmatically retrieved and submitted
would be very useful both to enable automatic disaggregation systems and
also to encourage research into disaggregation.

The Challenge
-------------

The aim of this project would be to build a web application to allow
appliance signatures to be submitted, categorised, analysed and
retrieved.<!--break-->

Some features you could play with:

-   allow users to submit new signatures using a web interface
-   allow users to search for and display signatures using a simple
    web interface. It would be especially useful to be able to compare
    multiple instances of the same type of appliance (e.g. to see common
    features in washing machine signatures, sorted by criteria such as
    country of origin).
-   An API would be essential to allow disaggregation systems to
    programmatically retrieve signatures from the DB and to insert
    new ones.
-   Accept a range of sample rates and data dimensions (e.g. collect not
    just active power but also reactive power for each appliance and
    whether the reactive power is capacitive or inductive)
-   It would be useful to collect some metadata for each appliance
    signature, e.g.:

    -   Appliance make, model, age
    -   Appliance category ("TV", "fridge", "desktop PC", "washing
        machine" etc). This could be auto-completed if a previous
        appliance with the same make & model was given a category).
    -   Mode (e.g. "40 degree spin wash", "eco-mode" etc)
    -   rough geo location (so external temperatures can be obtained
        from the metoffice; and so country can be determined: UK washing
        machines behave quite differently to US washing machines)
    -   timestamp (so signatures can be aligned with aggregate data,
        where available); and so time-of-day dependencies can
        be analysed.
-   This appliance DB could also be used to store anonymised whole-home
    aggregate datasets along with continuous recordings of
    individual appliances.

-   Could also calculate and present (graphically and programmatically)
    usage patterns for each category, e.g.:

    -   average daily pattern of usage
    -   seasonal variation
    -   correlation with weather variables

Further reading
---------------

-   [TraceBase](http://www.tracebase.org/) is the nearest that we
    currently have to an online database of appliance signatures. It's a
    great start. But it doesn't allow users to submit new signatures or
    allow disaggregation systems to programmatically
    download signatures.


