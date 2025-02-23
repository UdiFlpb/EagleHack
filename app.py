from flask import Flask, render_template, request, jsonify
import subprocess

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
    result = subprocess.run(
        ["python", "HAPred.py", "--male", "1", "--age", "1", "--education", "1", "--currentSmoker", "0", "--cigsPerDay", "0", "--BPMeds", "0", "--prevalentStroke", "0", "--prevalentHyp", "0", "--diabetes", "0", "--totChol", "0", "--sysBP", "0", "--diaBP", "0", "--BMI", "0", "--heartRate", "0", "--glucose", "0"],
        capture_output=True, 
        text=True
    )
    
    if(result.stdout.__contains__("yes")):
        #yes response
        return jsonify({"message": "Form submitted successfully", "data": "<p><strong>We are 85% sure that you will have a heart attack.\nConsider talking to a doctor.</strong></p>"})

    if(result.stdout.__contains__("no")):
        #no response
        return jsonify({"message": "Form submitted successfully", "data": "<p><strong>We are 85% sure that you will not have a heart attack.</strong></p>"})
    else:
        return jsonify({"message": "Form submitted successfully", "data": "<p><strong>Problem accured.</strong></p>"})

    
if __name__ == '__main__':
    app.run(debug=True)