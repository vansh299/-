
async function generateqr() {

    let url = document.getElementById("url").value;

    if (url === "") {
        alert("Please enter a URL");
        return;
    }

    let response = await fetch("/generate", {
        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            url: url
        })
    });

    let data = await response.json();

    // Display QR Code
    document.getElementById("qr").src =
        "data:image/png;base64," + data.qr_code;
}
