# Hackathon Projects Description

The goal of this document is to provide you with enough details to choose a project for our end-of-semester hackathon event. Once you decide on your favorite projects head over __[here]()__ and rank them. All students should rank their preferences, even those who informed me that they couldn't attend.

## General Information

The event will take place during the week of __*******__. We will have a starting Zoom session on __*****__ that will provide with a few extra details and general guidance for the event, and then you'll be off on your way. We will not have a closing session together.

Before that week you'll each be assigned to a project based on your preferences; the number of students per project varies. This group of students will have a zoom meeting with their mentor, i.e. the person who can describe best the goals of that specific project, a few days or weeks before the start of the event. That meeting should provide you with all the details you need to start working, including assigning each student to a specific goal of the project. 

Each group will also be added to a Slack workspace, and have their own channel to discuss things, raise questions to their mentor, and monitor the general progress of the project. To join the Slack workspace click __[here]().__ You probably also want to download their app if you don't have it already.

After the week is done, each group should have a git repo with the final, working version of their app. This repo should be accompanied by an exhaustive README document which gives the overarching view of the project. The project should also have documentation that is clear, readable and can help the mentor use the app on their own device easily. Information on the technical side of these requirements can be found the course's notebooks.

### Grading

40% - Code quality - proper code structure, usage of libraries, tests, git, PyPI.

20% - Does it work?

40% - Team collaboration and documentation of the code.


## Project 1: Wake/Sleep State Assessment
### Mentor: Dr. Anan Moran

This project's goal is to find wake and sleep states in rats from electrophysiological data by using machine-learning based tools. The provided data comes from Anan's rats, which were implanted with electrodes that recorded extracellular activity for 24 hours. The data is huge (several TBs), so a large part of the project is using libraries which allow processing of out-of-memory arrays. The data will have to be filtered using basic signal analysis techniques, and then fed into some classifier (probably a type of a Support Vector Machine) which will (hopefully) learn to identify the different arousal states from the labeled data Anan will also provide.

#### Number of students per project: 2-3
#### Relevant libraries: `scikit-learn`, `dask`, `scipy`

## Project 2: Biomechanical Testing Analysis
### Mentor: Prof. Yankel Gabet

In this project you will analyze data generated from biomechanical testing experiments done in the mentor's lab. Students will have to plot the measured data and in phase one should let the users mark a few key areas on that curve, as well as choose the current experiment type. After the user marks these areas the application will calculate a few key parameters of that stress-strain curve and save them to disk in an appropriate format. In a later phase you'll try to automate the detection process of different areas so that it could run automatically, with minimal input from the user.

![Typical graph](prj2_graph.png)

#### Number of students per project: 2
#### Relevant libraries: `pandas`, `seaborn`, `scipy`

## Project 3: Better Feedback for Neurofeedback
### Mentor: Prof. Tamar Bar Shalita, Gil Issaschar

Prof. Bar Shalita's lab developed an EEG-based neurofeedback app which may help treated subjects with a variety of disorders. The system analyzes the EEG data in real time and shows the subjects a task that they should complete by modulating their own EEG signal. The way the system shows the subjects whether they're improving or not is by having them attempt inserting a ball into a rectangle on a computer screen in front of them. The lab would like to improve and extend the different visual and auditory outputs of the system, so that they could possibly test and find the best type of visual signal in neurofeedback-based tasks. Thus, the two main goals here are to create a robust interface to the existing system which outputs the data, analyze this data in real time and finally create and update the proper visual and auditory cue as the data flows.

#### Number of students per project: 2-3
#### Relevant libraries: `scikit-image`, `numpy`, `matplotlib`

## Project 4: Graphical Epidemic Simulation
### Mentor: Hagai Har-Gil

This project has no direct impact on some existing research; rather it's an exercise in simulating an epidemic with a SIR-type model. SIR stands for _susceptible_, i.e. haven't been infected, _infectious_ and _removed_. Each agent is in one of these three phases, and your goal is to move them randomly through their neighborhood and see how the disease spreads. The parameters of the epidemic - how infectious is it, what is the maximal radius for infection and so on - should be user controllable, which will help us understand the significance of some of the more obscure parameters of this disease. You should show both the way each agent moves on the grid (points on a canvas) and some metrics for the number of infections, infection rate and so on. The idea is to re-create some parts of the fantastic ThreeBlueOneBrown video linked [here](https://www.youtube.com/watch?v=gxAaO2rsdIs), although our visualizations will be a bit simpler.

#### Number of students per project: 2-3
#### Relevant libraries: `bokeh`, `numpy`

## Project 5: Graph-based Epidemic Spread
### Mentor: Dr. Pablo Blinder


#### Number of students per project: 2
#### Relevant libraries: `networkx`

## Project 6: Membrane Detection and Analysis
### Mentor: Mirna Safieh, Lab of Prof. Daniel Michaelson

The project revolves around a computational pipeline which is aimed at detecting and analyzing images of neurons and their membranes taken by a confocal microscope. The research question requires us to detect the outer membrane of each neuron, and to analyze the amount of fluorescence coming from that area following immunohistochemical staining which was done in the lab. The data will be analyzed statistically for a number of parameters. The other part of the project, the one not dealing with image analysis, deals with the construction of an effective computational pipeline that can efficiently process many images in parallel.

#### Number of students per project: 2
#### Relevant Libraries: `pandas`, `scikit-image`, `dask`

## Project 7: Tracking Analysis of Fluorescent Images
### Mentor: Mirna Safieh, Lab of Prof. Daniel Michaelson

fsfsdfsfsd

#### Number of students per project: 2
#### Relevant libraries: `pandas`, `scikit-image`, `opencv`

