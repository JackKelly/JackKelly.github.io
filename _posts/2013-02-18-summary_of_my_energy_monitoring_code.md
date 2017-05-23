---
title: "Summary of my energy monitoring code"
date: 2013-02-18 16:01:17 +0000
categories: ["PhD", "CurrentCost"]
permalink: /summary_of_my_energy_monitoring_code
---
This is just a quick summary of the code I've been working on recently.
The ultimate aim of all the code is to measure the whole-house
electricity consumption and the consumption of individual appliances as
cost-effectively as possible.

<span class="flickr-wrap" style="width:640px;"><span
class="flickr-image">[![](https://farm9.staticflickr.com/8379/8464804957_90456ed112_z.jpg)](https://www.flickr.com/photos/37816297@N06/8464804957)</span></span>

-   [rfm\_edf\_ecomanager](https://github.com/JackKelly/rfm_edf_ecomanager) -
    C++ code for running on a [Nanode](http://www.nanode.eu/) (an
    Arduino clone with easy wireless support and networking). This code
    allows the Nanode to talk directly to multiple Current Cost
    whole-house sensors (CC TXs) as well as to multiple [EDF Transmitter
    Plugs](https://shop.edfenergy.com/Item.aspx?id=540&CategoryID=1)
    (CC TRXs). This code aims to capture data from the sensors as
    reliably as possible. For example, it learns when each CC TX is due
    to transmit and ensures that it stops polling the CC TRXs for a
    short window of time around the CC TX's ETA. You talk to the Nanode
    over the serial port. You can send simple commands. It sends data
    back to the PC in a simple JSON format.
-   [rfm\_ecomanager\_logger](https://github.com/JackKelly/rfm_ecomanager_logger/) -
    A Python script for communicating with the rfm\_edf\_ecomanager
    Nanode system. rfm\_ecomanager\_logger provides a command-line tool
    for "pairing" sensors with the logging system; assigning
    human-readable names to those sensors and then logging the data in a
    [REDD](http://redd.csail.mit.edu/)-formatted form. Again, the
    emphasis is on reliable logging. It attempts to restart the Nanode
    if it dies. It goes to quite a lot of effort to make sure we
    correctly time stamp data (which is surprisingly difficult,
    especially given that the Nanode doesn't have a real time clock).
-   [babysitter](https://github.com/JackKelly/babysitter) - A Python
    module for "babysitting" a logging system. Sends an email if a
    sensor dies or if rfm\_ecomanager\_logger fails. Also sends a
    "heartbeat" email once a day with some stats and a graph produce by
    powerstats:
-   [powerstats](https://github.com/JackKelly/powerstats) - Produce
    stats and graphs from [REDD](http://redd.csail.mit.edu/)-formatted
    power data. Mainly used for checking the health of sensors.
-   [snd\_card\_power\_meter](https://github.com/JackKelly/snd_card_power_meter) -
    System for recording voltage and current waveforms at 96 khz, 20 bit
    per channel using a PC's sound card. Saves down-sampled high
    frequency data and also calculates real power and apparent power.

Also, I wrote [a long guide to setting up a complete logging
system](https://github.com/JackKelly/rfm_ecomanager_logger/wiki/Build-a-complete-logging-system)
which uses all the code listed above and is based on a small, low-cost,
low-power Intel Atom system running Ubuntu Server.

<!--break-->

