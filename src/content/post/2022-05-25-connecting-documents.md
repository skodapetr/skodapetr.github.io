---
title: "Connecting documents"
description: "Honestly, I do not enjoy writing documentation.
  By documentation, I do not mean comments in source code.
  I am talking about external documentation, API specification, data model, user documentation, database schema documentation, etc...
  <br/><br/>
  Yet frankly, even more, tedious and labour-intensive than writing the documentation is keeping it up to date.
  The reason is there is no connection between to code to the documentation.
  As a result, we manually synchronize multiple documents. "
published: "2022-05-25"
tags: ["bachelor-thesis", "active"]
---

Honestly, I do not enjoy writing documentation.
By documentation, I do not mean comments in source code.
I am talking about external documentation, API specification, data model, user documentation, database schema documentation, etc...

Yet frankly, even more, tedious and labour-intensive than writing the documentation is keeping it up to date.
The reason is there is no connection between to code to the documentation.
As a result, we manually synchronize multiple documents.

There must be a better way, and you can contribute to it.

There are multiple document types in software solution documentation.
Each document focuses on a particular audience and addresses certain needs.
For example, administration documentation explains to the administrator how to install and administer the running instance.
Analysis and architects can employ data models and API design documents to get the big picture of architecture and data.
What about the developers?
As a developer, I would love to be able to jump from code to relevant documentation.

As a developer or software engineer, I may be tasked with adding a new property to a domain object.
It would be great if I can easily list relevant code and documentation where a given domain object is used.
This would not only help me to carry out impact analysis; but also make it easier to change all the relevant documentation.

The main idea here is to connect the code with other documents like documentation, HTML forms, design documents, database schema definitions, etc...

We may draw inspiration from PHP before version 8.
While other languages provide a way to annotate code, this was not the case with PHP.
Instead, PHP developers employ comments to store annotations.
The main advantage is that this does not introduce any new must-have dependency.
As a result, any language with comments can host annotations.

We can design annotations that allow a developer to connect from code to other documents.
On this connection, we can build additional logic with a considerable impact on software development.
For example, let us consider ontology engineering.
Ontology engineers often design ontologies and draw specifications that a developer must implement or adhere to.
Even if a developer can change the specification, they may have ot employ a specialized tool.
What if we can propose changes just by writing code and using annotations?

To give a tangible example, let us consider a simple use case.
A developer can write an annotation, like this:
```PHP
// @sc sc:seeAlso repo:documentation/concepts.md#Pipeline
class Pipeline { ...
```
This annotation connects the class with the given documentation document.
Using an IDE a developer can navigate to the document.
In addition, should the class or the document change, the developer is informed that connected documents should change as well.
By doing so it should be easier to maintain the documentation.

---

*Update*: 13.9.2025:

PoC implementation was undertaken in bachelor thesis [Linking software artifacts](https://dspace.cuni.cz/handle/20.500.11956/200560).
What is missing is better architecture and support for annotation consumption.

---

*Next iteration*:

- Focus more on software visualisation and search of annotations, it is an orthogonal information we add to the software.
- Provide a way, VSCode plugin, to provide and visualize additional information for the annotations.
  This information may be stored in a project knowledge file.
- Implement GH actions to extract annotations and build an index.
- Explore VSCode build-in support for custom shortcuts and [Contextive VSCode extension](https://github.com/dev-cycles/contextive) instead of lsa-helper plugin
