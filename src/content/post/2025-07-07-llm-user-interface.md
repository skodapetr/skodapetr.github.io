---
title: "LLM user interface"
description: "The objective is to explore how to pair LLM-chat interface with traditional graphical user interface."
published: "2025-07-07"
tags: ["bachelor-thesis", "master-thesis", "available"]
---

LLMs and AI agents can utilize a chat-like interface to export a wide range of functionality.
For example, an AI agent can utilize the [MCP](https://modelcontextprotocol.io/) server and execute actions on the user's behalf.
This is great if the action is part of the conversion, like placing an order.
The agent can ask the user for all the details and then invoke MCP action to execute the business logic.
But what if the action is part of some non-linear user workflow, like creating a data schema diagram?

We get a hint of possible interaction thanks to IDE and coding assistants.
They provide two main forms of interaction: autocomplete and agent-mode.
In the first mode, the objective is to predict and carry out future users' actions to improve user effectiveness.
In the second mode, the AI agent executes commands given by the user via a chat-like interface.

While this may work great for writing a text, is this the best approach for other types of interaction?
Is it better to provide chat chat-like interface instead of a well-designed input form?

For the bachelor's thesis, the objective is to pick representative workflows.
For each workflow, design and implement a classic and LLM-based interface
Evaluate the interfaces using a user study.

For the master's thesis, the objective is to explore possibilities of LLM and non-LLM-based user interfaces.
The thesis should pick one or more complex workflows and explore different levels of LLM involvement.
For example, we can explore if it is easier for the user to fill in the workflow step by step or have it prefill based on a previous conversation with an AI agent.
