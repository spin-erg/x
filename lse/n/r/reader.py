import requests

from bs4 import BeautifulSoup as bs

## Pretty sure cookies not needed for LSE?
# from cookie_handler import supply_cookies
## Not sure what equivalent to topics are, but may use same format?
#from topic_handler import UpdateTopicDict, ListTopics
## Will definitely adapt this:
from saver import SaveArticle

s = requests.Session()
#s.cookies = supply_cookies()

# Alternatively, consider extracting topics, tickers, article text etc.
# NB article text contains HTML entities that need to be parsed to Unicode
# for purposes of matching/storage etc. (e.g. &amp; => ampersand symbol)
def GetMktNewsPage(session, url):
    page = session.get(url)
    soup = bs(page.text, "lxml")
    # TODO: double check this line retrieves <div id="fullcontainer">
    article = soup.find('div', attrs = {'id':'fullcontainer'})
    # save article to content/{DATE}/{ID}.html:
    SaveArticle(article, url)
    # extract topics and check if they need to be added to the dictionary
    # UpdateTopicDict(ListTopics(article))
    return article

# TODO:
# - get topics and store them under `spin⠶e⠶x⠶lse/n/t`
# - probably not for this: begin to populate a graph database with these topics
# - match the company ticker to the list in exchanges directory
# - make an incoming feed directory and set up infra for running this as a pipeline on all new stories
# - put project on GitHub after removing anything sensitive - done
# - make a changelog and 'predict' against this using the market data
# - (presumably lots of other uses and interesting avenues will become clear upon browsing the results)
