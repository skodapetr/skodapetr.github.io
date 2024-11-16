---
title: "Implementation bachelor thesis"
---
# Implementation bachelor thesis

The goal is to show the craftsmanship.
In other words, to demonstrate the ability to follow the software engineering process.
The main product is the [software](./software).

The text part of the thesis should contain following sections:
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

Please make sure you read the general notes regarding the [text](./text) in general.

## Introduction
The initial chapter should introduce a reader to the domain and introduce the problem you address.
You must not expect the reader to have any domain-specific knowledge.
Use this chapter to define the vocabulary and issues and reference relevant literature.

Once the domain is defined, introduce the setup and the problem and hint at a possible solution.
In the ideal case, you should forward the reference following chapter to also introduce the text outline.

## Related work
This is an important yet often overlooked part of the thesis.
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

Are there any issues that have not been addressed by existing solutions?
Are you producing an N+1 version of an already existing tool?
Is there a need for your solution?
What inspiration can you draw from the existing solution?
After reading the conclusions/summary section, the reader should have answers to all those questions.

## Analysis
In this part, you should analyze the issue/opportunity you are about to address.
You need to think about users, stakeholders, functionality, and other systems.

You should start with a description of the domain.
In other words, you system in the context of other systems and users.
You can employ [C4 model, system context diagram](https://c4model.com/diagrams/system-context#system-context-diagram) to visualize the context.

Next, you should list functional and non-functional requirements.
Non-functional requirements are sometimes called quality requirements.
Each requirement should be referenceable, i.e. have unique identifiers like F01, F02, N01, etc.

Functional requirements should be clear, using simple English and the same structure as "X can do Y".
For non-functional requirements, it is best to add some measures.
The requirement "system should be secured" is hard to measure and evaluate.

In addition, you can list use-cases.
A use-case is about a user and the added value of the software for the user.
As a result, "user can log in to the system" is not a good use-case as there is no value to the user.
Keep in mind that from this perspective user may always be a human but also another system.

If you have multiple use-cases you should utilize a use-case diagram.
Each diagram should communicate certain information to a particular audience.
As a result, it may be better to have multiple smaller use-case diagrams rather than one big one.
Optionally, you can elaborate on selected use-cases by providing user-scenarios.

Keep in mind that in this chapter, you are analyzing the required functionality from your software.
In other words, you are establishing the contract between the software and the user.
You do NOT design the software or the solution.

There is a sort of alternative content for this chapter.
The main difference is that you utilize different approaches to establish the contract.

You may start with a list of features.
Instead of use-cases, you can provide breakdowns.
Instead of requirements, you can list responsibilities.

## Design
In the previous chapter, you established the contract between the user and your software.
The aim of this chapter is to design software that would be able to fulfill that contract.

You should start from top-level decisions, architecture, technologies, and data storage.
As you progress you provide more detail.
A good idea is to utilize  L2 and L3 levels of the C4 model.

For each decision, you should introduce the problem, list solutions, discuss advantages and disadvantages, and explain your decision.

Let me demonstrate an example of using a library.
First, you need to specify expectations from the library.
What functionality do you need?
What language are you using?
Next, you list libraries that match your expectations.
For each library, you may provide examples of how to use the library.
You also list the advantages and disadvantages of using the library.
You can comment on the quality of documentation, community support, API, etc..
At this point, it should be clear which library is the best.
If there is no winner, you may pick one based on your preference.
In either case, you explain your decision.

## Developer documentation
It is not easy to draw a line between design and developer documentation.
You can assume that a software architect would read only the design section.
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
In this chapter, you need to introduce your testing strategy.
Do you employ units tests, end-to-end tests, or regression tests?
How can tests be executed?
You can probably name other questions related to testing.
In this chapter, you should provide answers to those questions.

You should also explain, why the testing strategy of your choice guarantees that your solution is functional.
On the other hand, keep in mind that 100% test coverage is not what you should primarily aim for.

## User testing
While testing is basically mandatory, user testing is not.
Thus, this is an optional chapter.
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
