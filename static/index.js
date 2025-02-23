document.getElementById("myForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent default form submission

    // Collect form data
    const formData = {
        male: document.getElementById("male").checked,
        age: parseInt(document.getElementById("age").value),
        education: parseInt(document.getElementById("education").value),
        currentSmoker: document.getElementById("currentSmoker").checked,
        cigsPerDay: parseInt(document.getElementById("cigsPerDay").value) || 0,
        BPMeds: document.getElementById("BPMeds").checked,
        prevalentStroke: document.getElementById("prevalentStroke").checked,
        prevalentHyp: document.getElementById("prevalentHyp").checked,
        diabetes: document.getElementById("diabetes").checked,
        totChol: parseInt(document.getElementById("totChol").value),
        sysBP: parseFloat(document.getElementById("sysBP").value),
        diaBP: parseFloat(document.getElementById("diaBP").value),
        BMI: parseFloat(document.getElementById("BMI").value),
        heartRate: parseInt(document.getElementById("heartRate").value),
        glucose: parseInt(document.getElementById("glucose").value)
    };

    // Send data to backend
    fetch("http://127.0.0.1:5000/submit", { // Replace with your backend URL
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        console.log("Success:", data);

        // Update or create response div
        let responseDiv = document.getElementById("responseDiv");
        responseDiv.innerHTML = `<p><strong>Server Response:</strong> ${data.message}</p>`;
    })
    .catch(error => {
        console.error("Error:", error);
    });
});