Title: A Fast Algorithm for Computing Fibonacci Numbers
Date: 2009-10-10 10:48:00
Modified: 2009-10-10 10:48:00
Tags: python
Authors: Tracy Poff

I came across an algorithm for computing Fibonacci numbers in [a paper by
Takahashi Daisuke](http://ci.nii.ac.jp/naid/110002725383/en); the paper's in
Japanese, but the pseudocode of the algorithm is plain enough that it's easy to
understand, even if I can't read any of the explanation. I've implemented it in
python, and it's decidedly slower than the Fibonacci function in Mathematica,
though that's to be expected. My implementation takes quite a few seconds to
compute F(2^20) but is quick for numbers below about F(2^15), with the
additional benefits of not computing absurdly huge floats or recursing a million
times.

The algorithm is apparently a refinement of another (perhaps well-known?)
algorithm, which computes Fibonacci numbers from the product of Lucas numbers.
I'll have to look into it to see just how it works.

Edit: After some investigation, a large part of Mathematica's apparent advantage
is in its faster display, rather than faster computation, though Mathematica
does still beat my python program by a rather huge amount--Mathematica computes
Fibonacci[2^23] in about 0.2 seconds, while my program takes just over five
seconds. This disparity increases as the argument grows larger. Also, found an
English version of that paper. Neat.
