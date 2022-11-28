import requests as req
from bs4 import BeautifulSoup
import pprint as p

res = req.get('https://news.ycombinator.com/')
res2 = req.get('https://news.ycombinator.com/news?p=2')
res3 = req.get('https://news.ycombinator.com/news?p=3')

soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
soup3 = BeautifulSoup(res3.text, 'html.parser')

link1 = soup.select('.titleline > a')
link2 = soup2.select('.titleline > a')
link3 = soup3.select('.titleline > a')

mega_links = link1+link2+link3

sub1 = soup.select('.subtext')
sub2 = soup2.select('.subtext')
sub3 = soup3.select('.subtext')
mega_subs = sub1+sub2+sub3


def sorted_by_votes(hn):
    return sorted(hn, key=lambda k: k['votes'], reverse=True)


def customized_news(links, subs):
    chn = []
    for index, item in enumerate(links):
        title = links[index].getText()
        link = links[index].get('href',None)
        score = subs[index].select('.score')
        if len(score):
            points = int(score[0].getText().replace('points', ''))
            if points > 99:
                chn.append({'title': title, 'link': link, 'votes': points})
    return sorted_by_votes(chn)


if __name__ == '__main__':
    p.pprint(customized_news(mega_links, mega_subs))
