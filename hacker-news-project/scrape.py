import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get("https://news.ycombinator.com/?p=1")
soup = BeautifulSoup(res.content, "html.parser")
links = soup.select(".titleline > a")
subtext = soup.select(".subtext")

def sort_stories_by_vote(hnlist):
    return sorted(hnlist, key=lambda k:k["votes"], reverse=True)

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = item.get("href")
        vote = subtext[idx].select(".score")
        if len(vote):
            points = int(vote[0].getText().replace(" points", ""))
            if points > 99:
                hn.append({"title": title, "link": href, "votes": points})
    return sort_stories_by_vote(hn)

pprint.pprint(create_custom_hn(links, subtext))