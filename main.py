import network2 as nx
import pylab as plt

from crawler import Crawler, Page, Document, Corpus

if __name__ == '__main__':
    start_page = Page('http://info.cern.ch/hypertext/WWW/TheProject.html')
    crawler = Crawler(start_page)
    crawler.crawl()


    web_graph = nx.DiGraph()
    edges = []
    edges2 = []

    for page in crawler.web:
        for link in page.links:
            edges.append((hash(page.address), hash(link)))

    web_graph.add_edges_from(edges)
    nx.draw(web_graph)
    plt.show()
    pageRanks = nx.pagerank(web_graph)
    for page in crawler.web:
        page.page_rank = pageRanks[hash(page.address)]
    pages = sorted(crawler.web, key=lambda p: p.page_rank, reverse=True)

    corpus = []
    for page in pages:
        corpus.append((page.address, page.text))

    corpus2 = []
    for corp in corpus[0:3]:
        corpus2.append((Document(corp[0], corp[1])))

    corp = Corpus(corpus2)
    print(corp.rank(query="World-Wide Web"))



