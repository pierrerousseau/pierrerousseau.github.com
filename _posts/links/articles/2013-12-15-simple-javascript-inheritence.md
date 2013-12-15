---
layout: post
categories : [links, articles]
tags : [javascript, closure, inheritance]
title: "Simple JavaScript Inheritance"
---
{% include JB/setup %}

#### [Simple JavaScript Inheritance] by [John Resig], 2008.

##### Abstract (article introduction)

I’ve been doing a lot of work, lately, with JavaScript inheritance – namely for my work-in-progress JavaScript book – and in doing so have examined a number of different JavaScript classical-inheritance-simulating techniques. Out of all the ones that I’ve looked at I think my favorites were the implementations employed by base2 and Prototype.

I wanted to go about extracting the soul of these techniques into a simple, re-usable, form that could be easily understood and didn’t have any dependencies. Additionally I wanted the result to be simple and highly usable.


##### Personnal opinion

In this article John Resig gives and comments a source code implementing inheritance in JavaScript. It would have been interesting to have his view on other inheritance technics and to know why he has chosen to present this one. However the code is simple and well explained. In addition to the main subject, I think the implementation of *super* is one of the most brilliant example of closure I ever seen : it's simple and powerful, understand it, and you'll understand closures.


[Simple JavaScript Inheritance]: http://ejohn.org/blog/simple-javascript-inheritance/
[John Resig]: http://ejohn.org/
