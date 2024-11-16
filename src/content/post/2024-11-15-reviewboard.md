---
title: "Review Board"
description: "First impression on Review Board."
published: "2024-11-15"
---
I decided to try out [Review Board](https://www.reviewboard.org/).
I was happy to find a deployment using Docker.
Even better, the [docker compose file](https://github.com/reviewboard/reviewboard/blob/release-7.0.2/contrib/docker/examples/docker-compose.postgres.yaml) lists instructions for starting the whole thing.
As a result, it just took a couple of minutes and I got my instance running.
Sweet!

With the instance to log in, there was a last step, log in.
It seems there is an "admin" user, but what is the password?
I searched the Docker compose logs and found this:

```rb-site install --noinput --copy-media --admin-email=admin@example.com --admin-password=admin --admin-user=admin --allowed-host=127.0.0.1 --cache-info=memcached:11211 --cache-type=memcached '--company=My Reviewboard' --db-host=db --db-name=reviewboard --db-user=reviewboard --db-pass=reviewboard123 --db-type=postgresql --domain-name=localhost --web-server-port=80 --web-server-type=apache /site```

So, the password for "admin" should be "admin".

Unfortunately, when I try to log in, I get Forbidden 403.
Looking again at the logs:

```reviewboard-1  | 2024-11-15 20:31:56,233 - WARNING - None - AnonymousUser - /account/login/ - django.security.csrf - Forbidden (Origin checking failed - http://localhost:9010 does not match any trusted origins.): /account/login/```

There is a domain option in the configuration.
Maybe I need to include the port as well.

Time to stop the container, update configuration, and re-run.
The `docker compose down -v` should take care of this.
Nope, setting `domain` to `localhost:9010` does not work at all.

Last chance, use port 80, and .. it works.
It is not what I would like it to be, but should be good enough for initial testing.
I may need to look more into `django.security.csrf` to support running with a non-default port.

It seems that I can create a review.
Add files to the review, add reviewer.
I can add comments on the lines of the uploaded files.
Once published, I can see the review even without being logged in.

There is another part of the Review Board tool called RBTools.
It is a command line tool to allow for easy of of Review Board.
There is even [best-practice guideline for use with Git](https://blog.beanbaginc.com/2015/01/26/an-effective-rbtools-workflow-for-git/).

After about 10 minutes of using the Review Board, I got my first impression.

What I liked:
- Easy deployment using Docker compose.
- Ability to add comments to source code.
- Ability to create multiple reviews and assign reviewers.
- Integration with the RBTools seems interesting.
- Ability to add comments to comments in source code or to review.

Where I see misalignment with my expectations:
- Reviews are published to be visible to all users.
- Lack of IDE-like experience in file navigation.
- A need to hover over a comment in the source code to view it.
- Once published, review content can not be modified. For example, it is not possible to edit past comments.

Overall, the project is interesting, and I can see the benefits of using it.
On the other hand, there is a learning curve and best practices to follow.
The main issues are access control and the lack of an IDE-like environment.
While the first may be fixed by reading documentation, the second one may be a design choice.
The thing is that the Review board is designed to be able to review almost anything.
As a result, it is not a perfect fit for my use-case of reviewing software artifacts.
With that said, I would not hesitate to revisit Review Boards in the future should I need a review tool.
