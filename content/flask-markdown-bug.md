Title: Flask-Markdown bug
Date: 2015-10-07 08:01:59
Modified: 2015-10-07 08:01:59
Tags: quoted forsooth, flask-markdown
Authors: Tracy Poff

I encountered a mysterious bug in Flask-Markdown: footnotes in one document were polluting others. I noticed footnotes being duplicated in a markdown-formatted sidebar, and then I found them showing up on new pages altogether.

The (approximate) cause was obvious: markdown was keeping state between different renders.

It turns out that Python-Markdown allows you to instantiate a renderer with options set and reuse that, if you choose, and Flask-Markdown takes advantage of this. However, when using Python-Markdown in that way, you need to `reset()` the instance between renders.

Solution: change line 69 of Flask-Markdown's markdown.py from:

```python
        return Markup(self._instance.convert(stream))
```

to

```python
        return Markup(self._instance.reset().convert(stream))
```

Simple.

Unfortunately, it looks like the maintainer of Flask-Markdown hasn't been active on github in quite a while, so this problem may persist.
