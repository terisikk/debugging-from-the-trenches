---
layout: post
title: "Problem Solving Mindset"
date: 2016-10-07 22:00:00 +0300
categories: 
  - issues
  - classification

featured_image: /images/blocker.jpg
comments: true
---

In my first real post I will talk about debugging as problem solving: the mindset and the thought processes, no matter what actual tools you use for it. You might have expected something more concrete, but bear with me: these first posts will be the foundation I use to make connections with other, more code-oriented topics.

So let's start with the basics:

## What is a bug?

> In IT, a bug refers to an error, fault or flaw in any computer program or a hardware system. A bug produces unexpected results or causes a system to behave unexpectedly. In short it is any behavior or result that a program or system gets but it was not designed to do. - [Technopedia](https://www.techopedia.com/definition/3758/bug)

As we can see, this definition is quite broad, but that is also the reality: we often call it a bug no matter how the program is at fault. The term encompasses things like _crashes_, _faulty logic_, _unresponsiveness_, _access violations_, _graphical errors_ etc. However, when reporting and fixing bugs, it is definitely beneficial to be more precise about the nature of a fault. Being specific helps everyone involved to comprehend the situation better.

Bugs can also be classified by the effect the have on the software as whole, the so called _severity_ of a bug. Each project has its own classifications, but let me give you an example that is somewhat widely used:

- _Blocker_: Bugs that prevent the program from working completely.
- _Critical_: A large feature of the software is broken.
- _Major_: The functionality does not meet the requirements.
- _Minor_: Does not prevent the program from functioning.
- _Trivial_: cosmetic or design errors. 

Even this grouping is not set to stone. What makes a bug for example a blocker or a critical differs widely between projects, companies and teams.

## The Principle of Confirmation

How exactly do we fix these bugs then? The tools vary widely, and everyone has their own preferences. Sometimes another tool is more fit for a certain problem than the other, but the process itself tends to stay fundamentally the same: **the Principle of Confirmation**. In a No Starch Press book _"The Art of Debugging"_ (Norman Matloff & Peter Jay Salzman, 2008) the authors define the Fundamental Principle of Confirmation as such:

> Fixing a buggy program is a process of confirming, one by one, that the many things you _believe_ to be true about the code actually _are_ true. When you find that one of your assumptions is _not_ true, you have found a clue of the location (if not the exact nature) of a bug.

That is actually nicely on par with the definition of debugging I came up with in the last post: both talk about the importance of the knowledge about the code. The more you understand about the system you are working with, the more likely you are to know where to look when a bug appears. When your assumptions are correct, they turn into facts, and you can use those facts to your advantage.

## When the unexpected happens

The first thing you should do when encountering a bug is to assess the situation. Take time to identify these items:

- How is the problem **reproduced**? What are the exact **steps and conditions** for it to occur?
- What is the **expected** behavior of the program?
- What is the **actual**, erroneous behavior?

If you are working in a ticket-based environment, the reporter of the bug might have already written these down. But even if you are not working with tickets, and even if you will be fixing the bug by yourself, you should make sure you know the answers to these questions. 

### Reproducibility

The reproducibility of the bug is by itself a good clue about the issue, so try to cause the bug to reappear, and gather information about it. Repeat the steps you did when the bug first occurred. Does it happen again? If it does, and does so consistently, you have a good baseline to start working with. The problem is most likely related to _faulty logic_, _wrong implementation_ or _syntax errors_.

If it does not, you are not so lucky. Definitely do not write it off as a "one time issue". Most of the time there are no such things, and not being able to reproduce something might be a sign of some deeper issues with things like _concurrency_, _system load_ or the _alignment of stars_. These are usually the hardest kinds of bugs to fix, since it is not easy to pinpoint a problem when you do not even know how to make it appear. These can also be so called [heisenbugs](https://en.wikipedia.org/wiki/Heisenbug): trying to examine the bug causes the program to work differently and hides the problem.

{% include captionimage.html src="stackoverflow.png" caption="Something is a miss..." %}

Some bugs can also be _sporadic_: they do not happen all the time, but still frequently. This kind of behavior can be traced back to things like _random values_, _uninitialized variables_, _timing issues_ or _corner cases_. For example, one time I was investigating strange behavior of a game object. Turns out the reason was an uninitialized `float` variable: a novice mistake. In C++ the variables are not initialized when _declared_, and so the initial value was some random value from the memory address, and not always 0.

Whatever the reproducibility rate of the bug is, _you now have some clues where to start looking_.

### Steps and conditions

Especially if you are reporting this bug to another party, be it a ticket-system in your company or an issue in Github or whatever, make sure you include all the data that you think is relevant for reproducing what happened. This includes of course clear details of the steps you took when the bug happened, but equally relevant could also be things like error messages, logs, your operating system or software versions.

{% include captionimage.html src="issues.png" caption="Github supports reporting issues" %}

However, there is a fine line between detailed and obfuscated. Attaching the whole source code, your browsing history and the video clip from your cousins wedding serves only as a distraction to the one who tries to figure out what is going on. So think carefully what might be important. When asking online about a piece of code, the instructions at Stackoverflow about providing a [Minimal, Complete and Verifiable](http://stackoverflow.com/help/mcve) example of your problem are especially useful. More than that, often times producing such an example can help you to solve the problem by yourself.

### Expected

Expected behavior is naturally the way that a program should work in this particular case. In some cases the expected behavior is clear: a buffer should not overflow, passwords should not leak etc. But there are cases where it is not that clear how the program should function. It might even be entirely possible that the thing you have encountered is actually not a bug at all, but a feature you were not aware of. 

I was implementing a feature to an HMI when I noticed that backstepping from a certain sub-menu moved me back to root menu instead of the previous menu. That was even inconsistent with how the other sub-menus on that level worked. Before submitting a bug report though, I glanced through the customer requirements. To my surprise, the documents clearly mentioned it as an intended feature: my initial assumptions of the situation were wrong.

### Actual

The actual behavior of the program is the embodiment of a bug. This can be just about anything, so once again: be precise of what happens if you explain it to someone else, as this also defines the aforementioned severity class of the bug. You might notice the bug for example as garbled output, unresponsiveness or missing elements.

## The first actions to take

Even before firing up a debugger, there are some things that can help with solving the problem. You should understand the value of these clues, often you see people rushing to ask for help from Stackoverflow even when the answer was literally before their eyes in the console.

### Errors and stack traces

If your program throws an error message you do not know the meaning of, try to remember the good advice [this book](https://www.google.fi/search?site=&tbm=isch&q=googling+the+error+message+book&gws_rd=cr&ei=nnT2V_2hFcKhsgGAh6aACg) gives. Chances are pretty good that you are not the first one to encounter such a problem. For beginner programmers, lists like [these](https://pbs.twimg.com/media/CtOm5jRXEAAomcq.jpg:large) can also be very helpful to decipher an error you do not understand. 

In Python, the error messages or _stack traces_ can often tell you the exact location where the error happened, or even the reason for a crash. 

{% highlight python %}
>>> print('One more Marine reporting, Sir — I've served my time in Hell.')
  File "<stdin>", line 1
    print('One more Marine reporting, Sir — I've served my time in Hell.')
                                               ^
SyntaxError: invalid syntax
{% endhighlight %}

Oops, another rookie mistake, apostrophes inside a string should be escaped with \\.

### Code Smells

Martin Fowler talks about "Code Smells" - bad practices in programming - in his classic programming book _Refactoring_, and Robert C. Martin builds his own list of smells on top of that in another classic: _Clean Code_. These smells are good hiding places for bugs, and obvious lines to start the search from. Even though a 2-line function can have a bug as well as a 2000-line, the error is much harder to spot from a place that is already cluttered. If your code adheres to the principles of [SOLID](https://en.wikipedia.org/wiki/SOLID_(object-oriented_design)), it is also much easier to debug. You can ignore the parts of the code that (most likely) have nothing to do with the problem, and focus on the relevant areas.

These are just examples of thing you can do to narrow down the problem space before even really starting to debug. I will probably talk about these with greater detail in the upcoming posts, so if you did not quite catch everything I tried to say, do not worry. 

## Conclusion

We have talked about the nature and classification of bugs. You have hopefully learned how to extract vital information from the behavior of the bug itself, and have some ideas about what kind of behavior relates to a certain kind of bug. The most important part to remember is that most of the time you have a lot of information and clues that can help you solve a problem even before using any tools. 

Next time I promise to venture into a more practical topic. I will talk about the first tool that just about everyone uses to debug their software: _prints_. 