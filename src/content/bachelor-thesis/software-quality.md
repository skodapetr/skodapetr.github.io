---
title: "Software quality"
---

Warning: <span class="danger">This is work in progress.</span>

# Software quality

This is by not extend a complete list.
It is without saying that the software you design, and implement, should hold to certain quality standards.

## Deployment

When possible use [Docker](https://www.docker.com/) to distribute your application.
You can utilize [GitHub Packages](https://github.com/features/packages) to host your images.
I should be able to run your application just by:
<ul>
  <li>Clone the repository and navigate to it.</li>
  <li>Copy .evn.example and update it.</li>
  <li>Run docker compose.</li>
<ul>
