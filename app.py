# app.py
from flask import Flask
import running

app = Flask(__name__)

@app.route("/")
def home():
    message = cool_greet.display_time_and_greet("Sunil")
    # Wrap in <pre> to preserve ASCII formatting
    return f"<pre>{message}</pre>"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
