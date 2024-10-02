document.getElementById("send-btn").addEventListener("click", sendMessage);

function sendMessage() {
  const userInput = document.getElementById("user-input").value;
  if (userInput.trim() !== "") {
    displayMessage(userInput, "user-message");
    document.getElementById("user-input").value = ""; // Clear input
    fetchResponse(userInput);
  }
}

function displayMessage(message, messageType) {
  const chatBox = document.getElementById("chat-box");
  const messageElement = document.createElement("div");
  messageElement.classList.add("message", messageType);
  messageElement.textContent = message;
  chatBox.appendChild(messageElement);
  chatBox.scrollTop = chatBox.scrollHeight; // Scroll to the bottom
}

function fetchResponse(userInput) {
  fetch("http://localhost:5000/get_response", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ user_input: userInput })
  })
  .then(response => response.json())
  .then(data => {
    displayMessage(data.response, "bot-message");
  })
  .catch(error => {
    console.error("Error:", error);
  });
}
