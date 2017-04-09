#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from workflow import Workflow

def main(wf):
	
	import urllib2
	from bs4 import BeautifulSoup
	from xml.dom.minidom import Document

	request = urllib2.Request("http://feed.smzdm.com/")
	request.add_header("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36")

	soup = BeautifulSoup(urllib2.urlopen(request).read())

	for child in soup.find_all("item"):
		if (not child.title.string is None) and (not child.description.string is None):
			wf.add_item(child.title.string, child.description.string, arg=child.link.string, valid=True)
	
	wf.send_feedback()
	
if __name__ == "__main__":
	wf = Workflow()
	sys.exit(wf.run(main))