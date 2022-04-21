---
layout: post
language: en
title: Data Factory
tag: ["Bachelor thesis", "Reserved"]
category: project-ideas
---

Some form of data processing is a common task in almost any computer-related activity.
For example, a machine learning project may employ a pipeline/workflow, to extract data, transform data and train a model.
Implementation of the pipeline can be simple in the production environment.
However, during the development phase, many different pipelines may need to be tested.
Management and execution of those pipelines can be a tedious task.
The objective is to make this task easier.

<!-- more -->

The idea is to create software (*Data Factory*), that would allow a user to define and compute so-called *data entries*.
A simple *data entry* can be a local file or remote source of data. 
In addition, a new data entry can be produced using arbitrary software from existing *data entry*. 
Each *data entry* has accompanying metadata, called *definition*, that allows reproducible recomputation of a given *data entry*.

Given a list of *definitions*, the *Data factory* will compute the *data entries*.
The concept is similar to the ETL, but they focus on different use cases.
ETL focus on running mostly isolated pipelines on changing data.
*Data Factory* should help during the development phase of machine learning methods. 
Where a lot of pipelines is developed and tested on the same data.
As such, the focus is on reproducibility,  integration, re-use, and sharing of existing data.
