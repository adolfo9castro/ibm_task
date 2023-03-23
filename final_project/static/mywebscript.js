
const url = 'http://localhost:8080/'

const translateToFrench = ()=>{
    const textToTranslate = document.getElementById("textToTranslate").value;

    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            console.log(xhttp.responseText);
            document.getElementById("translated_text").innerHTML = xhttp.responseText;
        }
    };
    xhttp.open("GET", `${url}englishToFrench?text=${textToTranslate}`, true);

    xhttp.send();
}

let translateToEnglish = ()=>{
    const textToTranslate = document.getElementById("textToTranslate").value;

    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("translated_text").innerHTML = xhttp.responseText;
        }
    };
    xhttp.open("GET", `${url}frenchToEnglish?text=${textToTranslate}`, true);
    xhttp.send();
}