Title: Arrays for Fun and Profit
Date: 2010-02-21 10:48
Modified: 2010-02-21 10:48
Tags: autofill-ebay, javascript, greasemonkey
Slug: arrays-for-fun-and-profit
Authors: Tracy Poff

My greasemonkey script for filling in a bid on eBay started out fairly horrible,
referencing element IDs that seemed to differ based on the phase of the moon.
It was terribly difficult to maintain and did not function well.

Epiphany: I discovered an element ID I could safely use that seems constant.
Also, discovered that `document.getElementsByName` seems to work in (at least
recent versions of) firefox--wasn’t there some recommendation against using that
a while back? My knowledge of javascript is poor. Anyway, between those two, it
became much simpler to maintain the script, and it worked much better, to boot.

Epiphany the second (third?): Javascript arrays let you do `array.push(value)`,
so now I push the patterns into an array, which means I can divide them up by
language and add new ones without worrying about which index the new pattern
should use. Super. Now adding a new currency/language pair is as simple as
adding a single line pushing the pattern into the array.

Unfortunately, I can’t safely (for my paranoid definition of safe) just run the
regex on the whole document–if a sneaky auctioneer inserted “Enter US $500.00 or
more” in the auction description, and the auction was actually in another
currency, then the English/USD pattern would pick up that $500 text before the
other-currency patterns ran, and the bid box would be filled with that value. Of
course, the user would still have to click the button to place the bid, and then
confirm it, but remember: paranoid. As long as eBay doesn’t decide to remove the
table IDs or something, though, this shouldn’t be an issue.

Next up is to try to get the script to work on the outbid pages that present
themselves immediately after entering a bid that’s too low. Magic 8-Ball says:
outlook good.
