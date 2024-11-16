---
title: "Semantic code"
description: "Semantic web, semantic data - the common objective is to attach meaning to the data and increase interoperability.
Tools like vocabularies, ontologies, and query languages, are employed to support the above-mentioned goals.
Yet while all the tools aim to add meaning to data, none is the source of true meaning.
<br/><br/>
Source code is the source of truth.
We can leverage it to improve software interoperability and introduce semantics."
published: "2023-04-19"
tags: ["Project idea"]
---

Semantic web, semantic data - the common objective is to attach meaning to the data and increase interoperability.
Tools like vocabularies, ontologies, and query languages, are employed to support the above-mentioned goals.
Yet while all the tools aim to add meaning to data, none is the source of true meaning.

Source code is the source of truth.
We can leverage it to improve software interoperability and introduce semantics.

Many developer tools support semantic technologies, yet most focus on a top-down approach.
In this approach, the ontology at the top, designed by an ontology engineer, is the source of truth and defines the data model.
It is only from this model a source code or file schema can be generated.
Should the semantic change, the model must be updated before the code.

As a result, software developers must wait for overwhelmed engineers to analyze and implement any change to the model.
This leads to slowed development and often even to abandoning ontologies and semantics together.
At the same time, many developer teams do not have an ontology engineer at their team.
This holds, especially for small or medium developer teams or companies.
In addition, there may be time and money restrictions that made it impossible to create and maintain an ontology for a given domain.

As a result, the data model is captured only implicitly in the code.
An important benefit of this approach is the ability to easily change the model for a small codebase.
The drawback is the absence of connection from the code to any formal model or other parts of the code.

The objective of this work is to tackle this issue from the bottom up by providing developers with a toolbox that can be utilized to connect code to a model.
An example of such an approach may be a set of annotations that would allow developers to state the meaning of the objects and their properties in code.
From those annotations, a model can be automatically created.
This would allow revision of the model by domain experts.
Any change in the model can then be propagated back to the developer who may then adjust the code and thus change the model.

The toolset should build upon semantic technologies such as [Resource Description Framework] and open standards.
By using common terms to describe the object, software interoperability can be greatly enhanced.

None of the ideas here is new.
The main difference is a shift in ontology ownership and source of truth.
The ontology should be owned by the whole team not only ontology engineers.
We should recognize that the source of truth is the code, not the ontology.

This post does not represent a particular topic but rather a general project idea that should be implemented piece by piece from the bottom up.
Particular projects for this idea may be posted separately.

[Resource Description Framework]: <https://www.w3.org/RDF/>
