---
title: "Text structure"
---

Warning: <span class="danger">This is work in progress.</span>

# Text structure

This page provides an overview of a possible implementation focused thesis.
The thesis should consists of:
- [Introduction](#introduction)
- [Related work](#related-work)
- [Analysis](#analysis)
- [Design](#design)
- [Developer documentation](#developer-documentation)
- [User documentation](#user-documentation)
- [Administrator documentation](#administrator-documentation)
- [Testing](#testing)
- [User testing](#user-testing)
- [Conclusion](#conclusion)

## Introduction

The initial chapter should introduce a reader to the domain and the problem you address.
You must not expect the reader to have any domain-specific knowledge.
Use this chapter to define the vocabulary and issues and reference relevant literature.

Once the domain is defined, introduce the setup and the problem and hint at a possible solution.
Clearly state what are the objective of the thesis.

Once objectives are defined explain the structure of the rest of the text.
In the ideal case, you should forward the reference following chapter to also introduce the text outline.

## Domain introduction

This chapter is optional.
You can employ it, or similar, if you need to introduce a reader to a certain domain.

## Related work

This is an important, yet often overlooked part of the thesis.
In the previous chapter, you briefly described the problem you aim to solve.

In this chapter, you should identify and describe existing solutions to the problem.
You can also include partial solutions, solutions of sub-problems, or any other related solutions.
In other words, the objective is to explore related work, as the name of the chapter suggests.

You should start this chapter by presenting what a related work for your work is.
Next, you should define how you search for it.
For example, you may list queries you utilized for your favorite search engine and how many search results you explored.
It is also a good idea to state when you performed the search.

Once the related work is identified, you need to briefly introduce and comment on each solution.
This does not mean you will copy an introduction text from the solution's website!
It may also harm readability to repeat the same information over and over again for different solutions.
Instead, provide a short introduction and then focus on specifics, advantages, and disadvantages.
It is also a good idea to include a screenshot of the solution.

The issue with the above-described approach is that it may be hard to compare the solutions based on such text.
To tackle the issue, I recommend introducing metrics and well-defined criteria.
For example, you can have criteria for whether a solution is open-source or not.
Try to be exact with the definition and evaluation of the criteria; the evaluation should be reproducible.
Thus, another student, given the same solutions and your criteria, should get similar evaluation results.
You may present an evaluation using a table.

Yet, even with the criteria, this chapter is not complete.
At this point, you laid down the evidence; now you need to make conclusions/summary.
You should describe what the evaluation means for your work.

Try to provide answers to following questions:
- Are there any issues that have not been addressed by existing solutions?
- Are you producing an N+1 version of an already existing tool?
- Is there a need for your solution, if so why?
- What inspiration can you draw from the existing solution?

## Analysis
In this part, you should analyze the issue/opportunity you are about to address.
You need to think about users, stakeholders, functionality, and other systems.
The objective is to figure out "WHAT" should be implemented.

The high level flow is simple and reflects how would you design a software.
- Identify your users.
- Collect user requirements from the users.
- Group user-requirements to use-cases and detail them with user scenarios.
- Extract functional and quality requirements.

### Users

In this section you should identify stakeholders and users of your software.
You may skip stakeholders if you want.
In short, a stakeholder is someone with a relation to the software.
For example developers may be stakeholders.
I hope there is no need to comment on who the users are.

### User requirements

Once you have identified the users it is time to find out what they need from your software.
These are called user requirements and you would get them from your users.
Imagine yourself as software analysis.
You sit down with users and stakeholders, ask questions, and records answers.

There is no strcit structure or level of detail user requirements must follow.
Yet, I would recommend try to keep them in a simple format:
```
As {USER-ROLE}, I need to {REQUIREMENT} to {REASON}.
```
The last part is optional, but beneficial to have as it allows you to prioritize the requirements.
This is useful as you may decide not to implement all of them at the end.

Each user requirement should have an identifier, like U1, U2, etc..

### Use-cases

One problem with user requirements is missing big picture.
We would like to group them together.
There are two reasons for this:
- We need to know who needs the functionality.
- We need to know whether there is shared functionality.

A use-case is about a user and the added value of the software for the user.
As a result, "user can log in to the system" is not a good use-case as there is no value to the user.
Keep in mind that from this perspective user may always be a human but also another system.

If you have a higher number of use-cases you should utilize a use-case diagram.
Each diagram should communicate certain information to a particular audience.
As a result, it may be better to have multiple smaller use-case diagrams rather than one big one.
Optionally, you can elaborate on selected use-cases by providing user-scenarios.

### User scenarios

This section is optional.
The problem with use-cases is that they are often quite high level.
It may not be clear how exactly will user interact with your software to archive their objectives.
A solution is to write user scenarios for the use-cases.

A user scenario consists of:
- Initial state
- Steps
- Final state

The steps are quite low level.
A step may be to click a button of fill in a form.
That is why, it makes sense to accompany them mock-ups or wireframe.

### Functional and quality requirements

At this point you should have a good idea who and what functionality expects from your software.
The next step is to express this knowledge in form a functional and quality requirements.
Unlike user requirements the requirements in this section should be precise.
This is what ultimately form the contract, this is what define what functionality you need to deliver.

All requirements in this section must be identified by an uniq identifier.
Use F prefix for functional and Q prefix for quality requirements.
All requirements must be clearly stated.

The functional requirements must focus on the user-system interaction.
You can stick to similar format as before.
So where is the difference you may ask?
Well mostly in quality, while user requirements can be high or low level, the functional are on the same level and are exact.
In fact, if you take your functional requirements and task two developers to design and implement a solution, you should get functionally similar results.
You can view functional requirements as a contract, or API, between users and your system.

While the functional requirements are about functionality they do not speak about quality.
In other word, you can provide all required functionality and your software can still be bad.
How bad?
Well, for example, you can have a web application, which can serve only one request at a time.
This is a scaling issues.

Quality requirements are there to address quality of the design and implementation.
Expanding on the example, you may have a quality requirement that the application should be able to handle certain number of users.
Unfortunately that is not a good requirement.
Each requirement, functional or quality, must be testable.
For functional it is easy, you just check the functionality.

The quality requirement must be stated in a way that you can verify the implementation.
You can do this by including some measurable metrics and numbers.

An alternative is reference to material or standards.
The requirement "system should be secured" is hard to measure and evaluate.
Instead refer to a security standard.

### Summary

Keep in mind that in this chapter, you are analyzing the required functionality.
In other words, you are establishing the contract between the software and the user.
You do NOT design the software or the solution.
In other words, you do NOT say HOW the system works.

If you provide two developers with the same analysis, they should produce application that allows to do the same stuff -- both application provide the same functionality.

## Design

In the previous chapter, you established the contract between the user and your software - the WHAT.
The aim of this chapter is to design software that would be able to fulfill that contract - the HOW.

### Architecture

You should start with a description of the context your application exists in.
In other words, you system in the context of other systems and users.
You can employ [C4 model, system context diagram](https://c4model.com/diagrams/system-context#system-context-diagram) for visualisation.

Once you have established your system, the context, you can work on the internals.
A good idea is to utilize L2 and L3 levels of the C4 model.
This will guide you through design of containers and components, adding more and more detail into your software.

Let us pause here for a second.
What does it mean to "add a detail"?
Well imagine you have an application and the application needs to persist data.
I hear you, "easy, just use PostgreSQL" -- here you made a decision.
But why?

When you design your application it is not only about the outcome, the design, but also the process.
For each "decision", you should introduce the problem, list solutions, discuss advantages and disadvantages, and explain your decision.
The "decision" is in quotes because it is not every decision, only the important ones.
You do not need to discuss name of each component, but you should discuss what approach you utilized to select which components are in your solution.

### Libraries and technologies

An alternative name for this section is "tech stack", the technologies you utilize.
You may have made some decision about it in the architecture section, that is fine.

Still here you should made your decision, if you not have done so before, on language, libraries, tools, etc..

Let me give you an example with a need for a library.
First, you need to specify expectations from the library.
What functionality do you need?
What language are you using?
Next, you list libraries that match your expectations.
For each library, you may provide examples of how to use the library.
You also list the advantages and disadvantages of using the library.
You can comment on the quality of documentation, community support, API, etc..
At this point, it should be clear which library is the best.
If there is no clear winner, you may pick one based on your preference.
In either case, you explain your decision.

### Summary

From a certain perspective the design is the most important part of the text.
It explain how you decide to tackle the problem of implementing the software.
Some would even say, that the rest is just the implementation detail.

If you provide two developers with the same design, they should produce an application of the same functionality and design.
Meaning you should recognize the structure of the application and be able to make decisions about changes.
Yet, you may not be able to effectively implement them, because you do now know the details.
This is why we need developer documentation.

## Developer documentation

It is not easy to draw a line between design and developer documentation.
You can assume that a software architect would read only the design.
In contracts, the software developer would read both chapters.

The developer documentation should be the entry point for a developer interested in contributing to the project or maintaining the software.

This chapter should not contain an extensive list of classes or generated documentation.
All this information is available in the source code, thus it makes no sense to copy it here.
Instead, this chapter should connect the high-level decisions from the Design chapter with the code.

In addition, you can comment on anything unusual.
For example, you have used a hack to deal with a bug in a library.
Explain the hack and the bug so another developer does not lose time trying to remove the hack.

## User documentation

This is the manual for a user of your application.
Should you have different users, you should have more than one user documentation.

There are two ways how to approach the documentation.
The first is to extensively list all screens and describe the functionality of every button.
By doing so, you basically create a reference manual.

A better alternative is to introduce your software using one or more tutorials.
A tutorial should be accompanied by images and capture the main functionality of your solution.
You may also link a video version of the tutorial.

## Administrator documentation

This documentation focuses on the installation and maintenance of the software.
You should provide a detailed list of requirements.
Keep in mind that your software may have compile-time as well as runtime requirements.

You should also provide a step-by-step guide to installation.
As an administrator, I should be able to copy and paste the command into the command line and, by doing so, install and start the software.

For web applications, you should aim at nearly one-line deployment using [Docker](https://www.docker.com/).

If you assume the presence of any data in the software, for example, in the user documentation, you must provide steps to load the data into your software.

## Testing

It probably comes as no surprise that your software should be tested.
Without tests, how can you be sure that your application is working properly?

In this chapter, you need to introduce your testing strategy.
Do you employ units tests, end-to-end tests, or regression tests?
How can tests be executed?
You can probably name other questions related to testing.
In this chapter, you should provide answers to those questions.

You should also explain, why the testing strategy of your choice guarantees that your solution is functional.
On the other hand, keep in mind that 100% test coverage is not what you should primarily aim for.

## User testing

While testing is basically mandatory, user testing is not making this chapter optional.
On the other hand, I would highly recommend to perform user testing.
The inclusion of user testing may significantly enhance the overall impression of the work.

In this chapter, you need to describe the setup and process of user testing.
You may start by introducing your tester, their background, and expertise.
Rather than focusing on each tester introduce them as a group.
You should have at least three testers.

Next, you need to introduce user scenarios used for testing.
As the full description of each scenario can be quite long, you may provide only a summary.
The full description can be part of the attachments.

In order to perform user testing you also need some way of an evaluation.
You can measure how well testers perform, based on time or completion rate.
In addition, you can collect feedback as a free text.
Testers may also fill in [System Usability Scale](https://www.usability.gov/how-to-and-tools/methods/system-usability-scale.html) questionnaire.

At the end of the chapter, you must comment on the results of the testing.
What went wrong, where can be improved, what testers like on your software, etc ..

## Conclusion

You can briefly comment on the problem you solved and how.
You may also outline future work.

Imagine somebody just read the introduction and conclusion.
They should still have a basic idea of what problem you solved and have a high-level understanding of how you solved the issue.
