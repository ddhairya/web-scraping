__author__= 'dhairya'
import requests
from bs4 import BeautifulSoup

# Taking the input from the users for the product he is looking for in the flipkart.
keyword = input("what would you like to look for? - ")
# Building the url based on the user input
uri = "https://www.flipkart.com/search?q="+keyword+"&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
# Using the library requests for getting the content of the site page
request = requests.get(uri)
content = request.content

# the content of the site is so ugly for our programing language :) that we are using Beautifulsoup4 to make it prettier by telling it's HTML.
soup = BeautifulSoup(content, "html.parser")
# using the inspect element from browser, getting the information for the item HTML tags.
# <div class="_1vC4OE _2rQ-NK">₹18,990</div>
# <div class="_3wU53n">Acer Aspire 3 Pentium Quad Core - (4 GB/500 GB HDD/Windows 10 Home) A315-33 Laptop</div>
# mentioning the particular tag class to get the only element instead of whole page
price_element = soup.find_all("div", {"class": "_1vC4OE _2rQ-NK"})
item_element = soup.find_all("div", {"class": "_3wU53n"})

for tag1, tag2 in zip(item_element, price_element):
    # form the tag we are just retrieving the value by .text
    print(tag1.text + " --- " + tag2.text)
