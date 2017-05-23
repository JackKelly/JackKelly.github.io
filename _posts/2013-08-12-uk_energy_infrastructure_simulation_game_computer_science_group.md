---
title: "UK energy infrastructure simulation game: computer science group project proposal"
date: 2013-08-12 10:48:01 +0000
categories: ["PhD", "student project", "energy efficiency"]
permalink: /uk_energy_infrastructure_simulation_game_computer_science_group
---
Here's a draft proposal for a computer science group project that I'm
thinking of submitting...

------------------------------------------------------------------------

Could we power the entire of the UK electricity grid on renewables
alone? What about a mixture of nuclear and renewables? How much would
this scenario cost to build? Or what about going to the other extreme
and switching our power generation to 100% coal? What implications would
that have?

Discussions about energy are becoming quite common in the media.
Questions like those listed above are frequently asked but it's hard to
find good answers. One of the big problems in communicating energy
issues to the wider public is that people have little sense of the
scales involved.

The aim of this project will be to build a kind of "SimCity" game to
allow members of the public to explore different energy scenarios for
the UK (or for the whole world if you're feeling very ambitious!). Users
would be allowed to input any scenario and the game would simulate the
consequences. Points are lost for triggering power blackouts or
excessive environmental damage. <!--break--> A random selection of
things you could play with (none of these are compulsory!):

-   variables that users can modify (the range limits for each variable
    should be physically realistic; e.g. don't allow users to add more
    off-shore wind turbines than we have available coastline):
    -   power generation mix (x% renewables, y% nuclear, z% gas etc.)
    -   grid storage (electric car batteries etc)
    -   modifications to load (Add 10 million electric cars? Replace 50%
        of the nation's gas boilers with ground source heat pumps?
        Replace all incandescent lights with LEDs?)
    -   population
    -   remove / add industrial users like steel fabrication works etc
-   Output the financial and environmental implications for each user
    defined scenario
-   simulate grid load based on historical power data (see the section
    below on "Sources of data") and add simulations for likely future
    trends like efficient lighting, electric cars and electrified
    heating
-   Add a "disaster" button which randomly throws in extreme events like
    very cold winters, floods or terrorism knocking out large numbers of
    power stations, sudden price spikes in the cost of gas / uranium
    / oil.
-   Automatically generate alarmist tabloid headlines(!) (e.g. see the
    "[Daily Mail-o-Matic](http://www.qwghlm.co.uk/toys/dailymail/)"
    automatic headline generator)
-   Include "pre-set" scenarios e.g. energy scenarios from various
    political party's manifestos and from groups like Greenpeace (is it
    really practical to turn off all nuclear?)
-   Automatically generate scenarios which optimise certain
    criteria (e.g. a user could opt to minimise cost or minimise
    environmental impact)
-   You could use Sankey diagrams to visualise the flow of energy
    through the system, see [these examples of energy use in 2007 and
    projected use in
    2050](http://www.sankey-diagrams.com/uk-2050-energy-flow-sankey-diagram/).

Scope of this project
---------------------

One of the fun but dangerous aspects of this project is that you could
easily spend many years developing this project. But, on the other hand,
you can make significant progress with nothing more complex than an
Excel spreadsheet. In other words: the scope of the project can scale
from relatively simple to a huge beast. My recommendation would be to
start with relatively modest ambitions and add complexity only if time
allows.

Sources of data and information
-------------------------------

-   Prof David MacKay's excellent book "[Sustainable Energy without the
    Hot Air](http://www.withouthotair.com/)" (available free online and
    I have a paper copy I can lend you)
-   DECC's "[2050 pathways
    calculator](http://2050-calculator-tool.decc.gov.uk)" and the
    associated [My2050 game](http://my2050.decc.gov.uk/) - see the
    comments for some discussion of DECC's "My2050" game; and many
    thanks to Oli for mentioning My2050!
-   We have been collecting power data from 5 homes, including from many
    individual appliances.
-   The UK government have collected individual appliance power data
    from 250 homes in their [Household Electricity
    Study](http://randd.defra.gov.uk/Default.aspx?Menu=Menu&Module=More&Location=None&Completed=0&ProjectID=17359).
-   [AMEE](https://www.amee.com/) - free data on the environmental cost
    of lots of products and actions


