import requests

def get_location_info(): #define function
    return requests.get("http://freegeoip.net/json/").json()

if __name__ == "__main__":
    pprint(get_location_info())
