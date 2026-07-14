const message = await pywebview.api.say_hello();

document.getElementById("Message").innerHTML = message;