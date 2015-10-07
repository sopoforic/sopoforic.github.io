Title: New project: cgrr-gamecube
Date: 2015-06-05 13:35:04
Modified: 2015-06-05 13:35:04
Tags: cgrr, gamecube
Slug: new-project-cgrr-gamecube
Authors: Tracy Poff

After about six hours of work, I've completed an initial release of a new
project: [cgrr-gamecube][1]. At the moment, it is able to parse GameCube GCI
file headers, plus decode the banner from the GCI file (if it's in CI8 format).

It also supports writing the GCI files back out, but only modifications to the
header are supported. That means no editing the banner, since it's stored in the
save data blocks, and not the header. In the future, I intend to add functions
specifically for replacing the banner.

Decoding the banner was something of a pain. The CI8 image format isn't very
complicated, I suppose. It's a 16bpp paletted format with 5 bits per channel
plus one transparency bit, with the image stored as a series of 8x4 pixel tiles
(documentation forthcoming--I used [this page][2], myself). Not complicated, but
annoying to work with, since I had to first rewrite the colors to a more usable
format, and second reorder the image data so it wasn't all tiles. Though in
retrospect I suppose I could have actually decoded the image as tiles and then
pasted the tiles into a new image in the right positions. Not sure which would
have been better.

Anyway, everything went pretty smoothly, my dislike of the image format aside.

I think I may put together a frontend so I can extract GCI files rapidly, to
support my (potential) future efforts in decoding GameCube save files. One more
item for the todo list, I suppose.

[1]: https://github.com/sopoforic/cgrr-gamecube
[2]: http://www.surugi.com/projects/gcifaq.html
