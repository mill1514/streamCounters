import webbrowser
import bs4
import urllib.request

myPNum = 600390025

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

        return str(td_node_list[5].contents[0])

ret = scrapeRank(myPNum)

print("\n\nRESULT:" + ret)