import json

def add_profile():
    profiles = []
    profile = {}

    profile["profile_name"] = "Main"
    profile["name"] = "Michael"
    profile["email"] = "test@example.com"
    profile["tel"] = "07826186281"
    profile["address"] = "1 test street"
    profile["zip"] = "ST11QL"
    profile["city"] = "Sunderland"
    profile["state"] = ""
    profile["country"] = "GB"

    profile["card_number"] = "1111111111111111"
    profile["exp_month"] = "02/2022"
    profile["cvv"] = "123"

    profiles.append(profile)
    print(profiles)

    with open("data.json", "w") as f:
        json.dump(profiles, f)
