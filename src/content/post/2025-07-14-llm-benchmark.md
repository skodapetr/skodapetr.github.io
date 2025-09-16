---
title: "LLM benchmark"
description: "The objective is to test what data representation is best for given task and LLM."
published: "2025-07-14"
tags: ["master-thesis", "available"]
---

With the advent of [MCP](https://modelcontextprotocol.io/) and argentic workflows, LLMs need to be able to process and produce data.
For example, an LLM can be provided with a restaurant menu and a task to select the best dishes with respect to given user preferences.

We can also utilize a more abstract example.
We can have a data schema and a set of questions about the schema, like find a class or list all properties.
This can be great for schema alignment tasks.

The general idea is simple: LLM is given a question and data.
LLM needs to utilize the data to answer the question and produce an output.

The research question is: What is the best data representation and for what tasks?

The objective is to design data-related queries with sample data, creating a benchmark.
The next step is to employ different LLMs and evaluate their performance.
The final step is to produce recommendations based on the results.

We can also view the idea from a different angle.
We define date-related use cases with relevant data to carry out the task.
What is the best way to provide the LLM with access to the data?
For example, should we also include schema information in the prompt?

Part of the experiment can also deal with the sentiment and relationship with the LLM.
Based on the closing paragraph of [Vibe Coding as a Coding Veteran](https://levelup.gitconnected.com/vibe-coding-as-a-coding-veteran-cd370fe2be50) where AI reflects on the vibe-coding experience.
Would the performance of the LLM change when it feels respected?
