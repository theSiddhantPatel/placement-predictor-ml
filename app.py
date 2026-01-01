from flask import (
    Flask,
    request,
    jsonify,
    render_template,
    redirect,
    url_for,
    flash,
    get_flashed_messages,
)
from model_loader import predict_placement

app = Flask(__name__)

# required for flash messages (temporary server-side storage)
app.secret_key = "dev-secret-key"


# ---------- UI ROUTES ----------


@app.route("/")
def home():
    """
    Home page.
    Shows prediction once (if available), then clears on refresh.
    """
    messages = get_flashed_messages()
    prediction = messages[0] if messages else None
    return render_template("index.html", prediction=prediction)


@app.route("/predict-ui", methods=["POST"])
def predict_ui():
    """
    Handles form submission.
    Uses POST → Redirect → GET pattern.
    """
    cgpa = float(request.form["cgpa"])
    iq = float(request.form["iq"])

    result = predict_placement(cgpa, iq)

    # store prediction for exactly one request
    flash(result)

    # redirect to home so refresh clears the form
    return redirect(url_for("home"))


# ---------- API ROUTES ----------


@app.route("/predict", methods=["POST"])
def predict_api():
    """
    JSON API endpoint (for Postman / future frontend).
    """
    data = request.json
    cgpa = float(data["cgpa"])
    iq = float(data["iq"])

    result = predict_placement(cgpa, iq)

    return jsonify({"prediction": result})


@app.route("/health")
def health():
    """
    Health check for deployment platforms.
    """
    return {"status": "ok"}


# ---------- ENTRY POINT ----------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
