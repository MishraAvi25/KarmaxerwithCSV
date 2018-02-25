from lxml import html
import requests

def get_dates():
    page = requests.get("https://www.reddit.com/r/funny/top/?sort=top&t=day")

    tree = html.fromstring(page.content)

    date = tree.xpath('//time[@class="live-timestamp"]/text()')

    return date