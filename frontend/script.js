async function loadRandomVideo() {
    const response = await fetch("http://127.0.0.1:8000/video");
    const data = await response.json();
    const video = document.getElementById("viewer");
    const source = document.getElementById("source");

    source.src = "http://127.0.0.1:8000/" + data.file;
    video.load();
    document.getElementById("title").textContent = data.title;
}

document.getElementById("randBtn").addEventListener("click", loadRandomVideo);

loadRandomVideo();