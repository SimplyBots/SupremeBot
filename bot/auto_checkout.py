import requests
import sys
from bot.get_params import get_params
from bs4 import BeautifulSoup as bs
from bot.profileLoader import inject_data, inject_header

def add_to_cart(session, item_id, size_id, style_id, check):

    data = {
        "size" : size_id,
        "style": style_id,
        "qty"  : "1",
        "chk"  : check,
        "authenticity_token" : getCSRF()
    }

    auto_checkout_url = f"https://www.supremenewyork.com/shop/{item_id}/atc.json"
    auto_response = session.post(auto_checkout_url, headers=inject_header(), data=data)
    if auto_response.status_code == 200: #Also wanna check if the content array within auto_response isnt empty
        print("[+] Added to cart")
        send_checkout_request(session, inject_data(), inject_header())

def getCSRF():
    response = requests.get("https://www.supremenewyork.com/shop")
    htmlSoup = bs(response.text, 'html.parser')
    script   = htmlSoup.find('meta', {'name':'csrf-token'})
    formKey  = script.get('content')
    return formKey

def make_checkout_request(session, profile, headers):
    print("[+] Navigating to checkout page")
    mainURL = "https://www.supremenewyork.com/mobile/#checkout"
    order_no_url = "https://www.supremenewyork.com/checkout"
    checkout_page_content = session.get(mainURL, headers=headers).text
    order_no = session.get(order_no_url, headers=headers).text
    cookie_sub = session.cookies.get_dict()["hnkdtrace"]
    checkout_params = get_params(checkout_page_content, order_no, profile, cookie_sub, session)
    if not checkout_params:
        sys.exit("Error with parsing checkout parameters")
    return checkout_params

