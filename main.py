from flask import Flask, request
import requests
import json
import os

app = Flask(__name__)
api_key = os.environ['API_KEY']


@app.route("/")
def index():
    ip_address = request.args.get("ip_address", "")
    if ip_address:
        result = check_ip(ip_address)
    else:
        result = ""
    return (
        """<h1>Check if IP proxy of not</h1>
            <form action="" method="get">
                Type IP address: <input type="text" name="ip_address">
                <input type="submit" value="Check">
            </form>
        """
        + "Result: "
        + result
    )


def check_ip(ip):
    try:
        headers = {
            "X-API-KEY": f"{api_key.strip()}"
        }
        r = json.loads(requests.get(
            f"https://api.seon.io/SeonRestService/ip-api/v1.1/{ip.strip()}", headers=headers).text)
        data = r['data']
        if data['web_proxy'] or data['public_proxy']:
            return "PROXY"
        else:
            return "NOT PROXY"
    except:
        "An error occurred while processing the request"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
