Title: ffcollection progress
Date: 2011-07-06 05:29
Modified: 2011-07-06 05:29
Tags: ffcollection, python
Slug: ffcollection-progress
Authors: Tracy Poff

I mentioned previously that I was working on a fanfiction database. Well, time
for an update: it’s in a functional state, though quite basic. I can feed it a
FanFiction.Net ID and it will download the fanfic and put it in the database
with some very basic metadata (author, ID, summary). Most recently, I’ve hacked
together an HTTP server using `http.server` so that I can accept commands over
HTTP. Currently, the only command it accepts is ‘add the fanfic at this URL’,
and it just responds with a status page and a copy of the form to add the fic to
favoritestracker. I really should use something a little more powerful than just
`http.server.BaseHTTPRequestHandler` for this--I really ought to create a
full-fledged web interface, instead of just a commands-over-http hack. But, for
the moment, that’s what I’ve got.
