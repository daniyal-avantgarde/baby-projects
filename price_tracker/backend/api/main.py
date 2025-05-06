""" 
Monitor the price of one or more products on e-commerce sites (like Amazon, eBay, or others), check periodically for updates, and alert the user when a price drops below a certain threshold.

1. Input
User provides:
Product URL(s)
Target price
Email address (optional for alerts)
2. Scraping
Send HTTP request to the product page
Parse the HTML to extract the current price
(Optional) Extract other info like product name, availability, or rating
3. Data Processing
Clean and convert the scraped price into a usable number
Compare it to the user’s target price
4. Notification Logic
If current price ≤ target price:
Send an email alert or display a console message
Log this event
Else:
Wait and check again later
5. Storage
Maintain a record (e.g., CSV, SQLite) of:
Previous prices
Timestamps
Status (price met or not)
6. Scheduling
Run checks periodically:
Using schedule, time.sleep(), or cron jobs

Optional Features
Multi-site support: Abstract scraper logic so you can support multiple stores
User interface: Build a basic command-line interface or simple web dashboard (Flask)
Browser automation: Use Selenium if sites block regular scraping or render data via JavaScript
Price history charting: Store prices and show graphs over time (with matplotlib or plotly)
"""

""" 
Price tracker program

This program is for when I want to buy something at the cheapest price. I'd probably want a chart of the product's price over the last month/year, to know the minimum price the product has gone for. Alternatively I should be able to fix a minimum price - I will not pay more than this for this, regardless of how stupid my proposed price is and whether the market will ever actually offer the product at that price. The program should also show me the current going price for the product i.e., current market valuation. 

We can summarise all this information into
- a price over time chart 
- a current market valuation number
- a buying price number, which the user can alter

So the program will:
1. Get which product and which buying price from user input
2. Scrape product price from website(s)
3. Display information summary (chart and two numbers)
4. Periodically re-scrape and update information
"""

