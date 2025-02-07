# --- Import required libraries / modules:
from customtkinter import *
from CTkColorPicker import *
from PIL import ImageTk
from tkinter.filedialog import asksaveasfile

from modules.elements.colour_picker import colour_picker
from modules.elements.text_entry import text_elements
from modules.elements.slider import create_slider
from modules.image_check.image_check import check_image_present
from modules.qrcode.qr_code import generate_qr_code

import os
import tkinter as tk


def main() -> None:
    """This is the main entry point for the program."""
    
    # --- Get the absolute path for main.py:
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__)))


    # --- Check to see if the icon image is present and apply it if so:
    icon_check = check_image_present(image_path = f"{BASE_DIR}/images/icon.png", 
                                     error_message = f"Check that the icon file exists in that directory with the name icon.png.\n\nPress Ok to close.")
    
    # --- Check to see if the placeholder image is present and if so setup image for the preview area:
    preview_image_check = check_image_present(image_path = f"{BASE_DIR}/images/placeholder.png",
                                              error_message = "Check that the placeholder file exists in that directory with the name placeholder.png.\n\nPress Ok to close.")
    
    preview_image = CTkImage(dark_image = preview_image_check,
                             size = (preview_image_check.width, preview_image_check.height))
    

    # --- Setup the application and window:
    app = CTk()
    app._set_appearance_mode("dark")
    app.title("QR Code Generator")
    app.geometry(geometry_string = "1350x990")
    app.resizable(width = False, height = False)
    
    icon = ImageTk.PhotoImage(icon_check)
    app.wm_iconphoto(False, icon)

    # --- Build the sidebar ----  

    # --- Define the sidebar that contains all the settings:
    sidebar = CTkFrame(master = app)
    sidebar.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "nesw")
    
    
    # --- Build the sidebar elements ---
   
    # --- Text Entry field:
    text_entry = text_elements(master=sidebar)
    
    for key in text_entry:
        text_entry[key]

    # --- QR code version slider:
    qr_code_version = create_slider(title = "Version", master = sidebar, title_row = 2, title_column = 0,
                                    frame_row = 3, frame_column = 0,
                                    slider_row = 0, slider_column = 0, default_value = 10, slider_from = 1, slider_to = 12,
                                    label_row = 0, label_column = 1)
    
    for key in qr_code_version:
        qr_code_version[key]

 
    # --- QR code box size slider:
    qr_code_box_size = create_slider(title = "Box Size", master = sidebar, title_row = 4, title_column = 0,
                                     frame_row = 5, frame_column = 0,
                                     slider_row = 0, slider_column = 0, default_value = 10, slider_from = 4, slider_to = 12,
                                     label_row = 0, label_column = 1)
    
    for key in qr_code_box_size:
        qr_code_box_size[key]


    # --- QR code border size slider:
    qr_code_border_size = create_slider(title = "Border Size", master = sidebar, title_row = 6, title_column = 0,
                                        frame_row = 7, frame_column = 0,
                                        slider_row = 0, slider_column = 0, default_value = 1, slider_from = 1, slider_to = 5,
                                        label_row = 0, label_column = 1)
    
    for key in qr_code_border_size:
        qr_code_border_size[key]
    

    # --- QR code foreground colour picker:
    qr_code_fg_colour = colour_picker(title = "Foreground Colour", master = sidebar, title_row = 8, title_column = 0,
                                      sticky = "nsew", colour_picker_row= 9, colour_picker_column = 0,
                                      default_colour = "#000000")
    
    for key in qr_code_fg_colour:
        qr_code_fg_colour[key]


    # --- QR code background colour picker:
    qr_code_bg_colour = colour_picker(title = "Background Colour", master = sidebar, title_row = 10, title_column = 0,
                                      sticky = "nsew", colour_picker_row= 11, colour_picker_column = 0,
                                      default_colour = "#FFFFFF")
    
    for key in qr_code_bg_colour:
        qr_code_bg_colour[key]
    
    
    # --- QR code preview button command function
    def update_qr_code():
        new_image = generate_qr_code(data = text_entry["text_data"].get(),
                                     version = int(qr_code_version["slider"].get()),
                                     box = int(qr_code_box_size["slider"].get()),
                                     border = int(qr_code_border_size["slider"].get()),
                                     fg_colour = tuple(qr_code_fg_colour["colour_picker"].rgb_color), 
                                     bg_colour = tuple(qr_code_bg_colour["colour_picker"].rgb_color))
        
        preview_image.configure(dark_image = new_image.get_image(),
                                size = (new_image.get_image().width, new_image.get_image().height))
        

    # # --- QR code preview button:
    preview_qr_code = CTkButton(master = sidebar, text = "Preview", hover=False, font=("", 16),
                                command = update_qr_code)
    
    preview_qr_code.grid(row = 12, column = 0, padx = 10, pady = 10, sticky = "w")
    
    
    # --- QR code save button command function:        
    def save_image() -> None:
        save_image = preview_image._dark_image
        filename = asksaveasfile(mode= "w",
                                 filetypes = [("PNG", "*.png")], 
                                 defaultextension = [("PNG", "*.png")])
        save_image.save(filename.name)

    # --- QR code save button:
    save_qr_code = CTkButton(master = sidebar, text = "Save", command = save_image, hover=False, font=("", 16))
    save_qr_code.grid(row = 12, column = 0, padx = 10, pady = 10, sticky = "e")


    # --- QR Code image area ---
    
    # --- Define the frame that contains the QR code or placeholder image:
    qr_code_frame = CTkFrame(master = app, width=996)
    qr_code_frame.grid(row = 0, column = 1, padx = (0,5), pady = 5, sticky = "nesw")

    preview_area = CTkLabel(master = qr_code_frame, image = preview_image, text="")

    preview_area.grid(row = 0, column = 0, padx = 10, pady = 5, sticky = "nesw")
    preview_area.place(x = 498, y = 498, anchor = tk.CENTER)
    
    # --- Keep the window active until it is closed:
    app.mainloop()


# --- Run the program:
if __name__ == "__main__":
    main()