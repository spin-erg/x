from wikidata.client import Client
import wikipediaapi

# for infobox scraping
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import re
import sys

client = Client()
lse_company_list = client.get('Q7110731', load=True)
wp_list_cat = lse_company_list.attributes['sitelinks']['enwiki']['title']

wiki_wiki = wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI
)

cat_entity = wiki_wiki.page(wp_list_cat)
preamble_links = ['List of companies listed on the London Stock Exchange',
                  'FTSE 100 Index', 'FTSE 250 Index']
assert list(cat_entity.categorymembers.keys())[0:3] == preamble_links

company_titles = list(cat_entity.categorymembers.keys())[3:]

# infoboxes aren't given by the Wikipedia API library so get manually:
for t in company_titles:
    print(f"{t}:", end="")
    u = wiki_wiki.page(t).fullurl
    full_page = urlopen(u)
    soup = bs(full_page, "lxml")
    infobox = soup.find('table', class_ = 'infobox vcard')
    if infobox is not None:
        trades_as = infobox.find(attrs={"title": "Ticker symbol"})
        if trades_as is None:
            print("\t? N/A ?")
        else:
            trades_info = trades_as.parent.find_next("td")
            lse_ticker = trades_info.find_all("a", attrs={
                "title": "London Stock Exchange"})
            if len(lse_ticker) == 0:
                lse_ticker = trades_info.find_all("a", attrs={
                    "title": "Alternative Investment Market"})
            if len(lse_ticker) > 0:
                sym_list = []
                for ticker in lse_ticker:
                    sym = ticker.find_next('a').text
                    sym_list.append(sym)
                ticker_sym = ','.join(sym_list)
            else:
                print(f"Manually check: {u}")
            print(f"\t{ticker_sym}")
