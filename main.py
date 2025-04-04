import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

header={
    "Accept-Language":"en-US,en;q=0.9,kn;q=0.8",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",

         }
# "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
# "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
# "sec-ch-ua-mobile": "?0",
# "sec-ch-ua-platform": "Windows",

url="https://www.amazon.com/REDMAGIC-Smartphone-Snapdragon-Dual-Sim-Transparent/dp/B0CP7K5NJ9/ref=sr_1_1?crid=WPGCCLFHR81Y&currency=INR&dib=eyJ2IjoiMSJ9.M51gRC77FS6YOUqbK3gvhjjadb73njtB6ukjz5O9_7ZDpYGClhU1qiVrTQHdIUcI5XcjjubhKbWLyfFO6VfncA.sSuZvAl5gCPdS-nTUwtTFOt9WHHEp57oC0DBUUP6pP0&dib_tag=se&keywords=iqoo+12+pro+5g&qid=1718804485&sprefix=iqoo+12+proc%2Caps%2C514&sr=8-1"
response=requests.get(url=url,
                      headers=header)
website_html=response.content

soup = BeautifulSoup(website_html, "lxml")
# print(soup.prettify())
title = soup.find(id="productTitle").get_text().strip()
print(title)

# price_dec = soup.find("span", class_="a-price-whole")  # Locate the whole part of the price
price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)
price_as_inr=price_as_float*82
print(price_as_inr)

buy_price=90000

YOUR_PASSWORD="dzwe ixka hdat iwie"
YOUR_SMTP_ADDRESS="smtp.gmail.com"
YOUR_EMAIL="aftab10667@gmail.com"

if price_as_inr<buy_price:
    message = f"{title} is now {price}"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )

# price_element=price_as_float
# #
# #
# if price_element is not None:
#     # Extract and clean the price text
#     price_text = price_element.getText().strip()
#
#     # Remove the dollar sign and convert to float
#     price_usd = float(price_text.replace('$', '').replace(',', ''))
#
#     # Convert to Indian Rupees using an exchange rate (e.g., 1 USD = 82 INR)
#     exchange_rate = 82
#     price_inr = price_usd * exchange_rate
#
#     # Print the final price in USD and INR
#     print(f"Price in USD: ${price_usd:.2f}")
#     print(f"Price in INR: ₹{price_inr:.2f}")
# else:
#     print("Price information not found on the page.")
#
#
# # Check if elements are found before attempting to access their text
# # if price_dec is not None and price_frac is not None:
# #     # Print the whole and fractional parts
# #     print(price_dec.getText().strip())  # Print the whole part
# #     print(price_frac.getText().strip())  # Print the fractional part
# #
# #     # Clean and combine the whole and fractional parts to get the final price
# #     # Use .replace(',', '') to handle prices with thousands separators and strip to remove extra characters
# #     whole_part = price_dec.getText().replace(',', '').strip()
# #     fractional_part = price_frac.getText().strip()
# #
# #     # Convert to integers
# #     whole_part_int = int(whole_part)
# #     fractional_part_int = int(fractional_part)
# #
# #     # Combine the parts into the final price
# #     price = whole_part_int + (fractional_part_int / 100)
# #
# #     # Print the final price
# #     print(price)
# # else:
#     print("Price information not found on the page.")