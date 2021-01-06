---
layout: post
title: "Debugging With Prints"
date: 2016-11-06 18:00:00 +0200
categories: 
  - prints
  - formatting

featured_image: /images/letter.jpg
comments: true
---

Print-debugging is most likely the first way that every new programmer uses to debug their code, probably even before they know what "debugging" is. That should be no surprise: printing a message is usually among the first things we learn about a programming language. And that is why I would like to discuss it first.

Now, there will be people that will arrogantly tell you that prints should _never_ be used to debug programs, but let me make this clear to you from the start:

> Console prints are just another tool in a developer's toolkit. - Franklin D. Roosevelt, probably 

Keep in mind though that they certainly are _not_ the best tool for many use cases, but sometimes useful nevertheless. Like any tool, printing has its strengths and weaknesses, and a skilled developer knows when to use a tool as well as when not to. 

The latter part of this post will focus a bit more in the implementation details of Python than some other posts, but I hope that the first part will still be useful to a more general audience. In Python 3 printing is of course done like this:

~~~ python
>>> print("Now I am become Death.")
Now I am become Death.   
~~~

Prints are a quick and easy way to get some feedback of the execution of your code. For example:

~~~ python
{% include debugging-from-the-trenches/p2/ex1.py %}
~~~

would print `Enlisting...`, and we would know that the function `enlist` is really executed by studying the output of the program.

The next logical step is printing the values of variables to know that they are what they should be. 

~~~ python
print("Enlisting:", name)
~~~

would of course in the first example print `Enlisting: Audie Murphy`.

## Printing as a debug-tool

The main reason prints are still commonly used is how easy they are to apply for variety of purposes. Prints can be inserted to inspect the flow of the program and to output the values of variables. These are of course the two first use cases a _debugger_ would be used for, and _I strongly encourage to use one_, if present. But sometimes we do not have the benefit of having a debugger ready to use. Prints, on the other hand, are almost always available. 

For example, one time I was working in an environment where we used QtCreator to develop a QML-application. The only problem was that the pre-installed version of QtCreator had a bug: QML-side variables could not be inspected during debugging. The easiest solution? Well placed `console.log`s. This was of course an issue with the work environment, but installing a new version of the IDE was not trivial at that point. So prints were a necessary substitution for the time being: sometimes we need to make use of what we have. Be sure to escalate these sorts of problems though.

Sometimes a debug build can also be quite heavy, and slow the execution of the program so that some conditions are hard to reach. Prints can be used to debug in a situation like this, though keep in mind that when investigating a threaded timing issue, even an added print can slow the program enough to make the problem seem to disappear.

## Binary search

The typical way of using prints is to _binary search_ the code for the part where the bug appears. You start top-down by inserting prints at a high level hierarchy, as near as the place you think the bug has occurred. If your assumption is correct, you then move to inserting a print to an earlier point where you think the bug should not have yet happened. When you track down the bug to for example a single function call, you can then move down in the hierarchy to the function level and continue with the same tactic. 

Of course this kind of debugging is quite tedious and time consuming, and efforts should be made to make it unnecessary. Be sure to remember the topics of the previous post, too. For example, it the code spits an error, you can most likely see the problematic area from the error message. The root cause itself might of course be somewhere earlier in the code, but that would be the first place to start the search. 

## Disadvantages and how to deal with them

The top reasons of being concerned about using prints include at least the time it usually takes compared to other methods, and the impact it has to code quality. 

When using a language like C++, adding prints iteratively will force us to recompile the code with every cycle, and that can be slow in a big project with a ton of dependencies. This is a situation when the normal ease and speed of prints is not present - you should really think of something else, for example logging. Luckily with scripting languages like Python this is less of a problem.

If you use a lot of prints to track down a problem, you will end up with a codebase littered with useless prints when the problem is finally solved. This is of course a problem: to keep your code clean you should remove the prints that do not add any value. You can make the cleanup easier by removing unnecessary prints on the go: if you track down the problem to a more specific part of the codebase, you should at the same time remove the more general prints. 

