---
layout: post
language: en
title: Data factory
tag: ["Bachelor thesis", "Diploma thesis"]
category: projects-ideas
---

Data processing is a common task in almost any computer-related activity.
For example, data scientists employ data pipelines, also called workflows, to prepare data from machine learning methods.
Scientists routinely process and analyze data with various levels of automation.
Data pipeline can be simple as running a bash script or as complex as running distributed streaming processing.

As science is an exploratory process, scientists often experiment with different data pipelines and datasets.
As a result, many different pipelines need to be designed, implemented and tested. Management and execution of those pipelines is a labour-intensive process.

Yet with proper toolset support, we should be able to make this process approachable and even increase the productivity of the researchers.


<!-- more -->

The idea is to implement this toolset. 
Yet, it is clear that the toolset can compose of multiple tools to address different requirements. 

We need to adopt or introduce data format standards and API definitions.
The objective is to support modifiability, quality, and interoperability while adhering to open standards as closely as possible. At the same time, we should implement particular tools to build the toolset.

Inspired by the science field, the toolset should support the notation of *data entries*.
A *data entry* can be a local or remote file.
New *data entries* can be created using *data pipelines* from the existing ones.
The toolset must allow users to easily create, manage, and execute *data pipelines* and *data entries* on a local machine, a remote machine, or using a cluster.

From a certain perspective, the toolset is similar to ETL tools.
The difference is in primary use cases.
Unlike ETL, the new toolset should focus on rapid development and experimentation, reproducibility, adhering to open standards, and sharing not only *data pipelines* but also *data entries*.
 