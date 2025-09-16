---
title: "User owned library"
description: "This project aims to reimagine how we work with libraries."
published: "2024-01-24"
tags: ["bachelor-thesis", "available"]
---
Libraries are a great way to boost developer productivity, as they provide ready-to-use functionality and components.
While particular library implementation is language-dependent, most libraries expose only their API.
This is an issue when a developer needs to modify inaccessible behavior or wants to express a higher level of control.
Despite that, we see little to no progress in the publication and use of libraries.

Nevertheless, there are promising projects exploring alternatives.
Project [Bit](https://bit.dev/) allows users to build composable software inside large development teams, by enabling the share of library-like artifacts.
[shadcn/ui](https://ui.shadcn.com/), a React component library, employs an alternative approach to publication.
Users can copy and paste the source, gaining complete control of the library in their projects.

This project aims to reimagine how we work with libraries.

The aim is to put library users in charge and thus lay the foundation of a user-centric library experience.

Notes:
- Develop should be able to mark and publish part of the project code (sources, documentation, tests) as a component.
- Other developers can use the component.
- Developers should have a way how to synchronize upstream changes.
- Developers should be able to locally change the code.
- The solution should stay as language-agnostic as possible.
- Focus on cross-projects usability.

---

*Update*: 13.9.2025:

[oul](https://github.com/basvas-jkj/oul) has been created in a bachelor thesis as an implementation of this idea.
The implementation focused on the client application and explore what a component may, what CLI API to use, and how to store information about components.

---

*Next iteration*:

- Re-implement CLI using Python for simplicity.
- Add support of language specific "initializers" to for example, rename packages or update paths.
- Implement server to enable component upload, download and search.

