---
layout: post
language: en
title: "Open Slides Editor"
tag: ["Bachelor thesis"]
category: projects-ideas
---

We all may need to give a presentation at some point in time.
Many presenters rely on slides as a cornerstone of their presentations.
Those slides are created in software like PowerPoint and Google Slides, ...
If you, like me, feel that there should be a better tool, you may consider reading the rest of this post.

<!-- more -->

An alternative to established tools is web-based presentations.
Although implementing such a presentation from scratch is possible, it is a labour-intensive task.
A solution is to utilize a framework like [reveal.js][revealjs].
Yet even with a framework creating slides as code is much slower than using a visual editor.
There is an editor for reveal.js called [slides][slides], but it starts at a $5 monthly subscription. 

Another issue is the slides as code (HTML) approach. 
It may provide more power than necessary.
For example, a user may need to use only a few basic operations:
* Add heading
* Add text 
* Format text using color, size, ...
* Load external graphics 
* Add a shape
* Position the content
The list is by no means complete; a proper analysis and related work research should be carried out to create the list.

It may be even more productive to strip a user of some power.
Instead, the user may be presented with a set of customizable layouts that may render it faster to create slides.

In addition, modern slides should be connected and open.
It should be possible to share slides, manage multiple versions, and easily compile new presentations from existing slides.
There should also be an option to query the slides, to find certain topics/slides.
As of the "open", that should be machine-readable and under the user's control.
The user should decide whether to save data on a local machine or a [Solid][Solid] POD.

The objective of the text above is to highlight a few possibilities of what a next slide solution may be.
Those ideas are far from implementation, yet they may contribute to better solutions than we have today.

[revealjs]: <https://revealjs.com/>
[slides]: <https://slides.com/>
[Solid]: <https://solidproject.org/>