def getCaptcha(session, header):
        v = "93a89cc"
        sitekey = "9c1f7658-2de8-43d2-abca-6660f344ea1c"
        formData = {
            "v": v,
            "sitekey": sitekey,
            "host": "www.supremenewyork.com",
            "hl": "en",
            "motionData": '{"st":1646905521604,"v":1,"topLevel":{"inv":true,"st":1646905499481,"sc":{"availWidth":1920,"availHeight":1040,"width":1920,"height":1080,"colorDepth":24,"pixelDepth":24,"availLeft":1920,"availTop":154},"nv":{"vendorSub":"","productSub":"20030107","vendor":"Google Inc.","maxTouchPoints":0,"userActivation":{},"doNotTrack":"1","geolocation":{},"connection":{},"pdfViewerEnabled":true,"webkitTemporaryStorage":{},"webkitPersistentStorage":{},"hardwareConcurrency":8,"cookieEnabled":true,"appCodeName":"Mozilla","appName":"Netscape","appVersion":"5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36","platform":"Win32","product":"Gecko","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36","language":"en-GB","languages":["en-GB","en-US","en"],"onLine":true,"webdriver":false,"scheduling":{},"bluetooth":{},"clipboard":{},"credentials":{},"keyboard":{},"managed":{},"mediaDevices":{},"storage":{},"serviceWorker":{},"wakeLock":{},"deviceMemory":8,"ink":{},"hid":{},"locks":{},"mediaCapabilities":{},"mediaSession":{},"permissions":{},"presentation":{},"serial":{},"virtualKeyboard":{},"usb":{},"xr":{},"userAgentData":{"brands":[{"brand":" Not A;Brand","version":"99"},{"brand":"Chromium","version":"99"},{"brand":"Google Chrome","version":"99"}],"mobile":false},"plugins":["internal-pdf-viewer","internal-pdf-viewer","internal-pdf-viewer","internal-pdf-viewer","internal-pdf-viewer"]},"dr":"https://www.supremenewyork.com/shop/accessories/ojwodz6f0/c3vq6ysdr","exec":true,"wn":[],"wn-mp":0,"xy":[],"xy-mp":0,"mm":[[0,419,1646905520020],[122,423,1646905520057],[173,424,1646905520073],[283,432,1646905520108],[338,436,1646905520127],[425,444,1646905520161],[471,452,1646905520177],[521,460,1646905520193],[571,467,1646905520209],[621,474,1646905520225],[671,480,1646905520241],[718,488,1646905520257],[760,495,1646905520273],[792,502,1646905520289],[819,511,1646905520305],[835,520,1646905520322],[847,531,1646905520338],[858,544,1646905520354],[868,556,1646905520370],[878,567,1646905520387],[887,576,1646905520403],[896,586,1646905520422],[902,592,1646905520440],[907,598,1646905520457],[914,603,1646905520473],[921,608,1646905520489],[929,612,1646905520507],[934,616,1646905520523],[939,619,1646905520541],[943,620,1646905520561],[947,623,1646905520581],[951,624,1646905520601],[954,624,1646905520627],[954,624,1646905521544]],"mm-mp":4.26890756302521,"md":[[954,624,1646905521544]],"md-mp":0,"mu":[[954,624,1646905521600]],"mu-mp":0},"session":[],"widgetList":["0cei8tl0relg"],"widgetId":"0cei8tl0relg","href":"https://www.supremenewyork.com/checkout","prev":{"escaped":false,"passed":true,"expiredChallenge":false,"expiredResponse":false}}',
            "rqdata": 'BhatpUVl88dSWNDQH9YI2hUtANap0kv/e4Aq+XdMNubqJ5UfGRMDmlWJm8b80JHXi8QAAtktnWv9gZM0Ka3U7ciNRN7qvqZsyRjfdFysuDC6lHbTIRyJVJASy6hE+uVEjO+btW2TA1Is5mtVlKzK6Kh2c6l0Ehns/t22hUjolx+nM2FeVl7ZSghwGByEz0qVSQDsiU/oJCO7iXoo+Ycy8X7urmT4VNRxurdCxbQk0oW6fCB1yqEMmbQ=IEJfnvP61aKuwLpp',
            "n": '6f8ebda1821df76f4b4d016b775a3eb944841721bd2e938b095e11a6928fc5f9a2a380be9b46611f1a66f25481866e24074cc48df419d6fff87d59093bc55cb26e7428fbb4312e97fa66c015333931d3dc47386e9159839afdf19873f52643a0fa678903477c33915f5256d9ab3a1b13bee6eab7f2ac1b5f7271b56e080594291c32c6214330118cbd6cf9062c069b740adb6b1acc29e130b30ffb164d0c9c5568f32f59183b12519b07025b3daea579e937ff70271788fd397632cd06659760817ef91a06bc70f2ef774f7a21ad635c9299eb58d1dda2c1c860d78ecb2784bf667a0142727e4b69ddb838e13875663d1adb8afc9007fb680ca8ae021a7fd3a11cf4e1b33cafbdf55c9670ea9a659a51eead6913fa378f4185686d93a7badf2ada8bef4b431faec272a23b252ca2497fcad1dcd2a87242dd7e9fdadc1a262b7a4893766a3fb44b26d7e9d0b5deb1853f8436c427b765df552aeb10d0cd28b54dd079db50a8430b19ce7c9f9f0146ac1af5caea91232d6e55a7f70c37efa422d7315ed022ee7d54e35e5f344830290d865bb6bb7a35e6d5f884422e2a70cfabb30387d02aeee7dfa70d2c0ac4fe9caa76035259eda6ec89b362af56faac1ea3c95aa1158f0642ebba86e3b43b18d06e5d10dd6a20d56a10437c42c9912c368dee61255b180fcda23fecbd835b618126b5ee6cb0035dbdbb610d7dbdba484c64aff8fbe81c72193c4a4ecf0a750c80c28528cb5ef451a5d7ec1f551963ccc479abf13c49457155a679b7c585841e39e31b9f44d3ffeb299bde5016372fad97c77627e8577b68e06acd764885e5298b5ae0bebad5a10ce01cb61d4d6f52bd4f27c4293e7a57e36e3f9824d8d3e46df12f6fd03c275ed6a3bbab7e7a1cefc43308228f7d6923cc0cda34367da88e1db6717ecf87e10f53396650c72bff0ee28a58a5901e366f50faa8a7b86d0efffece18e65c40c9d9ddd065f4e435890fac6f1b9afc78134316a29c640fe667a4b6d8b9b7c25dc735910b5fb93a0f3f69c261cf133720519c345462639f406406b6047adea93f609a7d1dfbd3b996682f0ce8108772db7c900488bdefdf489848f3867dbd8ca7a5d8700c49b2168df7f6cb209f4e76a71d2ea868f1d5b1742a819be7c6c7254861dd82628093092feae5c331364d55a3ac9be61de16d3f903644d513eeb9e27715f8cd8987bb50719b72915e98740fe9b10b596a9ab7072b6640185be3353b88e54f0959ed5caf5ab44f482f26368cf1065546cf25dfd2928245cb24735d3997c73580f4a3d4016e9e8b12340e21af2d1779e9ddbda4c5773721aca9f357553be9884d2c033e4ad149b75e4ac3a863201f49c65b1fe018ec59811b7397fa308508daa016307cbe6d01a761ba6b65491cb677ebae6ccdadc74cbbcec7a318239c54ca2828c54e908477072a02598e8fd5aed6cbed4c420dab4bf27ad3d7346bba399bb265cae95697b15d94ce5dd4cf031e7eadb28bdfa3ceef23162782bd2bd545d70f66aaee11eb29919df333ffff695e923edb95a66f3e7ecb3d549e80c4c4eff34dc5f3fb4ba269b4c0d20a30c90efb2b8e969644367ae78c6c9c0f90770fdf3a1bcc8a204730281224b518d7867c3563436dcb43d9f23bde9768f25fd27ab2caa89447101495a5820d5f12c2b3354e117c8beec1f4cbb11b919e3e62f95fb6e1875faf94f379c0adbfa4c37b933d7ed96c43b9cd976e2a0a718519043549cec3571d8c87919049d43d682f67d0b3ae08aee04462c3c36da0db6b9fc0f8baa6fdb6f30bb5228995933326563fd50cc51f077a2783e25064bf58c36e5b12f56a5b0b5bdab2d0204bde84da2f5b09d5a70212079d0e472af81d85e0d7adec8c473f4b2ec1dbd0ace48ed6b28cd8a02bb3bd243c5caa836a3f29809b534974bb49f5197194e09eddd6063600e7697333fdc083ef36643cfc93936b1cec833fe34f9b1d125976739b6d6f08788317a85c055047b7c1c3935134c5ffb4e82bb3369fb946e13070af580ce43ea8a8409a6719129b2011abc4f993a30b647b2a26fe3d57b6292f25c82dc5357474068e3363165b0f935a6281865c9c0cee712c975f62e7dc15009ede3391bf097f577c21daafe5ce11b66f563addeb40324a4018d559673a031a55fdab5198b58c864dc68abcd976f125e1943c0da7361e90e51aaaa26798231d1bc72f5566fb3f0e95f7e9e416a24868350abf736f51c909cf81982eb70068874b275f155f30fae6942b82d8eb6e9fee364f82bb6e1e29e83bdb2f1fb1c422428f6b195bcd2c52e6876505ccb0165587d3e2197199f9805051f647403911ab3c958bb272ef5c38afcf399a10230e06361ced5626356f8756fc2464ada1a79a941234723d5c60ce63a06bf575c8e1ffca25ee7867e2b6e5d4006639f966227a06eae34a33c52456f240c2f78f6670f44529ca95aa3e300a36d4612a9ee8f2061ac912031ad05e517fc43f25a2231e747a361ace97b9cfd775888a59d59dbc3160c18c46d5ee0ded60b1955d9695184502b267e082b3c7f3e60b9f5dd7069c2cc7d63ec8d608993206ee8a96edf0b0ed4bafe1fe8ce733232fe122b3ee42a0c482c066f2d8376551d216d4bf98afd1c30278cab511f2959cddc110c85e21c78eb145ae76fa661e978aa0b3cb94d4d6791cc05cec9d02ffe942c91c997a0efee5126236570b926982eeb42551ea1fa391e048cf7c6dc392b8e77d1702da4aba6af90b7e47779f1ecc39ac752df72c9f8b65931cad31534c3e3fc64f870e8ebec21ee21c9e241000be6f1958b1cef67ab8f07b044e3c2ee8870566ab55d8d60a56893ce456c89185f5dfc7ee72af97734cff81b82f3638905deb2977947629daf7a30bd9b7f5576f265c11d6751130a6fdd295dba1d56b393a5948a694ea6ce2404d3164fbdb4e49dc7bd051811df809dd7baaabb40fdfdf7f9ccd2ebc62db014e0225f2e78d65b527a39cf62dacccd46eb51d0cf32a47016ee7dd0ca6f0e29b06e36f23794c714c53072f2863cd517543d6afafcc6ba93e7871d36d7c67aa597c7a7a47cc831e990eff52ed20f3533d67fe2f60b4a53d62dcc7b809b81aa5b8fb96e8a446119dfb7c52234c407c582dc8bf8e039a513dec78105232877863f39390124957e9a50efcbc23849aed3a7d5379d98b7727844875589497bac0ae456d70931b5007d981b86aada33ea06130b5739b5a7d1275a295800918d97f6e2a24ca7f67f6fd7fcc216f7eb887041ca99242e8964fcae4accaa11a22c4f4bd16569f390c254b6d524cf752819ccf71e64ba2577f973e433193bef410ba62e2344630271007b96630dd9636e5c69d35c685a9b720955ccae29eb790a0b06c2d6067d956c8fe7f2295bec8ad49a26be4d249c0d6f212f8c51caefb45f6944610060a02786b169ed66eb6701b2f859c919ce307e372af14bdb2e0d621673d802f9e49e15d4480cb0a2f002a2ad2c5e449697feb4b803a90a540e7dadfa537d9c646c65e708fe2a2fa1c93cc10ae466584c0fc970c9ff9d6a31056219086e6ef3028c5e52bf27e2fbf0c1c4cf0a88aa09916a7668287bdec6b916401424ca6faaa5766f7ed4a8dc56145b3ceab15e5f4605eeb732f8ee3b4abc5d475fdfa871844c7ae5856e6b6eca6826e7eba83d64920d8106441693e5f77c6e1f077155cf3c6820686bb392344a8b60a3bcca9bbcfe835d5b9a57a23e9be31a9d29852b48a49476556d4a5d6bdb2da95315e80b2f3edfa5e21ebe216d78085696e5c30e41b31aa51a31950b5161eab5980f03b2b597672cc8902024c480d461b1834b8291fa43564a17f449bded613cbc6eaa4fe8a4b2208bfcc35be459a139652518f902caf15c77e8c2b104b3c739c4e19ceb16e4e7efe7e94955f60ac4dcbe3170620216948f4bea1a46f2a6ac700',
            "c": '{"type":"hsw","req":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzIjoyLCJ0IjoidyIsImQiOiIzQWU0eDN3ZVAvNW9XK0JVN3h4eHp1eWt3NTh3d3NJVTBlZC9sZjNxcGxibTlQMVdsWW1ZRHBjRmlvQ0RJcEJPdVJ5M3RsWFc2ekNnWkRYZlc2S1RIWmx6ejV6M0RIZkQwNEZjNHdYTXUxRzEvajgvZm80UnNRZDZlTmJSZG9LeEwzN3hqODB3RVJkdU5COUdGbWFFRytTa09FUWlrbVFRM1Z3SzV5RkNSTytTVkU5MnczcDNMN0ZVcGc9PXdITy9PQTFSVEFuT2FzaFgiLCJsIjoiaHR0cHM6Ly9uZXdhc3NldHMuaGNhcHRjaGEuY29tL2MvOTBhZDIzYjAiLCJlIjoxNjQ2OTA1NzM4fQ.-xDPwIadz5mwbEbeqaeugQ5_cZl5NNdNbrodKid2i7s"}',
        }

        captcha_response = session.post("https://hcaptcha.com/getcaptcha?s=9c1f7658-2de8-43d2-abca-6660f344ea1c", data=formData, headers=header)
        if captcha_response.status_code == 200:
            return captcha_response.text

def send_checkout_request(session, profile, headers):
    checkout_url = "https://www.supremenewyork.com/checkout.json"
    checkout_params = make_checkout_request(session, profile, headers)
    checkout_request = session.post(checkout_url, headers=headers, data=checkout_params)
    print("[+] Sent checkout request")
    if not checkout_request.json()['status'] == 'failed':
        print("[+] Success!")
    else:
        print("[-] Failed!")
    
    #    display_order_status(session, checkout_request)
    #else:
    #    print("[+] Failed to checkout, restart the job", "red")

def get_order_status(session, slug, headers):
    stauts_url = f"https://supremenewyork.com/checkout/{slug}/status.json"
    status_content = session.get(stauts_url, headers=headers).json()
    status = status_content["status"]
    return status

def display_order_status(session, checkout_request, headers):
    checkout_request.text
    print(checkout_request.text)
    #checkout_response = checkout_request.json()

    #status = checkout_response["slug"]
    #while True:
    #    status = get_order_status(session, status, headers)

    #    if status == "queued":
    #        print("ORDER QUEUED")
    #    elif status == "paid":
    #        print("SUCCESS, CHECK EMAIL")
    #    else:
    #        print("ORDER FAILED")



