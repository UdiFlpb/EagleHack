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
    
    #run the script here and get the answer:
    
    
    #yes response
    return jsonify({"message": "Form submitted successfully", "data": "<p><strong>We are 85% sure that you will have a heart attack.\nConsider talking to a doctor.</strong></p>"})

    #no response
    return jsonify({"message": "Form submitted successfully", "data": "<p><strong>We are 85% sure that you will not have a heart attack.</strong></p>"})

    
if __name__ == '__main__':
    app.run(debug=True)