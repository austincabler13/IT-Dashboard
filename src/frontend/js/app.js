async function sayHello() {
    const messageElement = document.getElementById("Message");

    try {
        const message = await pywebview.api.say_hello();
        messageElement.textContent = message;
    } catch (error) {
        console.error("Unable to contact backend:", error);
        messageElement.textContent = "Unable to contact the backend.";
    }
}

document
    .getElementById("MessageButton")
    .addEventListener("click", sayHello);
