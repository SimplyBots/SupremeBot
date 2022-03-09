from bot.auto_checkout import add_to_cart
from colorama import init, Fore
import time
import requests

GLOBAL_IN_STOCK_SIZE = "N/A"
GLOBAL_IN_STOCK_SIZE_ID = "84396"
GLOBAL_IN_STOCK_COLOUR = "Purple"
GLOBAL_IN_STOCK_NAME = "Supreme®/Nalgene® Characters 32 oz. Bottle"
GLOBAL_IN_STOCK_CATEGORY = "Accessories"

GLOBAL_OOS_SIZE = "US 9 / UK 8"
GLOBAL_OOS_COLOUR = "Black"
GLOBAL_OOS_ITEM = "Supreme®/Nike® SB Dunk High"
GLOBAL_OOS_CATEGORY = "Shoes"

def get_stock():
    init()
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
    proxies = {
        'http': 'http://188.138.106.158:5566',
        #'https': 'https://85.25.99.106:5566',
    }
    url = "https://www.supremenewyork.com/mobile_stock.json"
    session = requests.Session()
    response = requests.get(url, headers=headers, proxies=proxies)
    all_products = response.json()
    get_item_id(session, all_products, headers)
 
def get_item_id(session, all_products, headers):
    for product in all_products["products_and_categories"][GLOBAL_IN_STOCK_CATEGORY]:
        productName = product["name"]
        if(productName == GLOBAL_IN_STOCK_NAME):
            id = product["id"]
            check_stock(session, id, headers)
            time.sleep(1)
            return
        else:
            print(Fore.CYAN + "[+] Searching for item")
            
def check_stock(session, id, headers):
    print(Fore.YELLOW + "[+] Checking stock")
    item_url = f"https://www.supremenewyork.com/shop/{id}.json"
    response = session.get(item_url, headers=headers)
    item_variant = response.json()
    
    colours = item_variant["styles"]
    for colour in colours:
        style_id = colour["id"]
        chk = colour["chk"]
        productColour = colour["name"]

        # Checks for the product colour
        if(productColour == GLOBAL_IN_STOCK_COLOUR):
            item_inventory = colour["sizes"]
            for product_details in item_inventory:
                size = product_details["name"]
                stock = product_details["stock_level"]
                if(size == GLOBAL_IN_STOCK_SIZE):
                    if(stock > 0):
                        print(Fore.GREEN + "[+] Found requested item with parameters given")
                        add_to_cart(session, id, GLOBAL_IN_STOCK_SIZE_ID, style_id, chk)
                        return
                    else:
                        print(Fore.RED + "[+] Out of stock")
                        time.sleep(1.5)
                        check_stock(session, id, headers)
            return
        else:
            print(Fore.RED + "No colour found please try a different colour")
