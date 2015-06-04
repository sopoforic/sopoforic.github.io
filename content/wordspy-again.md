Title: WordsPy, again
Date: 2010-05-16 13:10
Modified: 2010-05-16 13:10
Tags: wordspy, python
Slug: wordspy-again
Authors: Tracy Poff

Well, the bad news is that wordspy still does nothing other than scroll new
lines onto the screen. The good news is that it does it in a better way.

In order to deal with letters dropping (due to letters below them being removed)
at the same time as a new line was scrolling up, it was necessary to re-engineer
the whole thing. Now letters store their current location, and it’s modified
whenever necessary by the newlinescroll and drop actions. This does have some
other benefits, too. For example, it simplifies drawing the new line onto the
screen somewhat. Before, I was doing:

```python
for col in range(10):
    screen.blit(Game.letters[6][col].image, (64*col, 481))
```

Now, since I initialize the letters with their location, I can just do:

```python
for letter in Game.letters[6]:
    screen.blit(letter.image, letter.rect)
```

Which is rather more readable.

Lesson learned, though: don’t forget to empty the dirty rectangles list after
updating the screen. Once it grows to 64 items or so, it noticeably slows down
the game. I’m fairly sure it shouldn’t contain more than a dozen or so items
under normal usage, but I’ll have to remember to keep an eye on it.
