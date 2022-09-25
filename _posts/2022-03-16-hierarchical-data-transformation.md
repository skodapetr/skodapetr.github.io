---
layout: post
language: en
title: Hierarchical Data Transformation
tag: ["Bachelor thesis"]
category: projects-ideas
---

RDF, XML, JSON and many other formats represent hierarchical data; data in a tree/forest like structure.
However, conversation/transformation between those formats is not always straightforward.
While it is easy to convert data from CSV, XML, and JSON to RDF, the opposite way can be improved.
The objective is to design and implement a language and processor that would allow for the extensible transformation of hierarchical data.

<!-- more -->

A transformation (lifting) from CSV, JSON to RDF can be handled using [CSVW][csvw] or [JSON-LD][json-ld].
When it comes to XML, there is XSLT.
For JSON user can employ XSLT as well or one of the many [alternative solutions][xslt-equivalent-for-json].
The transformation between several formats thus may require knowledge of languages and specifications.

In addition, many of the transformations provide functionality far beyond an ordinary use case, i.e. the tools are too powerful and complex.
This creates a space for a new tool, that would focus on a unified data model, simplicity and extensibility.
The main idea is that all the formats can be described as hierarchical.
This abstraction would allow to defined unifying transformation language for a limited set of operations.
The differences between the formats may then be addressed by utilizing different data models.
For example, the difference between JSON and XML may be the existence of an artificial node *@attr* that would provide access to attributes.

The project should build upon / extend the already existing implementation of [hierarchical data transformation][[hdt]];

[json-ld]: <https://json-ld.org/>
[csvw]: <https://www.w3.org/TR/tabular-data-primer/>
[hdt]: <https://github.com/skodapetr/hierarchical-data-transformationsl>
[xslt-equivalent-for-json]: <https://stackoverflow.com/questions/1618038/xslt-equivalent-for-json>
