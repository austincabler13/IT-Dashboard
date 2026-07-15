async function loadSystemInfo() {
    const messageElement = document.getElementById("status");

    try {
        const systemInfo = await pywebview.api.get_system_info();
        document.getElementById("os").textContent = systemInfo.os;
        document.getElementById("computer_name").textContent = systemInfo.computer_name;
        document.getElementById("bitness").textContent = systemInfo.bitness;
        document.getElementById("architecture").textContent = systemInfo.architecture;
        document.getElementById("python_version").textContent = systemInfo.python_version;
        messageElement.textContent = "System info loaded successfully";
        setTimeout(() => {
            messageElement.textContent = "";
        }, 3000);
    } catch (error) {
        console.error("Unable to contact backend:", error);
        messageElement.textContent = "unable to contact backend";
        setTimeout(() => {
            messageElement.textContent = "";
        }, 3000);
    }
}

document
    .getElementById("RefreshButton")
    .addEventListener("click", loadSystemInfo);
