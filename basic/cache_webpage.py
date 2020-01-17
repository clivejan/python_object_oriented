import time
from urllib.request import urlopen

class WebPage:
	def __init__(self, url):
		self.url = url
		self._content = None

	@property
	def content(self):
		if not self._content:
			print("Retrieving New Page...")
			self._content = urlopen(self.url).read()
		return self._content

webpage = WebPage("http://www.google.com/")

# get page first time
now = time.time()
content1 = webpage.content
print(time.time() - now)

# get page second time
now = time.time()
content2 = webpage.content
print(time.time() - now)

# check the contents from two requests are the same
print(content1 == content2)
