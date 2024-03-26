from flask import Flask, request
import requests

app = Flask(__name__)

# Thay thế YOUR_TOKEN dengan token của bạn
TOKEN = "962416910cd8f4"

# Thay thế YOUR_SECRET_KEYS dengan danh sách các secret key hợp lệ
SECRET_KEYS = ["0]ZI%m:4W0FS>M>", "baf<xm%`K;yk=Gs", "uoih%[ST]9XT?]4"]

@app.route("/getifnative", methods=["POST"])
def check_ip():
    # Ensure request is sent with JSON data
    if not request.is_json:
        return {"error": "Missing secret key in request body"}, 400

    # Try to get the JSON data
    try:
        data = request.get_json()
    except:
        return {"error": "Missing secret key in request body"}, 400

    # Check if 'secret_key' key exists in the JSON
    if "secret_key" not in data:
        return {"error": "Missing secret key in request body"}, 401

    # Get the secret key from the request body
    secret_key = data["secret_key"]

    # Validate the secret key against the list
    if secret_key not in SECRET_KEYS:
        return {"error": "Invalid secret key"}, 401

    # Assuming the proxy server sets a header named 'X-Forwarded-For'
    user_ip = request.headers.get('X-Forwarded-For')

    # If the header is not present, fall back to remote_addr
    if not user_ip:
        user_ip = request.remote_addr

    ip_address = user_ip

    url = "https://ipinfo.io/{}/json?token={}".format(ip_address, TOKEN)
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return {"country_code": data.get("country")}
    else:
        raise ValueError("Lỗi khi truy cập API ipinfo.io")
