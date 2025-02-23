// Handle form submission
document.getElementById('myForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const formData = new FormData(this);
    const data = {};

    // Gather and parse data
    for (let [key, value] of formData.entries()) {
      const input = this.elements[key];
      if (input.type === 'checkbox') {
        data[key] = input.checked;
      } else if (input.type === 'number') {
        data[key] = Number(value);
      } else {
        data[key] = value;
      }
    }

    console.log('Form Data:', data);

    // Send data to backend
    fetch("http://127.0.0.1:5000/submit", { // Replace with your backend URL
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(answer => {
        console.log("Success:", answer);

        //make the form dissapear
        document.getElementById('form-container').style.display = "none";
        // Update or create response div
        let responseDiv = document.getElementById("container");
        responseDiv.innerHTML = `${answer.data}`;
    })
    .catch(error => {
        console.error("Error:", error);
    });
});

  // Toggle "Cigarettes Per Day" based on "Current Smoker" checkbox
  const smokerCheckbox = document.querySelector('[name="currentSmoker"]');
  const cigsPerDayGroup = document.getElementById('cigsPerDayGroup');

  function toggleCigsPerDay() {
    cigsPerDayGroup.style.display = smokerCheckbox.checked ? 'block' : 'none';
  }
  toggleCigsPerDay();
  smokerCheckbox.addEventListener('change', toggleCigsPerDay);