---
layout: post
title: "About the blog"
date: 2016-10-01 16:00:00 +0300
categories: 
  - meta
  - about

featured_image: /images/trench3.jpg
comments: true
---

This blog aims to be a series of articles about **debugging**. I will talk about a range of varying topics around the area, like _inserting prints_, _stepping through the code_ and _profiling_.

Code examples in this blog will mostly be written in **Python 3.x**, mainly because it is the language I am most competent with, but also because of the popularity and readability. As a side note: if you are still using Python 2.x, I strongly recommend you to shift to 3 - there rarely is a reason not to, nowadays. Some of the examples are bound to be Python specific, but the topics in general can usually be applied to other programming languages too. From time to time I might even take a side step from Python to other languages and tools.

I myself have meddled with programming since high school, and that hobby eventually lead me to abandon my initial plans of studying medicine, and I instead applied to the Faculty of Information Processing Sciences in the University of Oulu. I now work as a Software Engineer in automotive business, but my interest in topics of software development is certainly not limited to only those in my area of work.

## Why From the Trenches?

_"From the Trenches"_ usually means that someone speaks with - often long and painful - experience of the subject. While I certainly do have hands on experience of many sorts of debugging, the title itself is a wordplay with the theme I am going to sprinkle my code examples with: war history. Because let's face it, aren't we all tired about the same `user = User()` and `class CashRegister` examples? Time for something more refreshing! Why not instead debug why the _Eagle's Nest_ does not receive reports from the field? Or try to work out the inner workings of an _Enigma-machine_ with writing tests? And moreover, war history of all fronts is another one of my great interests, so the crossover makes the whole process of writing this more fun for me.

The images of the theme used in this site are mostly taken from [http://sa-kuva.fi/](http://sa-kuva.fi/), a site that kindly allows the usage of images from the archives of The Finnish Defence Forces. 

## What is debugging?

You might be familiar with the term, but let's conjure up some definition: according to a Google-search, to debug is to _"identify and remove errors from (computer hardware or software)"_. That is a good definition, and it describes the word quite literally. However, for the purpose of this blog, I would like to use a bit different definition that I personally and arrogantly came up with:

> Debugging is the process of gaining an understanding of how a system works, and/or why it does not work like expected (I, 2016).

By redefining the term, I can handily limit myself to focus on how to _identify_ bugs, and leave the best practices of fixing them to someone else. The definition also justifies talking about topics that do not necessarily have anything to do with bugs, like optimization and working out what makes some piece of code tick. Notice that I, in purpose, distinct the term from _using a debugger_.

## Motivation

I have noticed that debugging, as important and common task it is, is rarely directly taught anywhere. The justification for that seems to be that the tools in software development change so fast, that teaching how to use some tool is useless. However, I believe that the _concepts_ are not limited to certain tools. For example, learning how to use one debugger can give a mental model that can be applied to usage of other similar software. Even more important is the ability and courage to trace a problem backwards to find the root cause, and that ability is certainly not limited to software development.

When first learning how to code, people might not fully understand what the lines they write do and mean, and thus do not have an idea where to look at when something goes wrong. That often leads to [shotgun debugging](https://en.wikipedia.org/wiki/Shotgun_debugging). This is a phase where a systematic debugging approach - be it prints, logs or a debugger - would be of tremendous help. When you do not have an understanding of what the lines of code actually do, it is pretty clear that you will not understand when they do _not_ work.

Now I will try to share some of the things I have learnt about debugging, and hopefully even learn something new in the process.




