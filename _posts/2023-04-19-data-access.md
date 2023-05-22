---
layout: post
language: en
title: "Request driven data access"
tag: ["Bachelor thesis"]
category: projects-ideas
---
The aim is to make data available in multiple representations as requested by the user.

<!-- more -->
Imagine a simple use-case.
A developer, or data engineer, has data in CSV format.
Yet, for additional processing, they need data to be in RDF format.
Nowadays, they may convert data manually or look for automated transformation from CSV to RDF. 
Such transformation may employ [CSV on the Web specification](https://www.w3.org/TR/tabular-data-primer/).

In a nutshell, the idea is to convert data in one format and representation to another format or representation.
Another use-case can be to map data from one vocabulary to another using a known mapping method.
If you are interested in finding the mapping you may consider the [Vocabulary hub project]({% post_url 2023-02-01-vocabulary-hub %}).

Anyway, in this project the objective is to focus on a seamless transformation.
A user would upload the data file, or point to an online source.
In addition, they may specify a schema or vocabulary of input data.
As a next step, users can request data in different profiles.
A profile defines data format and schema.

The application should implement HTTP API compatible with [LDP specification](https://www.w3.org/TR/ldp/) to enhance interoperability.

Related work:
* [grlc](https://github.com/CLARIAH/grlc)
  Provide REST API for SPARQL endpoint based on predefined SPARQL queries.
* [Ontology Access Toolkit (OAK) is a Python](https://incatools.github.io/ontology-access-kit/introduction.html)
