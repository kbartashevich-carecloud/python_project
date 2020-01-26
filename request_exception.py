import sys
import requests

url = sys.argv[1]

response = requests.get(url)

print(response.content)


try:
    response = requests.get("https://github.com/not_found", timeout=30)
    response.raise_for_status()
except requests.Timeout:
    print("error timeout, url:", url)
except requests.HTTPError as err:
    code = err.response.status_code
