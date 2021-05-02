import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.johnlewis.com/john-lewis-partners-isaac-ergonomic-office-chair-black/p3575108")
content = request.content
soup = BeautifulSoup(content,"html.parser")
element = soup.find("p", {"class":"price price--large"})
# <p class="price price--large">£279.00</p>
string_price=element.text
price_without_symbol = string_price[1:]
price=float(price_without_symbol)

if price < 200:
    print("you should buy the chair")
    print("The current price of the chair is {}".format(string_price))

else:
    print("dont buy it is too expensive")
