---
title: "RDF viewer"
description: "Linked data is five start data format, with promises of semantics and interoperability.
  Yet viewing, the basic operation, is not living up to the promise.
  The objective is to improve this situation and try to address not only linked data but RDF in general."
published: "2023-04-05"
tags: ["bachelor-thesis"]
---
Linked data is five start data format, with promises of semantics and interoperability.
Yet viewing, the basic operation, is not living up to the promise.
The objective is to improve this situation and try to address not only linked data but RDF in general.

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

Plugins may support visualisation of vocabularies such as:
- [SKOS](https://www.w3.org/TR/2009/NOTE-skos-primer-20090818/)
- [OWL](https://www.w3.org/TR/owl2-overview/)
- [DCTERMS](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/)
- [DCAT](https://www.w3.org/TR/2023/WD-vocab-dcat-3-20230307/)
- [PROV](https://www.w3.org/TR/prov-o/)
Additional specification can be found using [w3 search](https://www.w3.org/TR/).

Each plugin may work separately or better collaborate with others to provide a unified view of the data at hand.

Related resources:
* We should be able to provide visualisation of an [invoice](https://wiki.vicepremier.gov.sk/pages/viewpage.action?pageId=101833175).
* [Sig.ma](https://www.semanticscholar.org/paper/Sig.ma%3A-live-views-on-the-web-of-data-Tummarello-Cyganiak/42a003b88c1e3333c54dc5d67ddbd8d637122824)

---

*Update*: 13.9.2025:

This idea is being implemented in the [rdf-viewer repository](https://github.com/adamrer/rdf-viewer).
