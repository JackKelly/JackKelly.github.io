---
title: "Introducing NILM Metadata: a schema for energy datasets and prior knowledge about appliances"
date: 2014-06-27 10:34:39 +0000
categories: ["PhD", "nilm", "nilmtk", "metadata"]
permalink: /introducing_nilm_metadata_a_schema_for_energy_datasets_and_prior
---
![](http://nilm-metadata.readthedocs.org/en/latest/_images/schema.svg)

One of our aims with the open-source energy disaggregation toolkit
[NILMTK](http://nilmtk.github.io) is to make it easy to import any of
the 10+ NILM datasets currently available. One of the pain points when
writing a NILMTK importer for a new dataset is that each dataset uses a
different metadata schema and, sometimes, there simply is no metadata
associated with some datasets. At best, this means that we have to
manually map from the dataset's appliance names to NILMTK's standard
appliance names. At worse, it means that it's impossible to
unambiguously import the dataset (*did that channel really only include
the fridge? It sure looks like there are other appliances on there.
What's the wiring hierarchy between the mains meter, the circuit meters
and the appliance meters? Does that channel record active power or
apparent power? What pre-processing has already been applied? etc.
etc.*) <!--break-->

[NILM Metadata](https://github.com/nilmtk/nilm_metadata) is a draft
proposal for a schema and controlled vocabulary for describing energy
datasets. It also stores a set of 'central metadata'. This includes
simple stuff like the mapping from appliance type name (e.g. 'fridge')
to a set of categories (e.g. \['cold', 'large'\]) and the mapping from
country name to nominal mains voltages for that country. But we also try
to capture probabilistic prior information about variables such as the
on-duration of each appliance, the on-power of each appliance, which
appliances tend to be used with which other appliances etc. The 'central
metadata' uses a simple but powerful inheritance mechanism. For example,
a 'fridge' is a type of 'cold appliance' and inherits properties from
'cold appliance'. This inheritance allows us to minimise redundancy when
specifying the common metadata, and it also allows us to propagate prior
knowledge down the inheritance tree. For example, say we have no prior
knowledge about the times-of-day that a plasma TV is used. But we know
that a plasma TV is a subtype of a television, so we can use our prior
knowledge about televisions.

[NILM Metadata is on github](https://github.com/nilmtk/nilm_metadata),
and has a fair amount of
[documentation](http://nilm-metadata.readthedocs.org) (including a
[step-by-step guide to describe the REDD dataset using NILM
Metadata](http://nilm-metadata.readthedocs.org/en/latest/manual.html)),
and a [research paper](http://arxiv.org/abs/1403.5946).

I would dearly love for NILM Metadata to become a community project and
for folks to modify and extend it to their needs. It really is just a
draft at the moment - I'm sure there's lots missing from the current
proposal. Please go ahead and fork the project on github and submit a
pull request with your changes ([here's a guide from github on
forking](https://help.github.com/articles/fork-a-repo)). Or add ideas to
the [issue queue](https://github.com/nilmtk/nilm_metadata/issues).

Some questions on the evolution of NILM Metadata:

-   Perhaps the 'central metadata' should be [stored in a semantic
    wiki](/wiki_and_online_community_for_electricity_disaggregation)
    rather than [a set of YAML
    files](https://github.com/nilmtk/nilm_metadata/tree/master/central_metadata/appliance_types)
    to make it really easy for people to edit, and for machines to
    query it.
-   How best to represent inferred models of appliances? I've made a
    start at defining an
    [ApplianceModel](http://nilm-metadata.readthedocs.org/en/latest/central_metadata.html#appliancemodel)
    schema but it needs more thought
-   How best to represent event-based datasets? ([Mario
    Bergés](http://nilm-metadata.readthedocs.org/en/latest/central_metadata.html#appliancemodel)
    and I discussed this at the NILM Workshop in Austin (his [BLUED
    dataset](http://nilm.cmubi.org) is event-based)). Perhaps each
    ApplianceModel could enumerate every state for every appliance and
    then these states could be referenced from the event-based dataset?
    How to define a set of states for a complex appliance like a washing
    machine or a computer? Maybe we would have multiple ways to
    define states... e.g. the set of states that a human operator would
    care about (wash, spin, dry etc).


