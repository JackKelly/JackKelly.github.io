---
title: "Two levels of applying machine learning to solar power forecasting"
categories: [open climate fix, machine learning, climate change mitigation, software engineering]
---

I'd like to propose that there are two broad "levels" of applying machine learning to solar power forecasting. 
The first level is relatively easy, and everyone is doing it: I don't know for sure, but I'm almost certain that 
"level one ML" is what almost all power forecasting providers mean when they say they're "using AI"
in their glossy sales brochures! The second level is _much_ harder to achieve, but may provide 
better forecasting skill (especially at forecast horizons up to a few hours ahead).

"Level one" approaches learn a "power curve" which maps from numerical weather predictions (NWPs)
to solar power. The simplest approach would be to use linear regression to map from NWP irradiance to solar power, 
using NWP data from the NWP grid box closest to the solar PV site. (And this works surprisingly well!)
Or, to get a little fancier, folks train something like an XGBoost model that includes features such as:

* statistics from the last few days of solar power data, 
* NWPs from a handful of NWP grid boxes near to the target site, 
* NWPs from multiple NWP providers, 
* tilt & azimuth of the PV panels, 
* PV power forecasts from a physical model (e.g. from [pvlib](https://pvlib-python.readthedocs.io/en/stable/)).

These "level one" ML models don't attempt to learn atmospheric physics, or how clouds move, or how to interpret satellite images.
They're just trying to learn relatively simple relationships between a handful of input features, and PV power.
So it makes sense to use relatively simple models (linear regression, multilayer perceptrons, XGBoost, etc.).
But "level one" approaches are always limited by the forecasting skill and resolution of the NWPs.
And there are good reasons to believe that operational NWPs aren't great at forecasting irradiance.

"Level two" approaches try to use machine learning to out-perform NWPs.
Here, we _do_ want our ML model to learn atmospheric physics, and to interpret rich data sources.
For example, the ML model might try to predict how clouds evolve over the next few hours, 
given satellite imagery of the last few hours of clouds (this was the task in
[the ML competition that Open Climate Fix helped to organise](https://twitter.com/OpenClimateFix/status/1509510989213020160)). Or, for forecasts which extend days
into the future, you could imagine learning to infer irradiance (at the Earth's surface)
from NWP humidity and temperature at the altitude of clouds (because operational NWPs are pretty good at predicting humidity and temperature, 
but take a bunch of short cuts when predicting clouds and irradiance.)
Papers like [Google Research's MetNet-2 paper](https://ai.googleblog.com/2021/11/metnet-2-deep-learning-for-12-hour.html) (2021)
and [DeepMind's Precipitation Nowcasting paper](https://www.deepmind.com/blog/nowcasting-the-next-hour-of-rain) (2021)
demonstrate that this class of approach is _possible_: it is possible to train an ML model to predict weather variables, 
and the ML predictions are often better than NWPs (especially at short forecast horizons).
But it takes a _lot_ of data, compute, skill, time, and effort to pull this off.

Personally, I'm most interested in the "level two" approaches. Although, I'll admit, it's far harder to achieve than I originally thought!
And I'll also admit that, for many users, a good "level one" approach is probably sufficient. But, I do still cling to the hope that good "level two"
approaches could be really helpful for some folks (especially electricity grid system operators).

At Open Climate Fix, we're doing both "level one" and "level two".
