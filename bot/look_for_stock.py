from bot.profileLoader import inject_header, inject_proxies
from bot.auto_checkout import add_to_cart
from colorama import init, Fore
import requests
import time

def get_stock(item_category, item_name, item_colour, item_size):
    init()

    url = "https://www.supremenewyork.com/mobile_stock.json"
    session = requests.Session()
    response = requests.get(url, headers=inject_header(), proxies=inject_proxies())
    all_products = response.json()

    # Gets the item id
    for product in all_products["products_and_categories"][item_category]:
        if(product["name"] == item_name):
            id = product["id"]
            check_stock(session, id, inject_header(), item_colour, item_size)
    
            
def check_stock(session, id, headers, item_colour, item_size):
    print(Fore.YELLOW + "[+] Item found! Checking stock")
    item_url = f"https://www.supremenewyork.com/shop/{id}.json"
    response = session.get(item_url, headers=headers)
    item_variant = response.json()

    colours = item_variant["styles"]
    for colour in colours:
        style_id       = colour["id"]
        check          = colour["chk"]
        product_colour = colour["name"]

        # Checks for the product colour
        if(product_colour == item_colour):
            item_inventory = colour["sizes"]
            for product_details in item_inventory:
                product_size = product_details["name"]
                stock        = product_details["stock_level"]
                product_id   = product_details["id"]
                if(product_size == item_size):
                    if(stock > 0):
                        print(Fore.GREEN + "[+] Item in stock")
                        add_to_cart(session, id, product_id, style_id, check)
                        return
                    else:
                        print(Fore.RED + "[+] Out of stock")
                        time.sleep(1.5)
                        check_stock(session, id, headers)
            return
        else:
            print(Fore.RED + "No colour found please try a different colour")
