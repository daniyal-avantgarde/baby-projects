# input website url
# access website content (web scraping)
# find emails and collect in list (pattern matching)
# print list to csv (writing files)

import sys, webbrowser, requests, bs4, re

# INPUT WEBSITE URL
url = sys.argv[1]

# ACCESS WEBSITE CONTENT
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
} # apparently, have to use headers to avoid bot-detection
# what are headers?
response = requests.get(url, headers=headers) # downloads site content
response.raise_for_status() # does nothing if all well, raises error if otherwise
# print(f'TYPE: {type(page)}; LENGTH: {len(page.text)}')
# page.text is the raw website html

html = bs4.BeautifulSoup(response.text)

# FIND EMAILS AND COLLECT IN LIST
print(html.prettify)
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
emails = re.findall(email_pattern, html.prettify())
print(emails)

# get rid of duplicate emails


# webbrowser.open(url)

# fixed variable names
# using .text on the BeautifulSoup object returns only the visible text on the website
# you have to use .prettify() to get back the HTML, formatted for readability


