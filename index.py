from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from openai import OpenAI
import os
import time


app = Flask(__name__)
CORS(
    app
)  # Enables CORS for all domains. For specific domain, use CORS(app, resources={r"/api/*": {"origins": "https://your-squarespace-site.com"}})

# OPENAI_API_KEY = "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"
KOYUKI_API_KEY = "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"
# UWU_ID = 'asst_wxtdsDIEW8o8Z7s2DVnSRZwE'
# CONTRARIAN_ID = "asst_Iff45DG5TaSjLPrOzSK6ztyg"
DNS_ID = "asst_zdQvBwauDYXhh5BNG2HsktYe"

client = OpenAI(api_key=KOYUKI_API_KEY)


# TODO: Error handling
# TODO: User input santitization
# TODO: Better styling on the website chat
# TODOLATER: Subdomains on squarespace
@app.route("/chat", methods=["POST"])
@cross_origin(
    origins="https://lettuce-elk-tpmh.squarespace.com"
)  # Allows CORS for this route. For specific domain, use @cross_origin(origins="https://your-squarespace-site.com")
def chat():
    user_message = request.json["message"]
    thread = client.beta.threads.create()
    message = client.beta.threads.messages.create(
        thread.id,
        role="user",
        content=user_message,
    )
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=DNS_ID,
    )
    while run.status != "completed":
        time.sleep(0.5)
        run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
    messages = client.beta.threads.messages.list(thread_id=thread.id)
    print(dir(messages.data))
    last_message = messages.data[0].content[0].text.value
    return jsonify({"response": last_message})


@app.route("/")
@cross_origin()
def index():
    return "Hello from Flask!"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
