async function sayHello() {
    const message = await pywebview.api.Say_Hello();
    document.getElementById("Message").textContent = message;
}

document
    .getElementById("MessageButton")
    .addEventListener("click", sayHello);