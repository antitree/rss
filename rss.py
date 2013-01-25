import PyRSS2Gen
import datetime


class RSS(object):
    """ RSS wrapper class that creates an RSS feed for you"""

    def __init__(self, title, description):
      self.rss = PyRSS2Gen.RSS2(
        title = title,
        link = 'http://www.antitree.com',
        description = description,
        lastBuildDate = datetime.datetime.now(),
	
	items = [])

    def make_item(self, title=None, link=None, description=None, author=None, categories=None, pubDate=None, source=None):
        """Create an RSS item to add to the feed. Looking for title, link, description, author, 
        categories, pubdate, and source when possible. Returns an RSS2 item"""
        rssitem = PyRSS2Gen.RSSItem(title=title, link=link, description=description, author=author, categories=categories, pubDate=pubDate, source=source)
        return rssitem
        

    def add_item(self, item):
        """ Add an item to the RSS feed instance. must be a tuple object = "value", """

        self.rss.items.append(PyRSS2Gen.RSSItem(item))

    def to_xml(self, path="./output.rss"):
        """ Save the results in an XML format in the supplied path. If no path supplied, the default
        location is ./output.rss"""
        self.rss.write_xml(open(path, "w"))
        
    
