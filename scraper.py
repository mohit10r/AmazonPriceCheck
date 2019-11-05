import requests
from bs4 import BeautifulSoup
import smtplib

url = 'https://www.amazon.in/gp/product/B07HGKGDHH/ref=s9_acss_bw_cg_Top_3a1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-7&pf_rd_r=0HJVKG2P8Q87ANHSYZXJ&pf_rd_t=101&pf_rd_p=e088eae1-596e-4f43-9537-98258ba91274&pf_rd_i=19698998031'

headers = {
    "User-Agent" : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/77.0.3865.90 Chrome/77.0.3865.90 Safari/537.36'
}

def check_price():
    page = requests.get(url,headers=headers)

    soup = BeautifulSoup(page.content,'html.parser')
    #print(soup)

    title = soup.find(id='productTitle').get_text()

    print(title.strip())

    price = soup.find(id='priceblock_ourprice').get_text()
    converted_price = price[2:8]
    converted_price = converted_price.replace(',','')
    float_price = float(converted_price)
    print(price)
    print(converted_price)

    if(float_price < 60000):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('mohitranjan28@gmail.com','anrzgtvxgafpaisy')
    subject = 'Price Fell Down!!!'
    body = 'Check the link https://www.amazon.in/gp/product/B07HGKGDHH/ref=s9_acss_bw_cg_Top_3a1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-7&pf_rd_r=0HJVKG2P8Q87ANHSYZXJ&pf_rd_t=101&pf_rd_p=e088eae1-596e-4f43-9537-98258ba91274&pf_rd_i=19698998031'

    msg = f"Subject : {subject}\n\n{body}"

    server.sendmail(
        'mohitranjan28@gmail.com',
        'mohit10r@yahoo.com',
        msg
    )
    print("Hry!!, Email has been sent!!")
    server.quit()

check_price()