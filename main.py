from flask import Flask, request
import requests

app = Flask(__name__)

# Thay thế YOUR_TOKEN bằng token của bạn
TOKEN = "962416910cd8f4"

# Thay thế YOUR_SECRET_KEY bằng secret key của bạn
SECRET_KEY = "123456"

@app.route("/check-ip")
def check_ip():
    secret_key = request.headers.get("secret-key")
    if secret_key != SECRET_KEY:
        return {"error": "Invalid secret key"}, 401

    ip_address = request.remote_addr

    url = "https://ipinfo.io/{}/json?token={}".format(ip_address, TOKEN)
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return {"ip_address": ip_address, "country_code": data.get("country")}
    else:
        raise ValueError("Lỗi khi truy cập API ipinfo.io")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
