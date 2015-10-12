Title: git update-index --assume unchanged
Date: 2015-10-12 12:43:20
Modified: 2015-10-12 12:43:20
Tags: git
Authors: Tracy Poff

Thanks to [this stackoverflow question](http://stackoverflow.com/questions/3319479/git-can-i-commit-a-file-and-ignore-the-content-changes), I've learned a useful git trick:

> git update-index --assume-unchanged [<file> ...]

and its counterpart:

> git update-index --no-assume-unchanged [<file> ...]

This pair of commands lets me keep a default file in the repo (e.g. a sample config) and modify it locally without git complaining about changed files. Handy!
