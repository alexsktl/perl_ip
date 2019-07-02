import requests
from bs4 import BeautifulSoup
from collections import deque


def find_shortest_path(start, end):
    path = {}
    path[start] = [start]
    Q = deque([start])

    while len(Q) != 0:
        page = Q.popleft()
        links = get_links(page)

        for link in links:

            if link == end:
                return path[page] + [link]

            if (link not in path) and (link != page):
                path[link] = path[page] + [link]
                Q.append(link)

    return None


def get_links(page):
    r = requests.get(page)
    soup = BeautifulSoup(r.content, 'html.parser')
    base_url = page[:page.find('/wiki/')]
    links = list({base_url + a['href'] for a in soup.select('p a[href]') if a['href'].startswith('/wiki/')})
    return links


k = 'https://en.wikipedia.org/wiki/'
print('Write the starting article \n')
s=input()
print('Write the ending article \n')
e=input()
print(find_shortest_path(k + s, k + e))
print(find_shortest_path(k + e, k + s))
