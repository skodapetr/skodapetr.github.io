---
title: "Vocabulary hub"
description: "One of the core principles of linked data is to employ vocabularies to describe data in a machine-readable way.
  By doing so, data producers can significantly enhance data usability and interoperability.
  Findable, Interoperable, Accessible, and Reusable, or FAIR in short, vocabularies are enablers of the aforementioned.
  However, many vocabularies are not published in an easy-to-consume way.
  As a result, data publishers often resort to the design of their new proprietary vocabulary.
  While feasible, this approach decreases the value we would get from reuse and hinders data interoperability.
  The objective of this project is to tackle those issues."
published: "2023-02-01"
tags: ["project-idea"]
---

One of the core principles of linked data is to employ vocabularies to describe data in a machine-readable way.
By doing so, data producers can significantly enhance data usability and interoperability.
Findable, Interoperable, Accessible, and Reusable, or FAIR in short, vocabularies are enablers of the aforementioned.
However, many vocabularies are not published in an easy-to-consume way.
As a result, data publishers often resort to the design of their new proprietary vocabulary.
While feasible, this approach decreases the value we would get from reuse and hinders data interoperability.
The objective of this project is to tackle those issues.

As the problem is quite complex, I do not expect a single person could fully resolve it with a top-down approach.
Instead, we should focus on a bottom-up approach by proposing and implementing partial solutions in separate projects.

In this project, we focus on sharing the vocabulary using a shared repository called vocabulary hub.
What vocabulary hub exactly is and how it could be used should be specified as a part of the project.
Anyway, I would like to hint at a few ideas:
- Users can store references to their vocabulary in the vocabulary hub.
- Users can store their vocabulary in the vocabulary hub.
- Users can utilize the vocabulary hub as a "proxy" for dereferencing vocabularies.
- Users can search in stored vocabularies.

This idea is not new, and there are existing solutions like:
- [Linked Open Vocabularies (LOV)](https://lov.linkeddata.es/dataset/lov/)
- [FAIRsharing](https://fairsharing.org/search?fairsharingRegistry=Standard)

The list below contains some additional ideas to consider when tackling this project:
- The vocabulary hub should allow for search using example data or example vocabulary, similar to the query by example.
  Overall the idea is to make it easy for users to find a vocabulary to employ.
- The vocabulary hub should not be limited only to linked data vocabularies.
  It should support conceptual/logical models of any schema.
- Given source schema/vocabulary we should be able to align it to registered vocabularies.
- Given source and target ontology we should be able to find mapping.
- We can help user to find and create a new vocabulary from existing terms.
  By doing so we can lower the entry barrier for adopting existing vocabularies in existing projects.
  This example was motivated by [SSP pull request](https://github.com/datagov-cz/ssp/pull/628/files).

Related:
- [Let’s talk about pods](https://ruben.verborgh.org/blog/2022/12/30/lets-talk-about-pods/)
