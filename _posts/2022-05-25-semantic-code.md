---
layout: post
language: em
title: "Use-case : Documentation Reference"
tag: ["Bachelor thesis"]
category: projects-ideas
---

Use-case for [Semantic code]({% post_url 2022-03-06-semantic-code %}).

<!-- more -->

We may draw inspiration from PHP, where comments are extensively used to store annotations.
This is possible as the comments can be read at runtime.
For [example](https://phpstan.org/writing-php-code/phpdoc-types#global-type-aliases) type aliases.
The annotations are employed to do define types returned from functions.
In the example additional data are provided in an extra file.

In our case we are not interested in runtime.
Instead we aim to assist the developer when they write/read code.
As a result we also have access to comments.
We should not restrict ourself to PHP, instead we should be able to detect them and parse them for C-like languages.

A simple use-case is to include a link to a documentation.
The documentation may be stored in the same repository, or anywhere else.
The link would not be absolute, but rather relative with prefix defined in a configuration file.
For example:
```
// @sc sc:Link repo:documentation/concepts.md#Pipeline
```
May point to a file in current repository located at ```documentation/concepts.md``` section ```Pipeline```.


As a next step a plugin into IDE (Visual Studio Code) may be created.
The plugin would, on hover, show the link the metadata and the documentation.

Besides proof of concept this would allow us to separate comments and code.
The code may thus simply refer to a list of concepts, which is part of the documentation.
