from wikidata.client import Client
import wikipediaapi

# for infobox scraping
import wptools as wp
import re
#from bs4 import BeautifulSoup as bs
#from urllib.request import urlopen
#import sys

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
company_titles = [t for t in company_titles if t.find("Category:") < 0]

for t in company_titles:
    page = wp.page(t)
    page.get_parse()
    infobox = page.data['infobox']
    if infobox is not None:
        if not 'traded_as' in infobox.keys():
            print(f"{t}\t!N/A! no traded_as")
        else:
            traded = infobox['traded_as'].split('}}')
            rgx = r"\{\{lse\|(.+)"
            syms = [re.findall(rgx, x,
                               flags=re.IGNORECASE)[0].split('|')[0] \
                for x in traded \
                if len(re.findall(rgx, x, flags=re.IGNORECASE)) > 0]
            if len(syms) == 0:
                rgx = r"\{\{aim\|(.+)"
                syms = [re.findall(rgx, x,
                                   flags=re.IGNORECASE)[0].split('|')[0] \
                    for x in traded \
                    if len(re.findall(rgx, x, flags=re.IGNORECASE)) > 0]
            if len(syms) == 0:
                print(f"{t}\t!N/A! no symbol found")
            else:
                ticker_sym = ','.join(syms)
                print(f"{t}\t{ticker_sym}")
    else:
        print(f"{t}\t!N/A! idk")
