
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import qrcode
from io import BytesIO
import base64


app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/scripts", StaticFiles(directory="scripts"), name="scripts")

class QRData(BaseModel):
    url: str



@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

@app.post("/generate")
def generate(data: QRData):

    # Get URL from JavaScript
    user_url = data.url

    # Generate QR Code
    qr = qrcode.make(user_url)

    # Convert QR image into bytes
    buffer = BytesIO()
    qr.save(buffer, format="PNG")

    # Convert image into Base64
    img_base64 = base64.b64encode(buffer.getvalue()).decode()

    return {
        "qr_code": img_base64
    }