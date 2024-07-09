import feedparser
NewsFeed = feedparser.parse("")

entry = NewsFeed.entries[1]

print(entry.published)
print("===================")
print(entry.published_parsed)