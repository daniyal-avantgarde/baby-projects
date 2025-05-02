# Website Email Scraper

This project is a simple email scraping tool that takes a website URL as input and extracts all email addresses found within the page's HTML. The extracted emails are saved to a text file for easy access. The script works on sites where emails are directly embedded in the HTML, but does not support sites that rely on JavaScript to render content.

- Accepts a website URL as input from the command line
- Scrapes HTML content of the webpage
- Uses regular expressions to identify email addresses
- Outputs a list of emails to a `.txt` file

### Dependencies and Requirements
- Python 3.x
- `requests` library
- `re` and `sys` (built-in Python libraries)

### Installation and Usage
1. Clone this repository
```bash
git clone https://github.com/daniyal-avantgarde/website-email-scraper.git
```
2. Install the required dependencies
```bash
pip install requests
```
3. Run the script using a website URL as a command line argument
```bash
python email_scraper.py https://example.com
```

### Limitations
- This script only works on websites where emails are directly embedded in the HTML.
- It does not handle JavaScript-rendered content (such as content dynamically loaded via JavaScript after the initial page load).
- Emails that appear in images or non-standard formats are not captured.

### Future Improvements
- Extend the scraper to handle JavaScript-rendered HTML by using tools like Selenium or Puppeteer.
- Refine the email regex pattern to handle more edge cases and email formats.
- Add additional output formats (e.g., CSV).

### What I learnt
- Basic `requests` library functionality
    - response = requests.get(url)
    - html = response.text
- Basics of using git and Github
- Interesting caveats about web-scraping
    - Websites will use sneaky tactics to stump scraper bots, like using JS to inject the HTML. It reminds me of biological micro-organism warfare
    - HTTP stands for HyperText Transfer Protocol. It's a set of rules that devices obey when trying to connect to each other.
    - One of those rules is a device trying to connect to a website must provide a 'header'.
    - A 'header' is like a name-tag your device sends to the host device. The website uses your header to identify you.
    
        Using `requests.get(url)` without including a header will likely get your request to connect flagged as a bot, and you'll be shut out. To avoid that, we cleverly set a custom header to disguise ourselves as a real device:

        ```python
        headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
        } 
        response = requests.get(url, headers=headers) 
        ```

        Advanced checks will still see through this and shut you out, but it's better than nothing!