const chatContainer = document.getElementById("chat-container");
const userInput = document.getElementById("user-input");
const sendBtn = document.getElementById("send-btn");

// Add a message to the chat
function addMessage(message, sender) {
    const messageDiv = document.createElement("div");

    if (sender === "user") {
        messageDiv.className = "user-message";
    } else {
        messageDiv.className = "bot-message";
    }

    messageDiv.innerHTML = message;

    chatContainer.appendChild(messageDiv);

    // Scroll to the latest message
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

// Send message to Flask backend
async function sendMessage() {

    const message = userInput.value.trim();

    if (message === "") {
        return;
    }

    // Display user message
    addMessage(message, "user");

    userInput.value = "";

    // Show loading message
    const loadingDiv = document.createElement("div");
    loadingDiv.className = "bot-message";
    loadingDiv.innerHTML = "🤖 Thinking...";
    chatContainer.appendChild(loadingDiv);

    chatContainer.scrollTop = chatContainer.scrollHeight;

    try {

        const response = await fetch("/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })

        });

        const data = await response.json();

        // Remove loading message
        loadingDiv.remove();

        // Display AI response
        addMessage(data.reply, "bot");

    } catch (error) {

        loadingDiv.remove();

        addMessage(
            "❌ Unable to connect to the server. Please try again.",
            "bot"
        );
    }
}

// Send button click
sendBtn.addEventListener("click", sendMessage);

// Press Enter to send
userInput.addEventListener("keypress", function (event) {

    if (event.key === "Enter") {
        sendMessage();
    }

});