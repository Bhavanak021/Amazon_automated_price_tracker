from bs4 import BeautifulSoup
import lxml
import requests
import smtplib


URL= "https://www.amazon.com/American-Tourister-Backpacks-Gradation-Centimeters-25/dp/B086HKYX91/ref=sr_1_4?dchild=1&keywords=school+bags+american+tourister&qid=1621564901&sr=8-4"
User_Agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
Accept_Language = "en-US,en;q=0.9,hi-IN;q=0.8,hi;q=0.7,kn;q=0.6"

my_email = ""
password = ""

headers = {
    "User-Agent": User_Agent,
    "Accept-Language": Accept_Language
}

response = requests.get(URL, headers=headers)
raw_html = response.text

soup = BeautifulSoup(raw_html, "lxml")
# print(soup.prettify())

usd = float(soup.find(name="span", class_="a-size-medium a-color-price priceBlockBuyingPriceString").getText().split('$')[1])
inr = usd*73
print(inr)

if inr < 1000:
    # print("yuhuu ho gya")
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="",
            msg=f"Subject:Amazon lowest price\n\n hey! We have got lowest for bag INR {inr}. Go buy it now."
        )