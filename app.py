from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = ""

    if request.method == "POST":
        url = request.form["url"]

        if (
            url.count(".") >= 3
            or "@" in url
            or len(url) > 30
            or "login" in url.lower()
            or "verify" in url.lower()
            or "bank" in url.lower()
        ):
            result = "⚠️ Suspicious URL Detected"
        else:
            result = "✅ URL Looks Safe"

    return f"""
    <body style='background:#1e1e1e; color:white; text-align:center;'>
    <h1 style='color:cyan;'>🔐 Phishing URL Detector</h1>

    <form method='POST' style='margin-top:20px;'>

        <input type='text' name='url' placeholder='Enter URL' style='width:300px; padding:10px;'>

        <button type='submit' style='padding:10px; background:cyan;'>Check URL</button>

    </form>

    <h2 style='color:lime; margin-top:20px;'>{result}</h2>
    </body>
    """

app.run(debug=True)