Title: LETTER, a simple guessing game
Date: 2010-02-11 22:09:00
Modified: 2010-02-11 22:09:00
Tags: python, game, porting, BASIC
Authors: Tracy Poff

Recently, I've been looking through a book called <em>Basic Computer Games: Microcomputer Edition</em>, edited by David H. Ahl. The book contains lots of type-in computer games written in Microsoft BASIC for the Altair. A fair number of these 'games' are more like toys, and some aren't even interactive, but a few look like real fun, and they're all little pieces of computing history, which I find very interesting.

I thought I'd port a few of the more interesting games to a more modern language so people could check them out and see how far we've come (or, in some cases, how far we haven't come). Of course, I thought I'd start by doing exactly what I didn't set out to do, and port a very simple and not very interesting game, just to get a feel for it. Even this gave me a little pause, as I'll get into. First, the game: <a href="http://www.atariarchives.org/basicgames/showpage.php?page=99" target="_blank">Letter</a>, by Bob Albrecht. That link leads to a scan of (a different edition of) the book I got the game from, so you can see the original BASIC code I was porting. Programmers among us will recognize that it's extraordinarily simple, and, for a BASIC program, quite clean and readable. One thing gave me a little trouble:

```
510 FOR N=1 TO 15: PRINT CHR$(7);: NEXT N</pre>
```

This line didn't seem to affect the output in the printed sample run of the game, so I got an Altair emulator, just to be sure. Indeed, it doesn't actually print, though I have no idea why. Whatever the reason, I left it out so as to faithfully reproduce the game as it was on the original system, whatever the code says.

A part of my intention in porting these is to provide sample code for people who may be interested in learning to program; these simple games should prove to be pretty easy to understand for anyone who cares to look. Having just read through quite a lot of BASIC code, I wasn't in a very pythonic frame of mind when writing this, but I think it'll be clear enough.

Enough about my troubles, though. You can find the game <a href="http://bitbucket.org/sopoforic/letter/">here</a>. If you have python installed, you can just get <a href="http://bitbucket.org/sopoforic/letter/raw/4a46e69f19b3/letter.py">the tiny python source file</a>. If not, or if you're not sure, you can get <a href="http://bitbucket.org/sopoforic/letter/downloads/LETTER.zip">a ZIP with a Windows executable</a>, instead, which should run on anything from Windows 95 through Vista. If it won't run, or complains of missing files, you may need <a href="http://www.microsoft.com/downloads/details.aspx?FamilyID=9b2da534-3e03-4391-8a4d-074b9f2bc1bf&amp;displaylang=en">this</a>.

I'll port something more interesting, and hopefully more fun, next time. Until then, I HAVE A LETTER. START GUESSING.