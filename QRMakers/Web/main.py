from flask import Flask, render_template, request
import qrcode
import io
import base64

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    qr_code = None

    if request.method == "POST":
        data = request.form.get("data", "").strip()

        if data:
            # Generate QR code
            img = qrcode.make(data)

            # Convert image to bytes
            buffer = io.BytesIO()
            img.save(buffer, format="PNG")

            # Convert bytes to Base64
            qr_code = base64.b64encode(
                buffer.getvalue()
            ).decode("utf-8")

    return render_template("index.html", qr_code=qr_code)


if __name__ == "__main__":
    app.run(debug=True)