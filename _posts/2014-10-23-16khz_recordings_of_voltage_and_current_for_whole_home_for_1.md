---
title: "16kHz recordings of voltage and current for whole home for >1 year available"
date: 2014-10-23 07:14:57 +0000
categories: ["UK-DALE"]
permalink: /16khz_recordings_of_voltage_and_current_for_whole_home_for_1
---
Our 'UK Domestic Appliance-Level Electricity (UK-DALE)' dataset was
released earlier this year ([here's our paper on the
dataset](http://arxiv.org/abs/1404.0284)). Up until now, the data
available consisted of data recorded every second (for the whole house
power demand of two houses) or recorded every six seconds (for all
appliance-level data and the whole-house demand for all four houses).
But I also recorded voltage and current at 16kHz for two houses. I have
finally gotten round to figuring out how to put almost 4 TBytes of data
online.

The 16kHz signal is compressed as FLAC and is available in 1 hour chunks
(each chunk is about 200 MBytes in size). You can download it using
anonymous FTP. Details [here](http://www.doc.ic.ac.uk/~dk3810/data)
under the section 'The full 16 kHz dataset via FTP'.

And, while we're on the topic of updates to UK-DALE, a little while ago
I updated the metadata for UK-DALE to bring it into line with the new
[NILM Metadata v0.2
schema](http://nilm-metadata.readthedocs.org/en/latest), and I also
updated the [NILMTK converter for
UK-DALE](https://github.com/nilmtk/nilmtk/tree/master/nilmtk/dataset_converters/ukdale).
<!--break-->

