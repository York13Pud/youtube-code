# --- Import required libraries / modules
import qrcode # https://pypi.org/project/qrcode/


def generate_qr_code(data: str, version: int = 10, box: int = 10, border: int = 5, 
                     fg_colour: tuple = (0, 0, 0), bg_colour: tuple = (255, 255, 255)) -> object:
    """_summary_

    This function is used to generate a QR code image.
    
    Args:
        data (str): The information that will be used in the QR code.
        version (int, optional): The version will determine the size of the QR code.
        box (int, optional): The size of each box in the QR code. Defaults to 10.
        border (int, optional): The border size around the QR code. Defaults to 5.
        fg_colour (tuple, optional): The foreground colour of the QR code. Defaults to black (0, 0, 0) .
        bg_colour (tuple, optional): The background colour of the QR code. Defaults to white (255, 255, 255).

    Returns:
        object: The QR code as an object.
    """
    
    qr = qrcode.QRCode(version = version,
                       box_size = box,
                       error_correction = qrcode.constants.ERROR_CORRECT_M,
                       border = border)
    
    qr.add_data(data = data)
    
    qr.make(fit = True)

    img = qr.make_image(fill_color = fg_colour, 
                        back_color = bg_colour)
    
    return img

