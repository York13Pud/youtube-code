# --- Import required libraries / modules
import qrcode # https://pypi.org/project/qrcode/


def generate_qr_code(url: str, box: int = 10, fg_colour: tuple() = (0, 0, 0), bg_colour: tuple() = (255, 255, 255)):
    qr = qrcode.QRCode(version = 10,
                       box_size = box,
                       error_correction=qrcode.constants.ERROR_CORRECT_L,
                       border = 10)
    
    qr.add_data(data = url)
    
    qr.make(fit = True)

    img = qr.make_image(fill_color = fg_colour, 
                        back_color = bg_colour)
    
    print("W")
    
    return img
    #img.save("test1.png")