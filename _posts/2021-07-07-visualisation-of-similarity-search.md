---
layout: post
language: en
title: Visualisation of similarity search
tag: ["Bachelor thesis", "Diploma thesis"]
category: projects-ideas
---

Similarity search is a simple search method with a wide range of applications.
Yet the search results are often visualized just as isolated ordered lists.
While this is sufficient for users of the similarity methods, the authors of the methods can benefit from the additional insight.

<!-- more -->

For example, a similarity search for drug candidates is a core task in chemical informatics.
The task is simple; given a database of candidates and query molecules, sort the database based on similarity with query molecules.
A solution is to compute a score for each molecule in the database as an aggregation of similarities to all query molecules.
Maximum, minimum and average are some of the often employed methods. 

As a user of this method, we are interested in the final ordering. 
Yet, as the author of the similarity measure or aggregation method, we need additional insight.
For example, let us assume certain molecules should be rated higher. 
In other words, the similarity is not working as expected.
As authors of the method, we need to know why the molecules are rated as they are. 
Even better, it would be nice to have tools that allow for interactive exploration of the similarity.

The objective is to design and implement a web-based application that would help to tackle the above-mentioned issues.
