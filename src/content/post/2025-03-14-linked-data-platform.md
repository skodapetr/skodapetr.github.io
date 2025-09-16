---
title: "Linked Data Platform implementation"
description: "A Java-based implementation of W3C recommendation."
published: "2025-03-14"
tags: ["bachelor-thesis", "available"]
---

The main ideas is to implement Linked Data Platform (LDP) according to [W3C Linked Data Platform Recommendation](https://www.w3.org/TR/ldp/).
While there exists implementations, see [wiki](https://www.w3.org/wiki/LDP_Implementations), many of them are no longer actively developed.
At the same time LDP is being used as underlying specification of for [SOLID project](https://solidproject.org/) demonstrating the potential.
SOLID expand LDP with authentication and authorization.

I think, it would be interesting to focus on a personalized implementation.
Instead of using one server for multiple users, have one server per one user.

The implementation should:
- Implement LDP recommendation using Java.
- Provide token based access for easy sharing with other actors.
- Explore option of views, to share custom view of the data for a given actor.
  For example for resource A, I would be able to define derived resource B that I will share.
  Resource A can be RDF representation of my calendar, resource B can be created using SPARQL query that remove/hide some information.
- Provide simple client-side application to browse the resources.
