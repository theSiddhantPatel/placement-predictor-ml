from flask import Flask, request, jsonify, render_template
from model_loader import predict_placement

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", prediction=None)


@app.route("/predict", methods=["POST"])
def predict_api():
    data = request.json
    cgpa = float(data["cgpa"])
    iq = float(data["iq"])
    result = predict_placement(cgpa, iq)
    return jsonify({"prediction": result})


@app.route("/predict-ui", methods=["POST"])
def predict_ui():
    cgpa = float(request.form["cgpa"])
    iq = float(request.form["iq"])
    result = predict_placement(cgpa, iq)
    return render_template("index.html", prediction=result)


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=5000)  # for deployment
