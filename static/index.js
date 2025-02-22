document.addEventListener("DOMContentLoaded", function () {
    document.querySelector("form").addEventListener("submit", function (event) {
        event.preventDefault();
        
        const formData = {
            age: document.getElementById("age").value,
            gender: document.getElementById("gender").value,
            bloodPressure: document.getElementById("blood-pressure").value,
            heartRate: document.getElementById("heart-rate").value
        };

        fetch("http://127.0.0.1:5000/submit", {  // Ensure this URL matches your Flask route
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(formData)
        })
        .then(response => response.json())
        .then(data => {
            alert("Form submitted successfully!");
            console.log("Success:", data);
        })
        .catch(error => {
            alert("Error submitting form");
            console.error("Error:", error);
        });
    });
});
