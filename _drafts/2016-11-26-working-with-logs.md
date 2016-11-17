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


### Logging vs prints

In my last post I recommended to switch from littering prints to a proper logging framework when the project grows. What is then the difference between "just" prints and logging? The answer is strategy. Logging can very well be implemented with prints, but on the other hand random prints here and there should not be called logging. Logging should always be implemented with a defined strategy in mind.

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

The second one looks much nicer. The prints are well formatted, timestamped and readable - the reader can extract lots of different information from these lines.





Having a consistent format comes also handy when you want to filter and search the logs for some specific information - for example when debugging. As you might know, Linux command line has wonderful utilities for just that. Standard formatting and meaningful messages enable you to do things like these:

`:~$ grep "ABCD" debug.log`

`:-$ diff <(head debug.log | cut -f3-) <(head debug2.log | cut -f3-)`

These tools deserve a post or 10 by themselves, so I recommend you to read for example xxx yyy in case you are not familiar with them.


# Before vs After

Another difference in debugging strategy between prints and logs is timing. Prints are usually inserted to debug a specific situation and only when you start debugging a problem. With logging we would _start_ the debugging with examining the logs that already exist, or at the very least reproduce the problem with logging enabled. By examining the logs we begin digging for clues about what might have happened in the code.
