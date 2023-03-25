---
layout: post
language: en
title: Python RDF library
tag: ["Bachelor thesis", "Not available"]
category: projects-ideas
---

[Resource Description Framework] (RDF) is a standard data model.
As RDF becomes widespread, more and more data are available in one of the RDF data formats.
Yet no Python library would allow for the processing of larger RDF data files.
<!-- more -->

We can store RDF in formats like  [Turtle], [JSON-LD], [Trig] or [N-Quads].
While processing small RDF files is not an issue, processing a large amount of RDF is still a challenge.
For example, a [Wikidata entity dump] has over 80GB compressed. 
The issue is that many libraries, e.g. [rdflib], load all the data into the main memory.
As a result, processing large files is not possible.
A possible solution is to use non-Python tools with Python bindings like [Raptor] with [Redland].
Yet this is not developer friendly.

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
