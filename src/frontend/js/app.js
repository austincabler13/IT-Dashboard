async function loadSystemInfo() {
    const messageElement = document.getElementById("status");

    try {
        const systeminfo = await pywebview.api.get_system_info();
        document.getElementById("os").textContent = systeminfo.os;
        document.getElementById("computer_name").textContent = systeminfo.computer_name;
        document.getElementById("bitness").textContent = systeminfo.bitness;
        document.getElementById("architecture").textContent = systeminfo.architecture;
        document.getElementById("python_version").textContent = systeminfo.python_version;
    } catch (error) {
        console.error("Unable to contact backend:", error);
        messageElement.textContent = "Unable to contact the backend.";
    }
}

document
    .getElementById("RefreshButton")
    .addEventListener("click", loadSystemInfo);
