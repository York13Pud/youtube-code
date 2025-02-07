# --- Import required libraries / modules
import os
import qrcode # https://pypi.org/project/qrcode/


def generate_qr_code(data: str, filename:str = "qrcode") -> None:
    
    qr = qrcode.QRCode(version = 3,
                       box_size = 10,
                       border = 5)
    
    qr.add_data(data = data)
    
    qr.make(fit = True)

    img = qr.make_image(fill_color = "yellow", back_color = "black")
    
    img.save(f"{filename}.png")
    

if __name__ == "__main__":
    os.system("clear")
    
    generate_qr_code(
        data = input("What would you like the QR Code to contain?:\n"),
        filename = input("\nEnter the filename to save to:\n")
        )