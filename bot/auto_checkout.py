import time
import requests
import sys
from bot.get_params import get_params
from bs4 import BeautifulSoup as bs

def add_to_cart(session, item_id, size_id, style_id, check):
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/80.0.3987.95 Mobile/15E148 Safari/604.1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "DNT": "1",
        "Connection": "close",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "TE": "Trailers"
    }

    data = {
        "size" : size_id,
        "style": style_id,
        "qty"  : "1",
        "chk"  : check,
        "authenticity_token" : getCSRF()
    }

    auto_checkout_url = f"https://www.supremenewyork.com/shop/{item_id}/atc.json"

    payload = {
        "name":"Aidan Salsadoun",
        "email":"bluerewind1@protonmail.com",
        "address":"4 AboveAShop",
        "address1":"",
        "country":"GB",
        "tel":"07508226496",
        "city":"Sunderland",
        "zip":"SR5 1JE",
        "cardtype":"visa",
        "cardnumber":"4929000000006",
        "exp_month":"04",
        "exp_year":"2023",
        "cvv":"123"
    }

    auto_response = session.post(auto_checkout_url, headers=headers, data=data)
    print("[+] Added to cart")
    if auto_response.status_code == 200:
        send_checkout_request(session, payload, headers)

def getCSRF():
    response = requests.get("https://www.supremenewyork.com/shop")
    htmlSoup = bs(response.text, 'html.parser')
    script   = htmlSoup.find('meta', {'name':'csrf-token'})
    formKey  = script.get('content')
    return formKey

def make_checkout_request(session, profile, headers):
    print("[+] Navigating to checkout page")
    checkout_page_content = session.get("https://www.supremenewyork.com/mobile/#checkout", headers=headers).text
    cookie_sub = session.cookies.get_dict()["hnkdtrace"]
    checkout_params = get_params(checkout_page_content, profile, cookie_sub)
    if not checkout_params:
        sys.exit("Error with parsing checkout parameters")
    return checkout_params

def send_checkout_request(session, profile, headers):
    checkout_url = "https://www.supremenewyork.com/checkout.json"
    checkout_params = make_checkout_request(session, profile, headers)
    #checkout_request = session.post(checkout_url, headers=headers, data=checkout_params)
    print("[+] Sent checkout request")
    print(time.perf_counter())
    #if checkout_request.status_code == 200:
    #    print("[+] Success!")
    #    display_order_status(session, checkout_request)
    #else:
    #    print("[+] Failed to checkout, restart the job", "red")

def get_order_status(session, slug):
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/80.0.3987.95 Mobile/15E148 Safari/604.1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "DNT": "1",
        "Connection": "close",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "TE": "Trailers"
    }
    stauts_url = f"https://supremenewyork.com/checkout/{slug}/status.json"
    status_content = session.get(stauts_url, headers=headers).json()
    status = status_content["status"]
    return status

def display_order_status(session, checkout_request):
    checkout_request.text
    print(checkout_request.text)
    #checkout_response = checkout_request.json()

    #status = checkout_response["slug"]
    #while True:
    #    status = get_order_status(session, status)

    #    if status == "queued":
    #        print("ORDER QUEUED")
    #    elif status == "paid":
    #        print("SUCCESS, CHECK EMAIL")
    #    else:
    #        print("ORDER FAILED")



