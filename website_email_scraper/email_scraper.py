# input website url
# access website content (web scraping)
# find emails and collect in list (pattern matching)
# print list to csv (writing files)

import sys, webbrowser, requests, bs4

url = sys.argv[1]

wikipedia_page = requests.get(url) # downloads site content
wikipedia_page.raise_for_status() # does nothing if all well, raises error if otherwise
print(f'TYPE: {type(wikipedia_page)}; LENGTH: {len(wikipedia_page.text)}')
# download_site.text is the raw website html

wikipedia_soup = bs4.BeautifulSoup(wikipedia_page.text)

search_bar = wikipedia_soup.select('div.search-container')[0]
print(search_bar.attrs)
print(search_bar.get('class'))


webbrowser.open(url)