At this point, having and _using_ a version control system (such as git) helps with the cleanup. We can use the VCS to get a diff of the project and to discard the changes to files where only prints were added, then manually remove the rest in the list (we *did* make a commit before starting the bug hunt, didn't we?). Debug-prints should definitely not be pushed to a central repository: they have the tendency to stay there and bother others. Make everyone a favor and just remove unnecessary prints if you encounter them.

{% include captionimage.html src="p2/gitdiff.png" caption="With git diff you can easily track the changes to your files." %}

Having a huge amount of useless prints can actually even make the console cluttered with noise, making it hard to spot the _relevant_ prints. When you notice you are using a lot of prints and for some reason you also need to keep them, it is a good time to switch to a logging framework that will have useful features like different log levels and logging to a file. I will make a separate post of logging later. 

## Print techniques in Python

When you want to make your prints a bit more informative, you need to know how to format your strings to make the output appear like you want it to. This knowledge will also be useful when implementing a logging system or a command line interface, or in general when you need to operate with strings. 

There are two primary ways of formatting output in Python: the old way of using `%`, called _string interpolation_, and the new way: `string.format`. Python 3.6 will also feature a new, more compressed way. I'll cover all of them briefly:

~~~ python
# String interpolation
>>> print("I hereby grant %s to %s %s." % (decoration, rank, name))
# String formatting
>>> print("I hereby grant {} to {} {}.".format(decoration, rank, name))
# Python 3.6 f-strings
>>> print(f"I hereby grant {decoration} to {rank} {name}.")

I hereby grant a Medal of Honor to Lieutenant Audie L. Murphy.
~~~

At the time of this post, most of the time I would use `string.format`, but at some point you will most likely encounter formatting done with interpolation, so it is good to understand the syntax. F-strings will probably become popular when 3.6 comes out. 

These are just basic examples, especially the newer ways are very flexible in what you can print and how. [PyFormat.info](https://pyformat.info/) has a great overview of the first two techniques, I recommend you to at least skim it through. F-strings are explained extensively in this [PEP](https://www.python.org/dev/peps/pep-0498/).

## \__str__ and \__repr__

When printing instances of your own classes, you have probably noticed that sometimes the output is not as helpful as you would like. Let's consider the following example:

~~~ python
{% include debugging-from-the-trenches/p2/ex2.py %}
~~~

What this script will output is something like this:

`The captain of <__main__.BattleShip object at 0x7fdca3d8f4a8>. <__main__.BattleShip object at 0x7f7cc78504a8>.`<br/>
`[<__main__.BattleShip object at 0x7f7cc78504a8>, <__main__.BattleShip object at 0x7f7cc78504e0>]`

So not very handy, at least from a debugger's point of view. Of course in the case of the first ship, we could use `position.format(ship1.name)`, but for the sake of learning, let's dive into some other means. 

Let's first talk about `__str__`. `__str__` is one of Python's special methods or _dunders_ (double underscore). When implemented, the `__str__` method will be called for example when the value is printed or converted to a string with `str()`. It is of course expected that the method returns a string. `__str__` can be quite useful sometimes - you could do something like this:

~~~ python
{% include debugging-from-the-trenches/p2/ex3.py %}
~~~

This would change the ouput to:

`The captain of battleship USS Arizona.`

However, `__str__`  will not work with the second case, for that you need `__repr__`. It is meant to be unambiguous, so define your `__repr__` to return a string that you expect to be unique. For example:

~~~ python
{% include debugging-from-the-trenches/p2/ex4.py %}
~~~

Now the list would be printed like this:

`[<Battleship object: BB-39>, <Battleship object: BB-44>]`

Much more useful when reading the prints!

## pprint

The [pprint](https://docs.python.org/3.5/library/pprint.html) module comes also handy for a debugger when printing data structures. In the example of our lists (and combined with `__repr__`), using pretty printing can make the output much more readable, especially with nested structures. 


~~~ python
>>> patrol_shifts = [[ship1, ship2], [ship1], [ship2, ship3]]
>>> print(patrol_shifts)
[[<Battleship object: BB-39>, <Battleship object: BB-44>], [<Battleship object: BB-39>], [<Battleship object: BB-44>, <Battleship object: BB-61>]]
>>> from pprint import pprint
>>> pprint(patrol_shifts)
[[<Battleship object: BB-39>, <Battleship object: BB-44>],
 [<Battleship object: BB-39>],
 [<Battleship object: BB-44>, <Battleship object: BB-61>]]
~~~

The output certainly is easier to examine when formatted with `pprint`. 

## Conclusion

Using prints as a way of debugging is certainly popular and sometimes even necessary, but that is also why every developer should understand the limitations and disadvantages of the technique. Most of the time when a project grows, you are probably better off replacing prints with logging or using a debugger. Even so, the understanding about string formatting in python will not be useless: the principles described here are used elsewhere too. 