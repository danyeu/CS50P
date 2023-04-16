import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Incorrect usage")

try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Invalid number")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = response.json()
    rate = float(o["bpi"]["USD"]["rate_float"])
except requests.RequestException:
    sys.exit("API error")
except IndexError:
    sys.exit("API error")
except ValueError:
    sys.exit("API returned non-float")
except:
    sys.exit("JSON not returned")

print(f"${n * rate:,.4f}")