"""
Pass a website url to this program via the command line and
it will scrape all the emails from that website.

The program executes these steps:
1. Accepts website url as command line input 
2. Accesses url and scrapes HTML
3. Using regex, finds all emails in HTML and stores as them in a list 
4. Prints the list of emails to a text file (.txt)
"""

# STEP 1: INPUT WEBSITE URL #
import sys
url = sys.argv[1]

# STEP 2: ACCESS WEBSITE CONTENT #
import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
} 
response = requests.get(url, headers=headers) 
response.raise_for_status()
html = response.text

# STEP 3: FIND EMAILS AND COLLECT IN LIST #
import re
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
emails = re.findall(email_pattern, html)
emails = list(dict.fromkeys(emails))
emails = [email for email in emails if not (email[-3:]=="png" or email[-3:]=="jpg")]

# STEP 4: PRINT LIST TO FILE #
outputFile = open('output.txt', "w", newline='')
for email in emails:
    outputFile.write(email + '\n')



# fixed variable names
# using .text on the BeautifulSoup object returns only the visible text on the website
# you have to use .prettify() to get back the HTML, formatted for readability

# not going to export to csv because... there's no reason to.
# a text file will work just as well. i have no cells.
# i only have one email per line

# picking up weirdly named images like 12-2019_about-ig_women-at-sprout@2x.jpg so have to update regex expression to exclude those

# apparently, have to use headers to avoid bot-detection
# what are headers?

""" 
notes 
response = requests.get(url, headers=headers) # downloads site content
response.raise_for_status() # does nothing if all well, raises error if otherwise"""

'''count = 1
for email in emails:
    print(f'Email {count}: {email}')
    count += 1'''



