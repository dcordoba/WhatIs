import itertools
import urllib2
import urlparse
from bs4 import BeautifulSoup

try:
    from google.appengine.api import urlfetch
except ImportError:
    urlfetch = None

def wget(url):
    if urlfetch:
        return urlfetch.fetch(url).content
    else:
        req = urllib2.Request(url)
        req.add_header("User-Agent", "Mozilla/5.0 (Compatible)")
        return urllib2.urlopen(req).read()

def wikisummary(url):
	html = wget(url)
	soup = BeautifulSoup(html)
	div = soup.find('div', {'id':'mw-content-text'})
	snip = BeautifulSoup('')
	for node in div.childGenerator():
		if (isinstance(node, basestring) or
			node.name.lower() not in ['p']):
			continue
		if node.name.lower() == "h2":
			break
		snip.append(node)
	return snip.p.text

def wikisnip(url):
    html = wget(url)
    soup = BeautifulSoup(html)

    div = soup.find('div', {'id': 'bodyContent'})

    snip = BeautifulSoup('')

    for node in div.childGenerator():
        if (isinstance(node, basestring) or
            node.name.lower() in ["table", "script"] or
            node.get('id') in ["siteSub", "contentSub", "jump-to-nav"] or
            node.get('class') in ['dablink', 'toclimit-2']):
            continue

        if node.name.lower() == "h2":
            break
        snip.append(node)

    for a in snip.findAll('a'):
        if a.get('href'):
            a['href'] = urlparse.urljoin(url, a['href'])

    return snip
