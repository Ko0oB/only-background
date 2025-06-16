document.getElementById('uploadForm').addEventListener('submit', (e) => {
  e.preventDefault();

  const loadingMessage = document.getElementById('loadingMessage');
  const progressContainer = document.getElementById('progressContainer');
  const progressBar = document.getElementById('progressBar');
  const resultDiv = document.getElementById('result');
  const imgElem = document.getElementById('resultImage');

  loadingMessage.style.display = 'none';
  progressContainer.style.display = 'none';
  resultDiv.style.display = 'none';

  const files = document.getElementById('images').files;
  if (files.length < 2) {
    alert('Wybierz przynajmniej 2 zdjęcia');
    return;
  }

  const formData = new FormData();
  for (let file of files) {
    formData.append('images', file);
  }

  const xhr = new XMLHttpRequest();
  xhr.open('POST', '/upload', true);

  xhr.upload.onprogress = function (e) {
    if (e.lengthComputable) {
      const percent = Math.round((e.loaded / e.total) * 100);
      progressContainer.style.display = 'block';
      progressBar.style.width = percent + '%';
      progressBar.textContent = percent + '%';
    }
  };

  xhr.onloadstart = function () {
    loadingMessage.style.display = 'block';
    progressBar.style.width = '0%';
    progressBar.textContent = '0%';
    progressContainer.style.display = 'block';
  };

  xhr.onload = function () {
    loadingMessage.style.display = 'none';
    progressContainer.style.display = 'none';

    if (xhr.status === 200) {
      const data = JSON.parse(xhr.responseText);
      imgElem.src = data.result_image + '?t=' + Date.now();
      resultDiv.style.display = 'block';
    } else {
      alert('Błąd podczas przesyłania lub przetwarzania');
    }
  };

  xhr.onerror = function () {
    loadingMessage.style.display = 'none';
    progressContainer.style.display = 'none';
    alert('Błąd połączenia');
  };

  xhr.send(formData);
});
