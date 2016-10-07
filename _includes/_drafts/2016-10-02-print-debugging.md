---
layout: post
title: "Debugging With Prints"
date: 2016-10-02 16:00:00 +0300
categories: 
  - prints
  - debugging

featured_image: /images/trench3.jpg
comments: true
---

Print-debugging is most likely the first way that every new programmer uses to debug their code, probably even before they know what "debugging" is. That should be no surprise. Printing a message is usually among the first things we learn about a programming language. In Python 3 printing is of course done like this:

~~~ python
>>> print("Now I am become Death.")
Now I am become Death.   
~~~

Prints are a quick and easy way to get some feedback of the execution of your code. For example:

~~~ python
{% include p1/ex1.py %}
~~~

would print `Enlisting...`, and we would know that the function `enlist` is really executed by studying the output of the program.

The next logical step is printing the values of variables to know that they are what they should be. 

~~~ python
print("Enlisting:", name)
~~~

would of course in the first example print `Enlisting: Audie Murphy`.

In Python it is also very trivial to print the contents of a list:

~~~ python
>>> soldiers = ["Alvin York", "Ira Hayes", "Audie Murphy"]
>>> print(soldiers)
['Alvin York', 'Ira Hayes', 'Audie Murphy']
~~~

## Printing as a debug-tool
    - Everyones first tool
    - tool among tools
    - when to use
        - concurrent
    - when not to
    - version control
    - 

## Wolf fence algorithm

## String formatting in Python
    - % and format

There are two primary ways of formatting output in Python: the old way of using `%`, called _string interpolation_, and the new way: `string.format`.

## str, repr and format
    - differences, usages
    - c++ <<, js prototype.inspect
    - warn of overuse


## pprint
    - usage, cons

## Conclusion