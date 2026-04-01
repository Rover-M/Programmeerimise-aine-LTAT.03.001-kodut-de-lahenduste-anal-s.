document.addEventListener("DOMContentLoaded", function () {
    const dropZone = document.getElementById("dropZone");
    const fileInput = document.getElementById("fileInput");
    const selectedFileList = document.getElementById("selectedFileList");

    if (!dropZone || !fileInput || !selectedFileList) {
        return;
    }

    function updateSelectedFiles(files) {
        selectedFileList.innerHTML = "";

        if (!files || files.length === 0) {
            selectedFileList.innerHTML = '<li class="placeholder">Faile pole veel valitud.</li>';
            return;
        }

        Array.from(files).forEach(file => {
            const li = document.createElement("li");
            li.textContent = `${file.name} — valmis üleslaadimiseks`;
            selectedFileList.appendChild(li);
        });
    }

    fileInput.addEventListener("change", function () {
        updateSelectedFiles(fileInput.files);
    });

    dropZone.addEventListener("dragover", function (e) {
        e.preventDefault();
        dropZone.classList.add("dragover");
    });

    dropZone.addEventListener("dragleave", function () {
        dropZone.classList.remove("dragover");
    });

    dropZone.addEventListener("drop", function (e) {
        e.preventDefault();
        dropZone.classList.remove("dragover");

        const files = e.dataTransfer.files;
        fileInput.files = files;
        updateSelectedFiles(files);
    });
});