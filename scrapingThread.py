import counterUtils as cu

import urllib.request
import time
import bs4

sRank = True
sNPlaying = True
myPnum=600458471 # profile number from wiimmfi.de

# scrapes for current rank of profile number specified by pNum. Returns -1 if something failed.
def scrapeRank(pNum):
# Get website html + parse
	r = urllib.request.urlopen("https://wiimmfi.de/mkw/room/p" + str(pNum))
	html = r.read().decode()
	soup = bs4.BeautifulSoup(html, "html.parser")

	try:
		t_node = soup.find_all(attrs={"class": "tr2"})[1]
	except IndexError:
		return -1 # User is not online

	td_node_list = t_node.find_all_next("td")

	try:
		return int(td_node_list[5].contents[0])
	except:
		print("Ayy")

	return -1

# scrapes for number of people playing mkwii online. Returns -1 if something failed.
def scrapeNPlaying():

    # Get website html
	r = urllib.request.urlopen('https://wiimmfi.de/game')
	html = r.read()

    # Extract number from file
	try:
		nPlaying = int(html.decode().split("<a href=\"/game/mariokartwii\">")[2].split("<")[0])
	except:
		nPlaying = -1

	return nPlaying


def scrapingThread():

	while(True):

		if cu.getDicVal("kill") is not None:
			return

		if sRank:
			rank = scrapeRank(myPnum)
			if rank > 0:
				cu.updateValue("curr", rank, printOpt=False)

		time.sleep(10)

		if sNPlaying:
			nPlaying = scrapeNPlaying()
			if nPlaying > 0:
				cu.updateValue("nPlaying", nPlaying, printOpt=False)
		
		time.sleep(10)