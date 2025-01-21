# --- Import required libraries / modules:
from customtkinter import CTk, CTkButton, CTkImage
from tkinter.filedialog import asksaveasfile

from modules.qrcode.qr_code import generate_qr_code

# --- QR code save button command function:
def save_image(image: CTkImage) -> None:
    save_image = image._dark_image
    filename = asksaveasfile(mode= "w",
                                filetypes = [("PNG", "*.png")], 
                                defaultextension = [("PNG", "*.png")])
    save_image.save(filename.name)


def save_button(master: CTk, image: CTkImage) -> dict:
    # --- QR code save button:
    save_qr_code = CTkButton(master = master, text = "Save", 
                             command = lambda: save_image(image = image), hover=False, font=("", 16))
    save_qr_code.grid(row = 12, column = 0, padx = 10, pady = 10, sticky = "e")
    
    elements = dict()
    elements["save_button"] = save_qr_code
    
    return elements


def update_qr_code(data: str, version: int, box: int, border: int, fg_colour: tuple, bg_colour: tuple):
    from main import preview_image
    
    print(1)
    new_image = generate_qr_code(data = data,
                                 version = version,
                                 box = box,
                                 border = border,
                                 fg_colour = fg_colour, 
                                 bg_colour = bg_colour)
    
    print(2)
    preview_image.configure(dark_image = new_image.get_image(),
                            size = (new_image.get_image().width, new_image.get_image().height))
    
    print(preview_image._size)
        

    # --- QR code preview button:
def preview_button(master: CTk):
    preview_qr_code = CTkButton(master = master, text = "Preview", hover=False, font=("", 16),
                                command = lambda: update_qr_code(data = text_entry["text_data"].get(),
                                                                 version = int(qr_code_version["slider"].get()),
                                                                 box = int(qr_code_box_size["slider"].get()),
                                                                 border = int(qr_code_border_size["slider"].get()),
                                                                 fg_colour = tuple(qr_code_fg_colour["colour_picker"].rgb_color), 
                                                                 bg_colour = tuple(qr_code_bg_colour["colour_picker"].rgb_color)))
    
    preview_qr_code.grid(row = 12, column = 0, padx = 10, pady = 10, sticky = "w")
    
    elements = dict()
    elements["preview_button"] = preview_qr_code
    
    return elements