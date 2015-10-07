Title: Assembly
Date: 2015-06-17 15:20:56
Modified: 2015-06-17 15:20:56
Tags: assembly, games
Slug: assembly
Authors: Tracy Poff

Recently, I saw a new game from Zachtronics, [TIS-100][1], which was released
[on Steam][2] as an early access title on the first of June. In some ways,
calling it a game is overstating it: it's basically just a collection of
programming problems with an interface. The catch is that you're programming in
an assembly language on a virtual machine with unusual architecture. Problems
beyond the simplest will generally require you to take advantage of parallelism
(which is the primary distinguishing feature of the VM) to solve, which leads to
some rather different solutions for traditional problems. It's neat, and I
suggest checking it out.

Obviously, a game like that has a rather limited target audience. Case in point:
I have previously created my own little VM with a fake assembly language to play
with. The game is clearly made just for me, but how many others are likely to be
similarly interested? About 11,000 so far, [apparently][3].

I had good fun playing the game, which reminded me that I've been meaning to get
better at assembly. I've made some (very) simple programs in x86 assembly
before, but I could really use some more practice and study. I [looked into][4]
learning a little Z80 assembly for the Game Boy, which dovetails nicely with my
interest in video games, and even built a little test ROM, but ultimately it
seemed more useful to study something I'm a bit more likely to use. So, I've
been reading [Programming from the Ground Up][5], which teaches Linux x86
assembly. It's a little old, and could seriously use some proofreading, but it's
a decent resource.

One error to note here: in Chapter 4, on page 63, there is a lovely diagram
indicating the current state of the stack at a certain point during the
execution of the code. Lovely, but wrong. It has the order of the "Base Number"
and "Power" reversed. When I first saw it, the reversed order made me think that
the top of the stack was at the top of the diagram, when in fact it is not. I
worked it out, of course, but it did cause me to do some double- and
triple-checking of the code to be sure. Caveat lector.

As for what purpose I'll eventually put this to... I've got some ambitions to
write an emulator, and I hope to transfer this knowledge to other platforms. In
particular, I'm interested in looking at C64 assembly. It'd be nice to look at
some of those old games with a better idea of what's going on! For now, though
it's just learning for the sake of learning. I'm a way off from doing anything
very interesting with it.

[1]: http://www.zachtronics.com/tis-100/
[2]: http://store.steampowered.com/app/370360/
[3]: http://steamspy.com/app/370360
[4]: http://gameboy.mongenel.com/asmschool.html
[5]: http://download-mirror.savannah.gnu.org/releases/pgubook/ProgrammingGroundUp-1-0-booksize.pdf
