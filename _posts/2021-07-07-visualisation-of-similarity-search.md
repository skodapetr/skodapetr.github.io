---
layout: post
language: en
title: Visualisation of similarity search
tag: ["Bachelor thesis"]
category: projects-ideas
---

Similarity search is a simple search method with a wide range of applications in many domains.
Yet the search results are often visualised just as an isolated ordered lists.
While this is sufficient for users of the similarity methods, the authors of such method can benefit for additional insight.

<!-- more -->

For example, in chemical-informatics drug candidates may be found using so-called molecular fingerprints and similarity search.
The whole process can be seen as a similarity query into a molecular database. 
For each molecule in the database, we compute a score as an aggregation of similarities to all query molecules.
Some of the most commonly used aggregation methods are maximum, minimum and average.
The ordered list of molecules by score is the response to the similarity query.

This approach allows us to easily answer a question, why a given molecule is in a certain position. 
However, we as authors of the similarity function we may be interested in another question: what needs to change in order to change the position of the molecule. 
The changes may include a change in the query, molecule database or a similarity method.

The aim is to design and implement a web-based application.
The application would allow a user to visualise results of similarity search and get answers to above-mentioned questions.
