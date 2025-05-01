# app.py
from flask import Flask
import running

app = Flask(__name__)

@app.route("/")
def home():
    return f"<pre>{running.display_time_and_greet('Susan')}</pre>"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))  # Render will set the port dynamically
    app.run(host="0.0.0.0", port=port)
