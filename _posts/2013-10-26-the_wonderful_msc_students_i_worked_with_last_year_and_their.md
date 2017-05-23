---
title: "The wonderful MSc students I worked with last year and their award-winning projects ;)"
date: 2013-10-26 19:09:10 +0000
categories: ["PhD", "student project"]
permalink: /the_wonderful_msc_students_i_worked_with_last_year_and_their
---
This spring and summer I had the opportunity to work with some
exceptional MSc students at Imperial and I just wanted to write a
summary of their achievements.

MSc group project in Spring 2013
================================

Visualisation and Analysis of Domestic Electrical Energy Consumption
--------------------------------------------------------------------

In spring 2013, my PhD supervisor and I proposed an MSc computer science
group project on "Visualisation and Analysis of Domestic Electrical
Energy Consumption" ([here's the original project
proposal](http://www.doc.ic.ac.uk/~dk3810/VADEEC_proposal.html)). A very
enthusiastic and creative group showed great interest in the project
very early in the process and I was thrilled that they selected the
project. The group members were Andrei Petric (who stayed at Imperial to
do an advance MSc), David Sgorbati, Dave Wei (who stayed at Imperial to
do a PhD on network intrusion detection), Javier Zunzunegui,
Konstantinos Kamnitsas (who did an individual project with me in summer
and won Best Individual Project) and [Rebecca
Jones](http://rebeccaajones.wordpress.com/) (group leader). Their end
product and report were far better than I had hoped; they successfully
blended a mixture of technologies (including Python, D3.js, MongoDB and
HTML5) to create a visually appealing, effective and well designed web
app for monitoring energy usage from multiple appliances. Yesterday it
was confirmed that Becky's group were joint winner (with one other
group) of the Department of Computing's Best MSc Group Project Prize of
2013, which they definitely deserved.

Individual projects in Summer 2013
==================================

Room Occupancy Prediction for Smart Homes
-----------------------------------------

Shubhangi Harsha did a very well structured and thorough exploration of
algorithms for 1) detecting room occupancy from noisy PIR sensor data
and 2) predicting room-by-room occupancy. Here's her abstract:

> Space heating in homes is accountable for approximately 66% of the
> total energy consumption of domestic sector in Great Britain while
> more than 25% of the nation’s energy is consumed in this sector
> \[15\]. Residential heating equipment operates for most of the year in
> the majority of homes. Often, radiators are left switched on even when
> there is no occupant in a room. Even if people are aware and cautious
> about energy wastage, they tend to forget to turn the radiators off.
> These facts highlight the need to automatically control radiators by
> detecting presence of an occupant in the room and thereby
> substantially reduce wastage of energy. Specific to automating heating
> equipment, it would be desirable to know a few hours before the room
> is actually occupied so as to switch on the radiators automatically
> and achieve a comfortable temperature before the occupant arrives.
> This gives rise to the need for occupancy prediction. The project
> ‘Room Occupancy Prediction for Smart Homes’ aims at predicting
> occupancy of each room of a house from the observed output of Passive
> Infrared (PIR) motion sensors installed inside the room.\
> \
> This report presents a detailed methodology of predicting occupancy of
> each room of a house based on the pattern of output of PIR sensors.
> Due to the non-availability of sufficient occupancy data from PIR
> sensors, such data was simulated for different types of households and
> occupancy patterns. Details of the simulation process and the data
> simulator developed for this purpose are discussed in the report. PIR
> sensors only detect motion and fail to represent actual occupancy in
> situations where the occupant performs little or no movement. A
> classification of rooms on the basis of the level of activity expected
> is proposed and has been named as the Transitive, Active, Inactive,
> Dormant (TAID) Classification. Knowledge of the number of residents of
> a house can aid in inferring occupancy more accurately and an
> algorithm to learn the number of occupants from PIR sensor data has
> been developed and stated in the report. An algorithm to infer actual
> occupancy from PIR sensors data that takes into account the proposed
> TAID classification and number of occupants is presented. Occupancy
> inference accuracy of 90-97% has been obtained using this algorithm.\
> \
> Markov, linear regression and logistic regression models suit the
> sequential time-series nature of PIR sensors data and have, therefore,
> been explored for predicting occupancy. Occupancy prediction
> algorithms developed for these three models are stated and described
> in detail in this report. The report also discusses analysis of
> occupancy prediction results obtained for each of these models and for
> several different types of data sets. An integrated system has been
> developed to simulate PIR sensor-output data, infer occupancy and
> finally, predict occupancy. Functional and implementation details of
> this system are presented in this dissertation.

