Title: Awari AI
Date: 2010-02-21 09:01
Modified: 2010-02-21 09:01
Tags: awari, BASIC, porting
Slug: awari-ai
Authors: Tracy Poff

I've sorted out the BASIC version of Awari I'm porting into the 'draw the board'
routine, the 'make a move' routine and the 'incomprehensible AI' routine. The AI
seems to first sow from the first nonempty pit, then makes some weird comparison
and modifies a value:

```
860 FOR I=0 TO N-1:IF F(N)*6+K=INT(F(I)/6^(7-C)+.1) THEN Q=Q-2
```

The reason for that is fairly inscrutable. F is some array, and the program
claims to have a learning mechanism to improve the AI, so I suspect this is that
mechanism, but I'm not at all sure how it's meant to work. I think I'll have to
make a flow chart or something to decipher this thing. This would be easier if
the variables had meaningful names. I remember once, when I was first learning
to program, I thought that using meaningful names was a big waste of time, since
after all the code should be pretty self-evident, right? A second look at my
code after some weeks disabused me of that notion, and this serves to reinforce
that: code should be self-evident, but it won't be if you don't work at it.

Oh well. With any luck, I'll be able to sort this out with an hour or so of
concerted effort–it's just that reading BASIC is giving me a headache and I
haven't yet put in the requisite time. I must persevere!
