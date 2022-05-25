---
layout: post
language: em
title: Semantic code
tag: ["Bachelor thesis", "Master thesis"]
category: project-ideas
---

Semantic web, semantic data - the common objective is to attach meaning to the data and increase the interoperability.
While we have vocabularies, ontologies and query languages the key step in the world of software is often overlooked, source code.

<!-- more -->

Source code is the source of truth and as such can be leveraged to improve software interoperability and introduce semantics.
May attempts have already been undertaken to build systems that utilize semantic technologies.
However, most of them use a top-down approach, where the designer must design a data model.
It is only from this model a source code, or file schema can be generated.
Should the semantic change, the model must be updated before the code.

In reality, small to medium projects are often created by developers who have little to no experience with modelling.
In addition, there may be time and money restrictions that made it impossible to create a conceptual model before the software is created.
As a result, the data model is captured only implicitly in the code.
An important benefit of this approach is the ability to change the model with ease.
The drawback is the absence of any connection from the code to any formal model.

The objective of this work is to tackle this issue from the bottom up by providing developers with a toolbox that can be utilized to connect code to a model.
An example of such an approach may be a set of annotations that would allow developers to state the meaning of the objects and their properties in code.
From those annotations, a model can be automatically created.
This would allow revision of the model by domain experts.
Any change in the model can then be propagated back to the developer who may then adjust the code and thus change the model.

This approach may also benefit from semantic technologies such as [Resource Description Framework].
By using common terms to describe the object, software interoperability can be greatly enhanced.

While none of the ideas here is new, the main addition is the shift from the domain expert who is responsible for the model design to a developer who should now stand in the centre.

[Resource Description Framework]: <https://www.w3.org/RDF/>
