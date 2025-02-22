from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

# Serve the homepage
@app.route('/')
def home():
    return render_template('index.html')

@app.route("/submit", methods=["POST"])
def submit():
    data = request.json
    print("Received data:", data)
    return jsonify({"message": "Form submitted successfully", "data": data})

if __name__ == '__main__':
    app.run(debug=True)