---
title: "Data factory"
description: "Resource Description Framework (RDF) is a standard data model.
  As RDF becomes widespread, more and more data are available in one of the RDF data formats.
  Yet no Python library would allow for the processing of larger RDF data files."
published: "2021-07-28"
tags: ["bachelor-thesis", "available"]
---

Data processing is a common task in almost any computer-related activity.
For example, data scientists employ data pipelines, also called workflows, to prepare data from machine learning methods.
Scientists routinely process and analyze data with various levels of automation.
Data pipeline can be simple as running a bash script or as complex as running distributed streaming processing.

As science is an exploratory process, scientists often experiment with different data pipelines and datasets.
As a result, many different pipelines need to be designed, implemented and tested. Management and execution of those pipelines is a labour-intensive process.

Yet with proper toolset support, we should be able to make this process approachable and even increase the productivity of the researchers.

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

---

*Update*: 13.9.2025:

The first version was implemented as a bachelor thesis with [source code available](https://github.com/YArzumanyan/data-factory).
The solution demonstrated use of different vocabularies and the overall architecture design.

---

*Next iteration*:

What is missing is the integration with external resources, for example reading data from [National Open Data Catalog](https://data.gov.cz/).

