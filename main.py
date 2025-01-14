import requests
from bs4 import BeautifulSoup
import os


desired_price = 1000
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0",
          "Accept-Language": "en-GB,en;q=0.6"
          }

response = requests.get(url="https://www.amazon.in/Spigen-Hybrid-Compatible-Galaxy-Carbonate/dp/B0CM4NM2DN/ref=sr_1_4?nsdOptOutParam=true&sr=8-4", headers=header)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
try: 
    current_price = int(soup.select_one(".a-price-whole").getText().split(".")[0].replace(",",""))
    product_name = soup.select_one("#productTitle").getText().strip()
except :
    current_price = 2000
    print("Amazon Blocked request")
    print(response.text)

if current_price<desired_price:
    print("price alert sequence activated")
    import smtplib
    my_email = "sidr272002@gmail.com"
    my_password = os.environ["my_password"]

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        print("sending email")
        connection.sendmail(from_addr=my_email, to_addrs="sidharthr333@gmail.com", msg=f"Subject:Price Drop Alert!\n\nBuy your {product_name} now at just {current_price}")
        print("email sent")

