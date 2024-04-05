import requests
from bs4 import BeautifulSoup
import smtplib
import os

URL = 'https://www.amazon.com/-/es/dp/B06XVY9VBY/?coliid=INZEMZ89A4DJU&colid=3QVTYCG5BBLS7&psc=1&ref_=list_c_wl_lv_ov_lig_dp_it'

headers = {
    "User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36', 
    "Accept-Language" : 'en-US,en;q=0.9,es-US;q=0.8,es;q=0.7',
}

response = requests.get(url=URL, headers=headers)
page = response.text

soup = BeautifulSoup(page, 'html.parser')
# print(soup)

price = float(soup.find(name='span', class_= 'aok-offscreen').getText().split('$')[1])
product = soup.find(name='span', id= 'productTitle',class_= 'a-size-large product-title-word-break').getText().strip()
# print(product)

if price < 32 :
    my_email = 'unitedoutofcontext@gmail.com'
    password = os.environ.get('PASSWORD_UNITED') 
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        body = (f'{product} is now ${price}\n{URL}')
        connection.starttls() #make the conection secure
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs='jaimevillalbaoyola@gmail.com',
                            msg= (f'Subject: Amazon Price Alert !!!\n\n {body}').encode("utf-8"),
                            )
       