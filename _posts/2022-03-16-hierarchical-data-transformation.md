---
layout: post
language: en
title: Hierarchical Data Transformation
tag: ["Bachelor thesis", "Not available"]
category: projects-ideas
---

RDF, XML, JSON and many other formats represent hierarchical data.
The hierarchical data are in a tree or forest-like structure.
However, conversation/transformation between those formats is not always straightforward.

To be precise, transformations, like CVS, XML, and JSON to RDF, are simple and well-supported.
The same is not true for the opposite direction.
A solution? 
A language and processor designed for highly customizable and extensible transformation of hierarchical data.
The objective is to design and implement this tool or its part.

<!-- more -->

A transformation (lifting) from CSV, JSON to RDF is handled using [CSVW] or [JSON-LD].
When it comes to XML, there is XSLT.
[JQ], or [alternative solutions], can be employed to facilitate JSON to JSON transformation.
In general, the transformations between formats require specific knowledge of languages and libraries.

In addition, many transformation tools and languages provide functionality far beyond an ordinary use case, i.e. the tools are too powerful and complex.
This creates a space for a new tool focusing on a unified data model, simplicity and extensibility.
The main idea is that all the formats can be described as hierarchical.
With this abstraction, we can define unifying transformation language for a limited set of operations.
The differences between the formats may then be addressed by utilizing different data models.
For example, the difference between JSON and XML may be the existence of an artificial node *@attribute* that would provide access to attributes.

The project should build upon the existing implementation of [hierarchical data transformation].

[json-ld]: <https://json-ld.org/>
[csvw]: <https://www.w3.org/TR/tabular-data-primer/>
[hierarchical data transformation]: <https://github.com/skodapetr/hierarchical-data-transformations>
[xslt-equivalent-for-json]: <https://stackoverflow.com/questions/1618038/xslt-equivalent-for-json>
[jq]: <https://stedolan.github.io/jq/>
[alternative solutions]: <https://stackoverflow.com/questions/1618038/xslt-equivalent-for-json>
