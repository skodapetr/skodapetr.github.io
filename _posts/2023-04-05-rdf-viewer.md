---
layout: post
language: en
title: "RDF viewer"
tag: ["Bachelor thesis"]
category: projects-ideas
---

Linked data is five start data format, with promises of semantics and interoperability.
Yet viewing, the basic operation, is not living up to the promise. 
The objective is to improve this situation and try to address not only linked data but RDF in general.

<!-- more -->

Linked data is built using URLs, some as subjects, predicates or objects.
We can view subjects as entities, predicates as properties, and objects as values for a given property.
Values can be URLs or literals, i.e. typed strings.
The URLs can be accessed using dereference, as a part of a file, or using a SPARQL endpoint.
In addition to a variety of data sources, and their size, data about a single subject can be scattered among multiple data sources.

For a better user experience label of each predicate, subject, and value should be fetched.
In addition, some subjects can be typed.
Typed subjects may represent a point on a map, a person, a collection of items, etc..
There should be a way how to provide specialized visualisation based on the subject type.

The RDF viewer should be implemented as a web-based application extensible with plugins.
Optionally, the application may feature a backend to allow the processing of larger data.
