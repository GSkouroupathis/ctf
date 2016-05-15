#
# George Skouroupathis
# tags: wikipedia, scrapping, history
#
#
# Searches the history of the 'Flag' page
# in Wikipedia for the word 'CTF'
#
import urllib2
import re

noOfLoops = 15000
keyword = "ctf"
pagesWithKeyword = {}
keywordRegex = re.compile('[\s\d\D]*' + keyword + '[\s\d\D]*', re.IGNORECASE)

lastPage = "https://en.wikipedia.org/w/index.php?title=Flag&oldid=718031133"

for i in range(noOfLoops):
    print i,
    response = urllib2.urlopen(lastPage)
    htmlSource = response.read()

    # Find keyword
    if keywordRegex.match(htmlSource):
        print 'V',
        print lastPage


        keywordFinderRegex = re.compile(r'(' + keyword + r'[\s\d\D]*?)\n', re.IGNORECASE)
        keywordFound = re.findall(keywordFinderRegex, htmlSource)[0]
        print keywordFound
        pagesWithKeyword[lastPage] = keywordFound

    else:
        print 'X',
        print lastPage

    # Get previous pages
    previousLinkID = re.findall(r'<a href="/w/index\.php\?title=Flag&amp;direction=prev&amp;oldid=(\d+)', htmlSource)[0]
    lastPage = 'https://en.wikipedia.org/w/index.php?title=Flag&direction=prev&oldid=' + previousLinkID

for page in pagesWithKeyword:
    print page
