from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import os
import time


app = Flask(__name__)
CORS(
    app
)  # Enables CORS for all domains. For specific domain, use CORS(app, resources={r"/api/*": {"origins": "https://your-squarespace-site.com"}})


# TODO: Error handling
# TODO: User input santitization
# TODO: Better styling on the website chat
# TODOLATER: Subdomains on squarespace
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    return jsonify({"response": "request received"})


@app.route("/")
@cross_origin()
def index():
    return "Hello from Flask!"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
