let inputs = document.querySelectorAll("form input");
let labels = document.querySelectorAll("form label");

inputs.forEach(function (input) {
    input.classList.add("form-control");
})

labels.forEach(function (label) {
    label.classList.add("d-none")
})


function sendDeleteRequest(url) {
    const Http = new XMLHttpRequest();
    // Http.open("POST", url);
    Http.send("POST", url);

    // Http.onreadystatechange = (e) => {
    //     console.log(Http.responseText)
    // }
    console.log("Delete Button clicked!!! ");
}


