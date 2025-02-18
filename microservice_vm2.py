import platform
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/status")
def status():
    """Respond with system name and online status."""
    return jsonify({"message": "Online", "system": platform.node()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
