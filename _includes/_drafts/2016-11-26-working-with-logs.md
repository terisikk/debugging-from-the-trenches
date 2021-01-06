---
layout: post
title: "Working with logs"
date: 2016-11-26 16:00:00 +0300
categories:
  - logs
  - prints

featured_image: /images/trench3.jpg
comments: true
---

- Focus more on the debugging side of logging
- But a small introduction to what is good logging and how to python
- log levels
- filtering
- timestamping
- linux commands
- how it differs from prints


## Logging vs prints

In my last post I recommended to switch from littering prints to a proper logging framework when the project grows. What is then the fundamental difference between "just" prints and logging? The answer is strategy. Logging can very well be implemented with prints, but on the other hand random prints here and there should not be called logging. Logging should always be implemented with a defined strategy in mind.

Take a moment to compare these two outputs from program:

HERE WE ARE
1
2
3
End of loop
Calling getXXXX()...
  Name: Teemu Risikko
Error!

2016-11-17 09:00:45.255 xxx/yyy "Teemu Risikko"
...

The first one is clearly output from a program that has random print statements scattered throughout the code. There is no structure, no standard format and it contains tons of useless information.

The second one looks much nicer. The output is well formatted, timestamped and readable - the reader can extract lots of different information from these lines.





Having a consistent format comes also handy when you want to filter and search the logs for some specific information - for example when debugging. As you might know, Linux command line has wonderful utilities for just that. Standard formatting and meaningful messages enable you to do things like these:

`:~$ grep "Error" debug.log`

`:-$ diff <(cut -f3- debug.log) <(cut -f3- debug.log)`

These tools deserve a post or 10 by themselves, so I recommend you to read for example xxx yyy in case you are not familiar with them.


## Before vs After

Another difference in debugging strategy between prints and logs is timing. Prints are usually inserted to debug a specific situation and only when you start debugging a problem. With logging we would _start_ the debugging with examining the logs that already exist, or at the very least reproduce the problem with logging enabled. By examining the logs we start digging for clues about what might have happened in the code.

## Production environments

Logging is especially useful when implemented to a target production environment. When bug appears in production, the logs might be the only source of initial information you can get about the state of the system during the error. Usually you can not go and strap a debugger to a computer running your software: the machine might be remote or running your code embedded. The logging level enabled for production might differ from development, but hopefully at least errors are logged somehow. Otherwise you can only guess what could have possibly gone wrong. 

## Do not hide errors, log them

    Code example about printing "Error"

This is a common example in beginner questions at StackOverflow. The developer has learned about `try-except`, but is actually hindering their own work by hiding the actual error and believing that just catching an exception will make the program work. Even more harmful from the debugging perspective is this:

    Code example about passing the exception

In actual production code these could be annoying issues. If the logs contain a notification about an error without any further detail, it could be very hard for the person debugging it to deduce what has actually happened, and even more so if the error is omitted.

I always have a hard time writing the `except`-block in Python correctly, usually I make a typo and write is as `expect`. But that is actually not that far from the truth. When using `try-except`, I _EXPECT_ that at some point this exception will be encountered. Still, I definitely do _not_ want to hide the fact that it happened. So better to log the trace so that I can notice the _expected_ has happened.

    Code example about logging the trace

## Timing is information

One advantage of logging is that if you log with timestamps, you can examine timings. This information can of course help you to examine bugs that have something to do with time. 

For example, I was at first a bit baffled why sometimes some of my SQL queries were not executed when using SQLAlchemy. I had a rudimentary logging implemented that time, but it did include timestamps. I first noticed the bug when some values that I were sure that should have been in the database were missing. I examined the logs, and luckily I had at least logged the errors. The logs indicated that the connection to the database was closed seemingly in random, and was only re-established with the next query. If I would've had timestamps included, I might have noticed sooner that this happened in the mornings, or more specifically: after 8 hours of idle time when MySQL closed the connection automatically. 

Another time-related thing you can get out of well-implemented logs is the time it takes to execute something. If you notice that something takes significantly more time than it should, it might very well turn out to be a lead to that bug you are investigating. I was able to solve a bug in a Qt-application's animation with extensive timestamped logging: the logs revealed that the animation processing stopped during a data load and thus the animation took a second more than it should've taken. 

## Exchanging messages

The applications where logging really shines as a debugging method are pieces of software that use some kind of protocol to transmit data and messages between endpoints. It is usually hard or even impossible to debug such exchanges with a debugger, and even less so in production environment. However, logging can easily reveal problems with this kind of sequential exchange of information. 

##  Going further: automate!

