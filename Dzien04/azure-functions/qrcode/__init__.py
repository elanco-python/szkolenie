import logging
import validators
import json
import qrcode
import io
from PIL import Image
import base64

import azure.functions as func


def image_to_byte(img: Image, is_base64=False):
    byteIO = io.BytesIO()
    img.save(byteIO, format='PNG')
    byteArr = byteIO.getvalue()
    if is_base64:
        return base64.b64encode(byteArr).decode()
    else:
        return byteArr

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    fmt = req.params.get("format","")
    url = req.params.get("url","")
    try:
        if not validators.url(url):
            raise Exception("Not valid URL")
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        is_base64 = (fmt.lower()=="json")
        result = image_to_byte(img, is_base64)
        if (is_base64):
            return func.HttpResponse( 
                json.dumps({ "code" : 0, "message" : result }) , 
                status_code=200)
        else:
            return func.HttpResponse(result, status_code=200, mimetype="image/png" )

    except Exception as exc:
        logging.exception(exc, exc_info=True)
        return func.HttpResponse( 
            json.dumps({ "code" : -100, "message" : str(exc) }) , 
            status_code=500)
