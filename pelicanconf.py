#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Tracy Poff'
SITENAME = u'Sleepy Coding'
THEME= 'foundation-default-colours'
FOUNDATION_FRONT_PAGE_FULL_ARTICLES = True
SITEURL = u'https://sopoforic.github.io'
OUTPUT_PATH = u'output'
STATIC_PATHS = [u'images', u'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    u'extra\\favicon.ico': {u'path': u'favicon.ico'}
}
TYPOGRIFY = True

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('@TracyPoff', 'https://twitter.com/TracyPoff'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
