import requests
from bs4 import BeautifulSoup
import random

def scrape_wiki_article(url, counter, iterations):

	if counter == iterations:
		return
	
	response = requests.get(url)
	
	soup = BeautifulSoup(response.content, 'html.parser')

	title = soup.find(id="firstHeading")
	print(title.text + ": " + url)

	allLinks = soup.find(id="bodyContent").find_all("a")
	random.shuffle(allLinks)
	linkToScrape = 0

	for link in allLinks:
		# We are only interested in other wiki articles
		if link['href'].find("/wiki/") == -1: 
			continue

		# Use this link to scrape
		linkToScrape = link
		break
	
	counter += 1
	scrape_wiki_article("https://en.wikipedia.org" + linkToScrape['href'], counter, iterations)

scrape_wiki_article("https://en.wikipedia.org/wiki/Web_scraping", counter=0, iterations=5)