IntellyRPi: A Smart Home Automation Server
------------------------------------------

Sokratis Dafnis built a home automation server on a Raspberry Pi and
designed his own language for home automation. He finished his original
aims ahead of time and went on to investigate ways to predict appliance
usage from past experience. Here's the abstract from his report:

> The dawn of smart homes was restricted in the scientific field of home
> automation, while their commer- cial solutions where considered a
> luxury. During the last few years, however, smart homes have turned
> into a necessity and, nowadays, they attract public interest. The
> first step towards this direction was the introduction of network
> enabled technology together with the use of smart home appliances.
> These technologies facilitate home automation and monitoring of
> appliances, and can help us gain a better overview of user behaviour
> and energy patterns.\
> \
> By investigating, understanding and optimizing our energy consumption
> behaviour, we can cut down the cost of electricity and reduce harmful
> gas emissions into the atmosphere. Apart from the economical and
> environmental benefits, home automation aims to improve the residents’
> everyday life. The ultimate target of a home automation system is to
> be able to learn user habits and replicate them, without requiring
> user’s intervention. This function would reduce the load on the user,
> by discovering individual patterns in appliance usage and correlation
> patterns between different appliances.\
> \
> This project aims to build an intelligent home automation server
> (intellyRPi), whose core hardware component is a raspberryPi. From the
> software side, the server contains two powerful components: a home
> automation language, designed specifically for this application, and
> an integrated prediction engine, which models appliance usage
> patterns. In addition, the server includes a web interface which
> allows users to test and control appliance status and monitor
> appliance power consumption.\
> \
> The home automation language is a parallel, event-driven and
> concurrent language, lying on top of a distributed component
> architecture. Furthermore, the language uses the server’s embedded
> scheduler and an event dispatcher. The main task performed by the
> scheduler is controlling appliances, while the event dispatcher is
> responsible for firing events triggered by home automation scripts.
> The design of its statements renders the language simple and powerful,
> and, at the same time, bridges the gap between the user and the
> automatic system.\
> \
> The integrated prediction engine analyses historical data regarding
> appliance usage in a certain home, and recognizes patterns in these
> datasets. It is based on a density-based spatial clustering algorithm,
> DBSCAN, and combines it with probability theory principles to produce
> more accurate and robust results. Three different approaches were
> implemented and juxtaposed, in order to highlight the process that
> would lead to the most accurate predictions. The first approach was
> the most general one and detected appliance clusters regarding a day
> as a total. The second approach was similar to the previous one, but
> the output clusters are categorized based on the weekday. Finally, the
> last approach enhances the second one by calculating the clusters in a
> one hour time window and provides the system with more accurate
> predictions.\
> \
> The prediction engine translates the predictions to intellyRPi home
> automation language scripts, which are sent to the server for
> execution. This constitutes the key attribute of the home automation
> system, which aims to facilitate user’s everyday activities in the
> house and follow the resident’s habits. The highest performance
> recorded between the alternative prediction models was achieved by the
> third, more sophisticated approach. A set of 26 weeks with high
> temporal resolution (6 seconds) was used for the training of the
> engine, and the prediction accuracy achieved on 10 week dataset was
> 71%. These datasets contained a subset of 14 devices, which were the
> most likely to be correlated with each other.

Inferring Appliance-by-Appliance Energy Consumption from Whole-House Electricity Meter Readings
-----------------------------------------------------------------------------------------------

Konstantinos Kamnitsas's project was basically to do my entire PhD in 3
months. And he pretty much succeeded! I was amazed at how much work he
did in the 3 months. And, not surprisingly, he won the Winton Capital
Prize for the Best MSc Individual Project. Utterly deserved. Here's the
abstract from his report:

