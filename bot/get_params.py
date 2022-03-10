import re
from bs4 import BeautifulSoup as bs

def sanitize_value(value):
    regex = re.compile('[^a-zA-Z]')
    return regex.sub("", value).lower().strip()


def parse_input_fields(input_fields):
    custom_values = []
    default_values = []

    for field in input_fields:
        if field.get("value") is not None:
            custom_values.append(field)
        elif field.get("name") is not None:
            default_values.append(field)
    return custom_values, default_values


def assign_custom_values(checkout_data, profile_data, custom_values):
    for value in custom_values:
        checkout_data[value["name"]] = value["value"]
        checkout_data["credit_card[type]"] = profile_data["cardtype"]
        #if checkout_data[value["name"]] == "credit card":
        #   checkout_data[value["name"]] = profile_data["cardtype"]

        if not value["value"]:
            placeholder = value.get("placeholder")
            if placeholder is None:
                checkout_data[value["name"]] = value["value"]
                continue

            placeholder = sanitize_value(placeholder)
            value_name = value["name"]
            if "cvv" in placeholder:
                checkout_data[value_name] = profile_data["cvv"]
            elif "creditcardnumber" in placeholder or "credit" in placeholder:
                checkout_data[value_name] = profile_data["cardnumber"]

    return checkout_data


def get_default_values(checkout_data, profile_data, default_values, cookie_sub):
    for default_value in default_values:
        placeholder = default_value.get("placeholder")
        name = default_value.get("name")

        if placeholder is None or name is None: # only do following operations of placeholder and name are not None
            if name is not None and("cookie" in name or "sub" in name):
                checkout_data[default_value["name"]] = cookie_sub
            continue

        placeholder = sanitize_value(placeholder)
        name        = sanitize_value(name)
        if placeholder == "name" or "name" in default_value["name"]:
            if default_value.get("name") not in checkout_data:
                if default_value.get("style") is None:
                    checkout_data[default_value["name"]] = profile_data["name"]
                else:
                    checkout_data[default_value["name"]] = ""

        elif placeholder == "email" or placeholder == "e-mail" or "email" in name or "e-mail" in name:
            checkout_data[default_value["name"]] = profile_data["email"]

        elif placeholder == "telephone" or placeholder == "tel" or "tel" in name:
            checkout_data[default_value["name"]] = profile_data["tel"]

        elif placeholder == "address" or placeholder == "billing address" or placeholder == "addr":
            checkout_data[default_value["name"]] = profile_data["address"]

        elif "postcode" in placeholder:
            checkout_data[default_value["name"]] = profile_data["zip"]

        elif placeholder == "city" or "city" in name:
            checkout_data[default_value["name"]] = profile_data["city"]

    return checkout_data


def get_select_field_values(checkout_data, profile_data, select_fields):

    for select_field in select_fields:
        element_id = select_field.get("id")
        name = select_field.get("name")
        if select_field is None or name is None:
            continue

        element_id = sanitize_value(element_id)
        name = sanitize_value(name)

        if "orderbillingcountry" in name or "country" in element_id:
            checkout_data[select_field["name"]] = profile_data["country"]

        elif "creditcardmonth" in name or "month" in element_id:
            checkout_data[select_field["name"]] = profile_data["exp_month"]

        elif "creditcardyear" in name or "year" in element_id:
            checkout_data[select_field["name"]] = profile_data["exp_year"]

    return checkout_data


def check_data(checkout_data, profile_data):
    for key in profile_data:
        if key != "id" and key != "profile_name":
            if profile_data[key] not in checkout_data.values():
                return False
    return True


def get_params(page_content, order_no_content, profile_data, cookie_sub, url):
    #Finds the script
    checkout_data = {}
    scriptSoup = bs(page_content, "html.parser")
    checkoutScript = scriptSoup.find("script", id="checkoutViewTemplate")
    checkoutHTML = checkoutScript.text

    # Finds the right form
    formSoup = bs(checkoutHTML, "html.parser")
    
    # Finds all input fields
    input_fields = formSoup.find_all('input')
    select_fields = formSoup.find_all('select')
    custom_values, default_values = parse_input_fields(input_fields)

    soup = bs(order_no_content, "html.parser")
    order_no = soup.find_all("input", id="cardinal_order_no")
    for number in order_no:
        profile_data["cardinal_order_no"] = number["value"]
        checkout_data[number["name"]] = profile_data["cardinal_order_no"]

    # Assigns all values like credit card, billing etc
    checkout_data = assign_custom_values(checkout_data, profile_data, custom_values)
    checkout_data = get_default_values(checkout_data, profile_data, default_values, cookie_sub)
    checkout_data = get_select_field_values(checkout_data, profile_data, select_fields)

    checkout_data["hpcvv"] = ""
    checkout_data["h-captcha-response"] = "" 

    if check_data(checkout_data, profile_data):
        return checkout_data