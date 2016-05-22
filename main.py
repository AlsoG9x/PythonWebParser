import requests
from lxml import html

page = requests.get('https://boards.4chan.org/g/catalog')
tree = html.fromstring(page.content)

teaser = tree.xpath('//div[@class="teaser"]/text()')

print ('Description: ', teaser)

