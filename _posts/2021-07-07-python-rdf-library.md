---
layout: post
language: en
title: Python RDF Library
tag: Bachelor thesis
category: project-ideas
---

[Resource Description Framework] (RDF) is a standard data model.
As RDF becomes more widespread more and more data are available in one of the RDF data formats.
This makes it an interesting data source for developers and data scientists.
Yet there is no Python library that would allow for processing of larger RDF data files.

<!-- more -->

RDF model can be stored in number of formats including [Turtle], [JSON-LD], [Trig] or [N-Quads].
A common issue is a size, where a single RDF file can have up to several gigabytes without any problem.
For example, a [Wikidata entity dump] have over 80GB compressed. 
Another issue is that many libraries, e.g. [rdflib], try to load all the data into the main memory at once. 
A possible solution is to use non-Python tools with Python bindings like [Raptor] with [Redland].

The aim is to design and implement a library that would provide Python developers easy access to the RDF data. 
The library may provide event-based API (similar to [SAX] API) or some higher-level access after indexing the file.
The library must be able to handle large RDF files and should have no dependencies.

[Resource Description Framework]: <https://www.w3.org/RDF/>
[Turtle]: <https://www.w3.org/TR/turtle/>
[JSON-LD]: <https://json-ld.org/spec/latest/json-ld-rdf/>
[Trig]: <https://www.w3.org/TR/trig/>
[N-Quads]: <https://www.w3.org/TR/n-quads/>
[Wikidata entity dump]: <https://dumps.wikimedia.org/wikidatawiki/entities/>
[rdflib]: <https://github.com/RDFLib/rdflib>
[Raptor]: <http://librdf.org/raptor/>
[Redland]: <http://librdf.org/bindings/>
[SAX]: <https://docs.oracle.com/javase/tutorial/jaxp/sax/parsing.html>
