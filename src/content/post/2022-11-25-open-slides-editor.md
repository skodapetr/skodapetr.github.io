---
title: "Open Slides Editor"
description: "We all may need to give a presentation at some point in time.
  Many presenters rely on slides as a cornerstone of their presentations.
  Those slides are created in software like PowerPoint and Google Slides, ...
  If you, like me, feel that there should be a better tool, you may consider reading the rest of this post."
published: "2022-11-25"
tags: ["bachelor-thesis", "available"]
---

We all may need to give a presentation at some point in time.
Many presenters rely on slides as a cornerstone of their presentations.
Those slides are created in software like PowerPoint and Google Slides, ...
If you, like me, feel that there should be a better tool, you may consider reading the rest of this post.

An alternative to established tools is web-based presentations.
Although implementing web-based presentations from scratch is possible, it is a labour-intensive task.
A solution is to utilize a framework like [reveal.js].
Yet even with a framework creating slides as code is much slower than using a visual editor.
There is an editor for reveal.js called [slides], but it is not free of charge.

A similar approach is a slides-as-code approach.
In this approach, a user writes code used to generate the slides.
Conceptually this is similar to web-based presentations, yet limiting users in available constructs.

A similar approach is a slides-as-code approach.
In this approach, a user writes code used to generate the slides.
Conceptually this is similar to web-based presentations with limited constructs
Yet providing a user with fewer options may be beneficial.
The fewer options user has, the less they need to worry about it and can focus on the important stuff.
For example, users can be given only several layouts they can employ.
With proper design, users can be forced into making better slides without even knowing.

In addition, modern slides should be connected and open.
Users should be able to:
- Share slides
- Manage multiple versions
- Re-use slides
- Compile new presentations from existing slides
- Connect slides to other data sources
- Query the slides to find or transform the content
- Save presentations online using a custom instance or [Solid] POD
- Save presentations offline

The list above is only a suggestion.
We should compile the final list after an extensive analysis.
The objective is clear, analyze, design and implement a tool to support the slides-as-code approach.

---

*Update*: 13.9.2025:

An implementation was created in bachelor thesis [Open Slides Editor]() available [online](https://olcorolcor.github.io/OpenPresentationsForEducation/).
The thesis contains very good analysis and related work section.
There the author identifies [Marp](https://marp.app/) as a solution with a similar approach.
The application allows user to utilize lanes, images, metadata tags and export to Reveal.js.

---

*Next iteration*:

- Explore [Slidev](https://github.com/slidevjs/slidev) as a new related work.
- Consider ability to use Markdown files as the source of truth.
  The motivation is to provide as open serialization format as possible.
- Enable conversion to and from RDF, to enable SPARQL based query and slides modification.
- Check PowerPoint presentation format.
- Provide better options for the export.
- Provide multi-screen editor to see slides content as well as a preview.

[reveal.js]: <https://revealjs.com/>
[slides]: <https://slides.com/>
[Solid]: <https://solidproject.org/>
