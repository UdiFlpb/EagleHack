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
    
    #parse the data 
    a_male = ""
    a_age = ""
    a_education = ""
    a_currentsmoker = ""
    a_cigsperday = ""
    a_bpmmeds = ""
    a_prevalentStroke = ""
    a_prevalentHyp = ""
    a_diabetes = ""
    a_totChol = ""
    a_sysBP = ""
    a_diaBP = ""
    a_BMI = ""
    a_heartRate = ""
    a_glucose = ""
    
    #gender
    if data['gender'] == 'male':
        a_male = "1"
    else:
        a_male = "0"
    
    #age
    a_age = str(data["age"])
    
    #education
    a_education = str(data["education"])
    
    #smoker:
    if data["cigsPerDay"] == 0:
        a_currentsmoker = "0"
        a_cigsperday = "0"
    else:
        a_currentsmoker = "1"
        a_cigsperday = str(data["cigsPerDay"])
        
    #bpmmed
    if( "BPMeds" in data ):
        a_bpmmeds = "1"
    else:
        a_bpmmeds = "0"
        
    #prevalentStroke
    if "prevalentStroke" in data :
        a_prevalentStroke = "1"
    else:
        a_prevalentStroke = "0"
    
    #prevalentStroke
    if "prevalentHyp" in data:
        a_prevalentHyp = "1"
    else:
        a_prevalentHyp = "0"
        
    #prevalentStroke
    if "diabetes" in data:
        a_diabetes = "1"
    else:
        a_diabetes = "0"
        
    #totChol
    a_totChol = str(data["totChol"])
    
    #sysBP
    a_sysBP = str(data["sysBP"])
    
    #diaBP
    a_diaBP = str(data["diaBP"])
    
    #BMI
    a_BMI = str(data["BMI"])
    
    #heartRate
    a_heartRate = str(data["heartRate"])
    
    #glucose
    a_glucose = str(data["glucose"])
    
    
    #run the script here and get the answer:
    result = subprocess.run(
        ["python", "HAPred.py", 
         "--male", a_male, 
         "--age", a_age, 
         "--education", a_education, 
         "--currentSmoker", a_currentsmoker, 
         "--cigsPerDay", a_cigsperday, 
         "--BPMeds", a_bpmmeds, 
         "--prevalentStroke", a_prevalentStroke, 
         "--prevalentHyp", a_prevalentHyp, 
         "--diabetes", a_diabetes, 
         "--totChol", a_totChol, 
         "--sysBP", a_sysBP, 
         "--diaBP", a_diaBP, 
         "--BMI", a_BMI, 
         "--heartRate", a_heartRate, 
         "--glucose", a_glucose],
        capture_output=True, 
        text=True
    )
    
    if(result.stdout.__contains__("yes")):
        #yes response
        return jsonify({"message": "Form submitted successfully", "data": "<p><strong>After evaluating your results, you are at risk for heart disease. We suggest that you consult with a doctor.</strong></p>"})

    if(result.stdout.__contains__("no")):
        #no response
        return jsonify({"message": "Form submitted successfully", "data": "<p><strong>After evaluating your results, you are not at risk for heart disease. Please stay healthy :)</strong></p>"})
    else:
        return jsonify({"message": "Form submitted successfully", "data": "<p><strong>Problem accured.</strong></p>"})

    
if __name__ == '__main__':
    app.run(debug=True)