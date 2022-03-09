import json

def inject_data(): #This will for the moment run every task on every profile NEEDS TO BE CHANGED
    file = open("./data/profile.json")
    profiles = json.load(file)
    for profile in profiles["profiles"]:
        return profile
    file.close()

def inject_header():
    header = {
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
    return header

def inject_proxies():
    proxies = {
        'http': 'http://188.138.106.158:5566',
        #'https': 'https://85.25.99.106:5566',
    }
    return proxies