---
title: "Migration to Astro"
description: "From Jekyll to Astro."
published: "2024-09-06"
---
I have been using [Jekyll](https://jekyllrb.com/) for quite some time to host this website.

## Why Jekyll?
I have come across Jekyll thanks to [GitHub](https://github.com/), where Jekyll is utilized as the go-to-method for publishing GitHub pages.
This was way before most of the JavaScript solutions were developed and got popular.
Part of the appeal lies in the ability to utilize markdown.
Compare to HTML, markdown is much better to create simple content.
Also, when in need you can still mix HTML into markdown.
I have been also using the blog feature.
In a nutshell, you could just dump bunch of files into a directory and Jekyll would create a list you can easily render.
Add some html, css and you got all you need to run a simple blog.

## Running Jekyll
As a non-linux user I have decided to utilize [Docker image](https://hub.docker.com/r/jekyll/jekyll/) to run Jekyll locally.
In theory the setup was quite easy.

First start the Docker image:
```ps1
docker run -it --rm -p 4000:4000 -v "${PWD}:/srv/jekyll" -v "jekyll-gem:/usr/gem" jekyll/jekyll:4.2.2 sh
```

Now, in the Docker image just install the bundles and start Jekyll.
```bash
# Install using Gemfile.
# Using "bundle config set --local path '.vendor'" to create files in project directory.
# This would slow start of the jekyll command.
bundle install
# Start server.
jekyll serve --force_polling --drafts --config _config.yml,._config.yml
```

## Breaking point
Yet, as you may expect there were some issues.
- The first, issue was a time it took to execute the installation.
  It would take a minute or two.
  That is just the annoying amount of time.
  It is too short to do something else and too long to just state at the screen.
- The second problem was the necessity of using force pooling.
  Without it Jekyll would fail to detect changes and properly reload.
- The third issue was that sometimes I gor an error that I need to search how to solve.
  The lates error was related to privileges.

Could this issues be solved?
The answer is definite yes.
For example, I could run Jekyll under Linux distribution using WSL without Docker.
That would probably solved all the issues but, it would also mean that I would need to put the source into the WSL.
That is why, this was not acceptable.

## Welcome Astro
Long story short, I have decided to replace Jekyll with something else.
As of time of writing, there are plethora of tools to get the job done.
It just happen that I have recall Astro as the first one and decided to give it a go.
There is no need to write how to install it, create project, etc..
Like Jekyll, Astro has very good [documentation](https://docs.astro.build/en/getting-started/).
The only thing missing for me right now, is the ability to put HTML into the post description.

Let me explain.
When writing posts, you can specify post data, like title, date of publication, author, you name it.
You can then easily list all posts in a collection, basically a directory, and get those data.
So, if you want to render a list of posts, you just utilize this to create a list of post.
For each post you just take `data.title`, `data.description`, ... and render them in a list.
The problem is they are primitive values like strings.
In addition, Astro do sanitization, as it should, so any HTML in `data.description` is sanitized and thus not rendered as HTML.
A solution is to output the value without a sanitization.
```
<div class="mb-0" set:html={post.data.description}/>
```
