#!/usr/bin/env python

import sys
import os
import urllib
import json
import wikisnip
import re
 

def get_wiki_raw(query):
	base_url = "http://en.wikipedia.org/w/index.php"
	params = {'action':'raw', 'title':query}
	params = urllib.urlencode(params)
	f = urllib.urlopen(base_url + "?%s" % params)
	return f.read()

def get_wiki_summary(query):
	base_url = "http://en.wikipedia.org/wiki/"
	url = base_url + "%s" % urllib.quote(query)
	print wikisnip.wikisummary(url)

def get_wiki_page(query):
	base_url = "http://en.wikipedia.org/wiki/"+urllib.quote(query)
	page = wikisnip.wikisnip(base_url).prettify
	print page

def print_usage():
	print "You must supply an argument for search"

def main():
	if len(sys.argv) != 2:
		print_usage()
		sys.exit(1)
	query = sys.argv[1]
	get_wiki_summary(query)

if __name__ == '__main__':
	main()
