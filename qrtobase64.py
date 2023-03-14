import qrcode
import qrcode.image.svg
from io import BytesIO
from base64 import b64encode

qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=4,
            border=4,
        )
        
qr.add_data("Insert your data here")
qr.make(fit=True) 

img = qr.make_image()
buffered = BytesIO()

img.save(buffered, format="PNG")

img_str = b64encode(buffered.getvalue()).decode("utf-8")
print(img_str)
