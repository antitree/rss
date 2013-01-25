rss
===

Simple RSS wrapper that exports content to an rss feed. 

usage
===

import rss

feed = rss.RSS("This is the title of my feed", "This is the description of my feed")
item1 = feed.make_item(title="Title of my first item")
feed.add_item(item1) 
feed.to_xml("./output.rss")
