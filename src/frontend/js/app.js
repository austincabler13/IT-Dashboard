async function loadSystemInfo() {
    const messageElement = document.getElementById("status");

    try {
        const systemInfo = await window.pywebview.api.get_system_info();
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


async function loadHardwareInfo() {
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

async function loadPerformanceInfo() {
    const messageElement = document.getElementById("status");

    try {
        const performanceInfo = await window.pywebview.api.get_performance_info();
        document.getElementById("cpu_percent").textContent = performanceInfo.cpu_percent;
        document.getElementById("memory_percent").textContent = performanceInfo.memory_percent;
        document.getElementById("memory_used").textContent = performanceInfo.memory_used;
        document.getElementById("memory_total").textContent = performanceInfo.memory_total;
        setTimeout(() => {
            messageElement.textContent = "";
        }, 3000);
    } catch (error) {
        console.error("Unable to contact backend:", error);
        messageElement.textContent = "unable to contact backend";
    }
}

async function loadStorageInfo() {
    const messageElement = document.getElementById("status");
    const storageContainer = document.getElementById("storage_drives");

    try {
        const storageInfo =
            await window.pywebview.api.get_storage_info();

        storageContainer.replaceChildren();

        for (const drive of storageInfo.drives) {
            const driveElement = document.createElement("div");
            driveElement.className = "storage-drive";

            const heading = document.createElement("h3");
            heading.textContent = drive.drive_letter;

            const mountPoint = document.createElement("p");
            mountPoint.textContent = `Drive: ${drive.mount_point}`;

            const fileSystem = document.createElement("p");
            fileSystem.textContent = `File System: ${drive.file_system}`;

            const driveUsage = document.createElement("p");
            driveUsage.textContent = `Usage: ${drive.drive_usage}`;

            const totalSpace = document.createElement("p");
            totalSpace.textContent = `Total: ${drive.total_space}`;

            const usedSpace = document.createElement("p");
            usedSpace.textContent = `Used: ${drive.used_space}`;

            const freeSpace = document.createElement("p");
            freeSpace.textContent = `Free: ${drive.free_space}`;

            driveElement.append(
                heading,
                mountPoint,
                fileSystem,
                driveUsage,
                totalSpace,
                usedSpace,
                freeSpace
            );

            storageContainer.appendChild(driveElement);
        }
    } catch (error) {
        console.error("Unable to load storage information:", error);
        messageElement.textContent =
            "Unable to load storage information";

        setTimeout(() => {
            messageElement.textContent = "";
        }, 3000);
    }
}

async function loadInfo() {
    await loadSystemInfo();
    await loadHardwareInfo();
    await loadPerformanceInfo();
    await loadStorageInfo();

    setInterval(loadPerformanceInfo, 1000);

}

function showTab(tabId){

    const tabs = document.querySelectorAll(".tab-content");

    tabs.forEach(tab => {
        tab.classList.remove("active");
    });

    document.getElementById(tabId).classList.add("active");

}

window.addEventListener("DOMContentLoaded", () => {

    showTab("overview");

    startDashboard();

});


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