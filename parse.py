
from bs4 import BeautifulSoup
import requests as req

def loadPage(username, year):
    resp = req.get("https://github.com/{0}?tab=overview&from={1}-01-01&to={1}-12-31".format(username, year))
    soup = BeautifulSoup(resp.text, 'lxml')
    return soup

#-------------------------------------------------------------------------------

def parseSimpleYear(username, year):
    resp = req.get("https://github.com/{0}?tab=overview&from={1}-01-01&to={1}-12-31".format(username, year))
    soup = BeautifulSoup(resp.text, 'lxml')

    #print("read page: \"{0}\" ({1})".format(soup.title.text, year))

    text = soup.find('h2', 'f4 text-normal mb-2').text.strip()
    text = text.replace(',','')
    commits = int(text.split()[0])
    return commits

#-------------------------------------------------------------------------------

dates = []
counts = []

def parseFullYear(username, year):
    resp = req.get("https://github.com/{0}?tab=overview&from={1}-01-01&to={1}-12-31".format(username, year))
    soup = BeautifulSoup(resp.text, 'lxml')

    for tag in soup.find_all("rect", "day"):
    	#print("Date: {0}, Count: {1}".format(tag["data-date"], tag["data-count"]))
    	dates.append(tag["data-date"])
    	counts.append(tag["data-count"])
