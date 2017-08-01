# from .models import Map, Logo, MapHasLogo, MapHasTags, Tag
# # from django.core import serializers
# # from rest_framework import serializers
# from serializers import TagSerializer
# from django.forms.models import model_to_dict
import sqlite3
import requests
import TextSummaryEngine
import itertools
import operator



def most_common(L):
  # get an iterable of (item, iterable) pairs
  SL = sorted((x, i) for i, x in enumerate(L))
  # print 'SL:', SL
  groups = itertools.groupby(SL, key=operator.itemgetter(0))
  # auxiliary function to get "quality" for an item
  def _auxfun(g):
    item, iterable = g
    count = 0
    min_index = len(L)
    for _, where in iterable:
      count += 1
      min_index = min(min_index, where)
    # print 'item %r, count %r, minind %r' % (item, count, min_index)
    return count, -min_index
  # pick the highest-count/earliest item
  return max(groups, key=_auxfun)[0]


def getMapFromLogo(logo):
    conn = sqlite3.connect('/Users/Hallshit/Documents/KnowledgeVC/AppBackend/RESTAPI/db.sqlite3')
    c = conn.cursor()

    conn.text_factory = str

    c.execute("SELECT * FROM APIapp_logo WHERE company LIKE (?)", [logo])
    print c.fetchall()
    c.execute(
        "SELECT name FROM APIapp_map WHERE APIapp_map.id IN (SELECT mapID_id FROM APIapp_maphaslogo WHERE logoID_id IN (SELECT id FROM APIapp_logo WHERE APIapp_logo.company LIKE (?)))",
        ['%'+logo+'%'])
    try:
        print c.fetchone()[0]
        mmap = c.fetchone()[0]

    except:
        mmap = getEntititesFromHomepageAndMatch(logo, c)
    return mmap

def getMapWithTag(tag,c):
    c.execute("SELECT name FROM APIapp_map WHERE id IN (SELECT mapID_id FROM APIapp_maphastags WHERE TagID_id IN (SELECT id FROM APIapp_tag WHERE APIapp_tag.name LIKE (?)))", ['%'+tag+'%'])
    return c.fetchall()


def getEntititesFromHomepageAndMatch(company,c):
    # url = "https://autocomplete.clearbit.com/v1/companies/suggest?query={}".format(company)
    # req = requests.get(url)
    # domain = req.json()[0]['domain']


    text = TextSummaryEngine.getTextFromURL(company)
    print text
    sent, ent = TextSummaryEngine.analyzeText(text)

    mmaps = []

    for e in ent[:20]:
        try:
            mmap = getMapWithTag(e.name, c)
            for m in mmap:
                mmaps.append(m)

        except:
            print "tag not found"


    # print mmaps

    topMatch = most_common(mmaps)[0]
    return topMatch


# getEntititesFromHomepage('clarifai')