> Energy conservation has been in the forefront of attention for quite
> some time. The climate change, the continuously increasing energy
> demands and the limited availability of energy resources have made
> several bodies look for means to achieve more efficient energy
> consumption. National targets have been set in order to limit the
> environmental effects of fossil fuel consumption. The residential
> sector accounts for a big part of the global energy consumption
> (approximately 26% for the UK). In order to monitor the national
> energy consumption, as well as motivate home owners to improve their
> electricity consumption behaviour, smart-meters are being deployed in
> a large scale in the UK and the USA.\
> \
> A smart-meter is connected to the electric main of a residence and
> monitors the energy con- sumption of the whole house. The collected
> data are of great value; it may allow for prediction of the national
> load and enable optimization of the power grid or enable the utility
> companies to provide better services to their clients. Of great
> interest is the extraction of detailed information from this data
> regarding the electricity usage of consumers. Electricity is at the
> moment an ’invis- ible’ product, in the sense that it is rather hard
> to estimate how much is consumed and by which appliance. Providing
> more detailed information than simply a monthly bill to the consumers
> would enable them to get control over their electricity consumption
> and make wiser use of it.\
> \
> The task of extracting end-use and appliance-level information from
> the measurements of the whole-house consumption, the aggregate signal,
> is referred to as energy disaggregation. It has been the target of
> research attempts for over 20 years. However, there has not been
> developed a robust and accurate technique that could be widely adopted
> in the residential sector yet. The developed systems either require
> special equipment or have important limitations.\
> \
> This research elaborates on the disaggregation of multi-state
> appliances that are commonly found in residences. Multi-state
> appliances are problematic to disaggregate using classic approaches,
> which are based only on the detection of steady states in the power
> signal, because of the compli- cated nature of their operation.\
> \
> A novel supervised pattern recognition technique has been developed,
> inspired by feature extrac- tion techniques used in Optical Character
> Recognition. The designed system attempts to determine the
> ’approximate shape’ of the signatures (the measured power consumption
> of the appliance dur- ing one single operation) of a multi-state
> appliance by detecting the main parts that they consist of. By
> processing the signatures of various models of the same appliance
> type, the system attempts to extract patterns and features that are
> frequently observed during the operation of an appliance. The
> extracted set of features comprises the profile of an appliance, which
> describes the generic shape of a multi-state appliance’s signatures.
> It is an attempt towards the creation of a generic signature of an
> appliance, that may describe the appliance type as a whole,
> independent of the model’s size, manufacturer or other such factors.\
> \
> Most previous research attempts performed on data sampled at the
> frequency range of 1Hz- 0.1Hz only extract the power consumed during
> steady states of an appliance’s operation. In this work various
> features have been investigated, in order to determine a richer set
> that can accurately describe an appliance, allowing its detection and
> at the same time distinguish it from the rest. The investigated
> features include durations of states, time intervals between different
> states, repeating parts in an appliance’s signature, periods of rapid
> changes created by an appliance’s operation, power changes with the
> form of spikes and more. Signatures of different models of appliances
> have been processed, available in various public datasets. Three
> multi-state appliances were the main targets of this work: the
> dishwasher, the washing machine and the dryer.\
> \
> A system has been implemented in order to extract the various
> features, generate the profile of each appliance and, finally, test
> the approach by disaggregating operations of these appliances. The
> profiles generated manage to describe the generic characteristics of
> an appliance, allowing the system to detect fairly accurate instances
> of all three appliances in an aggregate signal (50-100% disaggregation
> accuracy in the tested cases). The results were particularly promising
> taking into account the very low number of false positives (83-100%
> detection accuracy in the tested cases), fact that may allow for
> further extensions to this work.

Summary
=======

In summary, I was extremely privileged to both have a PhD supervisor
([Dr Will Knottenbelt](http://www.doc.ic.ac.uk/~wjk/)) who is so
supportive of both his PhD and MSc students; and also to have been given
the opportunity to work with such intelligent, creative and hard-working
MSc students.

