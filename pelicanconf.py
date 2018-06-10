#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Pierre'
SITENAME = "Pierre's website"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),)

# Social widget
SOCIAL = (
    ('stack-overflow', 'https://stackoverflow.com/users/4596254/pierre'),
    ('github', 'https://github.com/pierrerousseau'),
    ('hacker-news', 'https://news.ycombinator.com/user?id=proussea'),
    ('linkedin', 'https://fr.linkedin.com/in/rousseaupierre/en'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "themes/hyde-pr"
PROFILE_IMAGE = "avatar.png"
BIO = """I'm a software engineer. <br />
I like to write code slowly but with agility and to test new tools. <br />
This website has been made with the help from <a href="http://getpelican.com/">Pelican</a> and <a href="https://github.com/jvanz/pelican-hyde">Hyde</a>.
"""
