---
title: "Hierarchical Data Transformation"
description: "Many formats represent hierarchical data.
  Yet there is no single tool for transformation between those formats, with strict output control."
published: "2022-03-16"
tags: ["bachelor-thesis", "available"]
---

RDF, XML, JSON and many other formats represent hierarchical data.
The hierarchical data are in a tree or forest-like structure.
However, conversation/transformation between those formats is not always straightforward.

To be precise, transformations, like CVS, XML, and JSON to RDF, are simple and well-supported.
The same is not true for the opposite direction.
A solution?
A language and processor designed for highly customizable and extensible transformation of hierarchical data.
The objective is to design and implement this tool or its part.

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

---

*Update*: 13.9.2025:

An attempt to solve this has been made in a bachelor thesis [Hierarchical data transformation](https://dspace.cuni.cz/handle/20.500.11956/193054).
The author propose an unified representation for hierarchical data called Ur.
For example JSON document:
```json
{
  "library": {
    "name": "Open Library",
    "books": [{
      "attributes": { "condition": "good" },
      "book-title": "Příliš hlučná samota",
      "page-count": 98
    }]
  }
}
```
Is represented as:
```json
{
  "@type": ["object"],
  "library": [{
    "@type": ["object"],
    "name": [{ "@type": ["string"], "@value": ["Open Library"] }],
    "books": [{
      "@type": ["array"],
      "0": [{
        "@type": ["object"],
        "attributes": [{
          "@type": ["object"],
          "condition": [{ "@type": ["string"], "@value": ["good"] }]
        }],
        "book-title": [{ "@type": ["string"], "@value": ["Příliš hlučná samota"] }],
        "page-count": [{ "@type": ["number"], "@value": ["98"] }]
      }]
    }]
  }]
}
```
We can see the representation is quite verbose.
For example every value is an array, which may not be necessary for build in types like prefixed with "@".
The author defined mapping for JSON, CSV, and XML to Ur.

Next the author defined UrPath a way do navigate Ur, e.g. `["library", "books", "[0]"]`.

The last step is definition of a transformation language for Ur.
Here author explores interesting idea where the query language is defined as a set of operations.
The operations include: shift, remove, default, filter, array-map, and replace.
Example of a shift operation:
```json
{
  "operation": "shift",
  "comment": "Posuň hodnotu name z objektu ’library’ do objektu ’org/lib’",
  "specs": [{
    "input-path": ["library", "name"],
    "output-path": ["org", "lib", "name"]
  }]
}
```

---

*Next iteration*:

- Simplify Ur and remove unnecessary arrays.
  We need to also include RDF conversion.
- Instead of transformation focus on navigation.
  Output can be produced as side-effect of navigation.
  For example, we can open an array on visiting an object and then emit value for each property.


[json-ld]: <https://json-ld.org/>
[csvw]: <https://www.w3.org/TR/tabular-data-primer/>
[hierarchical data transformation]: <https://github.com/skodapetr/hierarchical-data-transformations>
[xslt-equivalent-for-json]: <https://stackoverflow.com/questions/1618038/xslt-equivalent-for-json>
[jq]: <https://stedolan.github.io/jq/>
[alternative solutions]: <https://stackoverflow.com/questions/1618038/xslt-equivalent-for-json>
