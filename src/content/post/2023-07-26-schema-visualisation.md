---
title: "Schema visualisation / editor"
description: "There are many ways how to define a data schema: JSON Schema, RDFS, or code.
  We also have plenty of visualisation techniques like UML or ER-Model.
  So it should be simple to take your schema and visualise it right?
  Well, I've tried and I was unable to find, as of 2023, any suitable online tool to get the job done.
  We can try to change this together."
published: "2023-07-26"
tags: ["master-thesis"]
---

There are many ways how to define a data schema: JSON Schema, RDFS, or code.
We also have plenty of visualisation techniques like UML or ER-Model.
So it should be simple to take your schema and visualise it right?
Well, I've tried and I was unable to find, as of 2023, any suitable online tool to get the job done.
We can try to change this together.

Notes:
- In addition to visualisation, the user should be able to edit the schema. <br/>
- Export options to different schemas (JSON Schema, RDFS, ...) can be limited.

---

*Update*: 13.9.2025:

An attempt to implement a schema editor was made in bachelor thesis.
The result is available online as [code-data-wiz](xmon3r.github.io/code-data-wiz/), [source code](https://github.com/XMON3R/code-data-wiz).
The number of implemented input formats is quite limited.
Different input languages are converted to domain specific models (DSM).
DSM can be converted to, and from, so called universal model.

It turns out that parsing different languages is a complicated task that consumed significant amount of time.
As a result the implementation and size of the universal model is not where they can be.
The architecture and experience can be used as a foundation for next iteration.

---

*Next iteration*:

- Provide initial example values.
- Improve error handling.
- Expand support of languages.
- Focus more on definition and work with the universal model.

---

This post is a [stub](https://simple.wikipedia.org/wiki/Wikipedia:Stub).
I may add more information later.
Please feel free to reach out to me to discuss this topic further.


