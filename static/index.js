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
                console.log("Success:", data);

                // Create a new div element
                const responseDiv = document.createElement("div");
                responseDiv.id = "responseDiv";
                responseDiv.innerHTML = `${data.data}`;

                // Append the new div to the body (or a specific container)
                document.body.appendChild(responseDiv);


            })
            .catch(error => {
                alert("Error submitting form");
                console.error("Error:", error);
            });
    });
});
