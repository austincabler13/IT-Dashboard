async function sayHello() {
    const message = await pywebview.api.say_hello();
    document.getElementById("Message").textContent = message;
}

document
    .getElementById("MessageButton")
    .addEventListener("click", sayHello);