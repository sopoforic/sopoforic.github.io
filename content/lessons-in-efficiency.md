Title: Lessons in Efficiency
Date: 2012-08-17 00:52
Modified: 2012-08-17 00:52
Tags: Haskell, Project Euler
Slug: lessons-in-efficiency
Authors: Tracy Poff

I was working on [Project Euler problem 92](http://projecteuler.net/problem=92),
and having a great deal of trouble making my program run fast enough. I’m aware
of a trick that can be used to reduce the problem space, but I thought that with
only ten million numbers to check, it should be possible to do it
straightforwardly and just check them all, as long as I wasn’t too inefficient
doing it.

My first successful version took about three minutes to run–much too slow. I
eliminated a duplicate call to an expensive function, which brought me down to
about two minutes, and at length I managed to reduce the runtime down to about
thirty seconds–much better, though still very slow. I tried some alternate
techniques and just couldn’t make it go any quicker while still using a brute
force approach.

Now, there’s one important thing I haven’t mentioned: on the Windows PC I’m
using for development, the version of gcc included with the Haskell Platform
doesn’t work. I can’t figure out why, but it makes it impossible to compile
Haskell programs, so I’ve just been running them in the interpreter. Well, that
gives away the ending to this anecdote: I copied the program to a (much slower)
Linux PC and compiled it, and it ran in about five seconds. Even my first, very
inefficient attempt would have been fast enough to satisfy the one minute rule.
But I learned a bit by trying to make the interpreted version fast enough to
pass.

Lessons:

1. Squaring a number with (n^2) is significantly slower than doing it with (n *
n).
2. Arrays are faster to access than even fairly small lists.
3. It’s faster to compose several functions and then map them to a list than to
repeatedly map individual functions.

Of course, these apply to programs run through the interpreter–it’s quite
possible that at least the first of these might not hold if the program is
compiled. Maybe I’ll test it, some time.
