# --- Import required libraries / modules
import os
import qrcode # https://pypi.org/project/qrcode/


def generate_qr_code() -> None:
    data = "https://www.google.com/"
    
    qr = qrcode.QRCode(version = 3,
                       box_size = 10,
                       border = 5)
    
    qr.add_data(data = data)
    
    qr.make(fit = True)

    img = qr.make_image(fill_color = "yellow", back_color = "black")
    
    img.save("test1.png")