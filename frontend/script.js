async function loadRandomVideo() {
    const response = await fetch("/video");
    const data = await response.json();
    const video = document.getElementById("viewer");
    const source = document.getElementById("source");

    source.src = data.file;
    video.load();
    document.getElementById("title").textContent = data.title;
}

document.getElementById("randBtn").addEventListener("click", loadRandomVideo);

loadRandomVideo();