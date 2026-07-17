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


async function loadhardwareInfo() {
    const messageElement = document.getElementById("status");

    try {
        const hardwareInfo = await pywebview.api.get_hardware_info();
        document.getElementById("cpu_name").textContent = hardwareInfo.cpu_name;
        document.getElementById("physical_cores").textContent = hardwareInfo.physical_cores;
        document.getElementById("logical_processors").textContent = hardwareInfo.logical_processors;
        document.getElementById("total_memory").textContent = hardwareInfo.total_memory;
        messageElement.textContent = "Hardware info loaded successfully";
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

async function loadhardwareInfo() {
    const messageElement = document.getElementById("status");

    try {
        const hardwareInfo = await window.pywebview.api.get_hardware_info();
        document.getElementById("cpu_name").textContent = hardwareInfo.cpu_name;
        document.getElementById("physical_cores").textContent = hardwareInfo.physical_cores;
        document.getElementById("logical_processors").textContent = hardwareInfo.logical_processors;
        document.getElementById("total_memory").textContent = hardwareInfo.total_memory;
        messageElement.textContent = "Hardware info loaded successfully";
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

async function loadInfo() {
    await loadSystemInfo();
    await loadhardwareInfo();
}

function startDashboard() {
    if (window.pywebview && window.pywebview.api) {
        loadInfo();
    } else {
        window.addEventListener("pywebviewready", () => {
            loadInfo();
        }, { once: true });
    }
}

window.addEventListener("DOMContentLoaded", startDashboard);