---
title: "Current Cost and EDF EcoManager RF protocols almost fully decoded"
date: 2012-09-25 20:39:11 +0000
categories: ["PhD", "CurrentCost", "EcoManager"]
permalink: /current_cost_and_edf_ecomanager_rf_protocols_almost_fully
---
Thanks to the enormous help of Graham Murphy, Matt Thorpe and Paul
Cooper, the wiki pages for the [EDF EcoManager RF
protocol](https://github.com/JackKelly/rfm_edf_ecomanager/wiki/Technical-details-of-the-EDF-EcoManager-and-accessories)
and the [Current Cost RF
protocol](https://github.com/JackKelly/rfm_edf_ecomanager/wiki/Technical-details-of-Current-Cost-RF-protocol)
are nearing completion. Of course, jump in if you have anything to add.
Anyone with a github account can contribute.

And my [EDF EcoManager C++ AVR
code](https://github.com/JackKelly/rfm_edf_ecomanager) is ticking along.
Still some distance from being usable "in the field" but getting there.

One quick random thought: for those of us who have been tinkering with
the Current Cost RF protocol, it appeared rather odd that the data is
"manchesterised". It occurred to me this afternoon that we can take
advantage of this structure in the data to validate the data. A little
more discussion on [the
wiki](https://github.com/JackKelly/rfm_edf_ecomanager/wiki/Technical-details-of-Current-Cost-RF-protocol#wiki-The_data_is_Manchester_encoded).

### UPDATE 30/10/2012

Current Cost have asked me to remove the protocol documentation from the
wiki. More details [here](/deleted_current_cost_protocol_documents).

### UPDATE 5/1/2016

Current cost have kindly allowed me to put the docs back onto [the
github wiki](https://github.com/JackKelly/rfm_edf_ecomanager/wiki/)!
<!--break-->

