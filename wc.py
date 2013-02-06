#!/usr/bin/python
import os
import sys
import operator


def wc(text, f = None):

	if (f is None):
		f = sys.stdout
	
	words = {}

	wordlist = text.lower().split()
	for rec in wordlist:
		try:
			words[rec] = words[rec] + 1
		except KeyError:
			words[rec] = 1
	
	sorted_words = sorted(words.iteritems(), key=operator.itemgetter(1))
	for item in sorted_words:
		print>>f, item

	if (f is not sys.stdout):
		f.close()
