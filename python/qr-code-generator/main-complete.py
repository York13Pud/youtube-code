# --- Import required libraries / modules:
from customtkinter import *
from CTkColorPicker import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile

from modules.qrcode.qr_code import generate_qr_code

import os
import tkinter as tk


def main() -> None:
    """This is the main entry point for the program."""
    
    # --- Get the absolute path for main.py:
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__)))

    # --- Setup the application and window:
    app = CTk()
    app._set_appearance_mode("dark")
    app.title("QR Code Generator")
    app.geometry(geometry_string = "1350x1100")
    app.resizable(width = False, height = False)

    # --- Check that the required images exist and load them ---
    
    # --- Set the icon for the program:
    try:
        icon_file = Image.open(f"{BASE_DIR}/images/icon.png")
        
    except FileNotFoundError as error:
        messagebox.showerror("Error", f"{error}.\n\nCheck that the icon file exists in that directory with the name icon.png.\n\nPress Ok to close.")
        raise Exception(error)
    
    icon = ImageTk.PhotoImage(icon_file)
    app.wm_iconphoto(False, icon)

    
    # --- Get the default placeholder image for the preview area:
    try:
        preview_image_path = Image.open(f"{BASE_DIR}/images/placeholder.png")
        
    except FileNotFoundError as error:
        messagebox.showerror("Error", f"{error}.\n\nCheck that the placeholder file exists in that directory with the name placeholder.png.\n\nPress Ok to close.")
        raise Exception(error)
    
    preview_image = CTkImage(dark_image = preview_image_path,
                             size = (preview_image_path.width, preview_image_path.height))


    # --- Build the sidebar ----
    
    # --- Define the sidebar that contains all the settings:
    sidebar = CTkFrame(master = app)
    sidebar.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "nesw")
    
    
    # --- Build the sidebar elements ---
    
    # --- URL Entry field:
    url_frame_title = CTkLabel(text = "Enter Your Text / URL", master = sidebar, font=("", 16))
    url_frame_title.grid(row = 0, column = 0, sticky="nsew", columnspan = 2, pady = (10, 0))

    url_frame = CTkFrame(master = sidebar)
    url_frame.grid(row = 1, column = 0, padx = 10, pady = 10)

    url_label = CTkLabel(text = "URL:", master = url_frame, font=("", 16))
    url_label.grid(row = 0, column = 0, padx = 10, pady = 10)

    url_text = CTkEntry(master = url_frame, width = 230, placeholder_text = "Enter text / URL", font=("", 16))
    url_text.grid(row = 0, column = 1, padx = 10, pady = 10)

    # --- QR code version:
    qr_code_version_title = CTkLabel(text = "Version", master = sidebar, font=("", 16))
    qr_code_version_title.grid(row = 2, column = 0, sticky="nsew", columnspan = 2, pady = (10, 10))

    qr_code_version_frame = CTkFrame(master = sidebar)
    qr_code_version_frame.grid(row = 3, column = 0, padx = 10, pady = 10, columnspan = 2)

    qr_code_version_value = tk.IntVar()

    qr_code_version = CTkSlider(master = qr_code_version_frame, width = 260, 
                                from_ = 1, to = 12,
                                variable = qr_code_version_value)

    qr_code_version.set(10)

    qr_code_version.grid(row = 0, column = 0, padx = 10, pady = 10)

    qr_code_version_value_label = CTkLabel(textvariable = qr_code_version_value, 
                                           master = qr_code_version_frame, font=("", 16), width = 20)
    qr_code_version_value_label.grid(row = 0, column = 1, sticky="nsew", columnspan = 2, padx = (0, 5))

    # --- QR code box size:
    qr_code_box_size_title = CTkLabel(text = "Box Size", master = sidebar, font=("", 16))
    qr_code_box_size_title.grid(row = 4, column = 0, sticky="nsew", columnspan = 2, pady = (10, 10))

    qr_code_box_size_frame = CTkFrame(master = sidebar)
    qr_code_box_size_frame.grid(row = 5, column = 0, padx = 10, pady = 10, columnspan = 2)

    qr_code_box_size_value = tk.IntVar()

    qr_code_box_size = CTkSlider(master = qr_code_box_size_frame, width = 260, 
                                 from_ = 4, to = 12, 
                                 variable = qr_code_box_size_value)

    qr_code_box_size.set(10)

    qr_code_box_size.grid(row = 0, column = 0, padx = 10, pady = 10)

    qr_code_box_size_value_label = CTkLabel(textvariable = qr_code_box_size_value, 
                                            master = qr_code_box_size_frame, font=("", 16), width = 20)
    qr_code_box_size_value_label.grid(row = 0, column = 1, sticky="nsew", columnspan = 2, padx = (0, 5))


    # --- QR code border size:
    qr_code_border_size_title = CTkLabel(text = "Border Size", master = sidebar, font=("", 16))
    qr_code_border_size_title.grid(row = 6, column = 0, sticky="nsew", columnspan = 2, pady = (10, 10))

    qr_code_border_size_frame = CTkFrame(master = sidebar)
    qr_code_border_size_frame.grid(row = 7, column = 0, padx = 10, pady = 10, columnspan = 2)

    qr_code_border_size_value = tk.IntVar()

    qr_code_border_size = CTkSlider(master = qr_code_border_size_frame, width = 260, 
                                    from_ = 1, to = 5,
                                    variable = qr_code_border_size_value)

    qr_code_border_size.set(1)

    qr_code_border_size.grid(row = 0, column = 0, padx = 10, pady = 10)

    qr_code_border_size_value_label = CTkLabel(textvariable = qr_code_border_size_value, 
                                               master = qr_code_border_size_frame, font=("", 16), width = 20)
    qr_code_border_size_value_label.grid(row = 0, column = 1, sticky="nsew", columnspan = 2, padx = (0, 5))


    # --- QR code foreground colour:
    qr_code_fg_colour_title = CTkLabel(text = "Foreground Colour", master = sidebar, font=("", 16))
    qr_code_fg_colour_title.grid(row = 8, column = 0, sticky="nsew", columnspan = 2, pady = (10, 10))

    qr_code_fg_colour = CTkColorPicker(master = sidebar, initial_color="#000000")
    qr_code_fg_colour.grid(row = 9, column = 0, columnspan=2, padx = 10, pady = 10, sticky = "nesw")


    # --- QR code background colour:
    qr_code_bg_colour_title = CTkLabel(text = "Background Colour", master = sidebar, font=("", 16))
    qr_code_bg_colour_title.grid(row = 10, column = 0, sticky="nsew", columnspan = 2, pady = (10, 10))

    qr_code_bg_colour = CTkColorPicker(master = sidebar, initial_color="#FFFFFF")

    qr_code_bg_colour.grid(row = 11, column = 0, columnspan=2, padx = 10, pady = 10, sticky = "nesw")


    # --- QR code preview button command function
    def update_qr_code():
        new_image = generate_qr_code(data = url_text.get(),
                                     version = int(qr_code_version.get()),
                                     box = int(qr_code_box_size.get()),
                                     border = int(qr_code_border_size.get()),
                                     fg_colour = tuple(qr_code_fg_colour.rgb_color), 
                                     bg_colour = tuple(qr_code_bg_colour.rgb_color))
        
        preview_image.configure(dark_image = new_image.get_image(),
                                size = (new_image.get_image().width, new_image.get_image().height))
    
    # --- QR code preview button: 
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
    qr_code_frame.grid(row = 0, column = 1, padx = (0,5), pady = 10, sticky = "nesw")

    preview_area = CTkLabel(master = qr_code_frame, image = preview_image, text="")

    preview_area.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "nesw")
    preview_area.place(x = 498, y = 498, anchor = tk.CENTER)
    

    # --- Keep the window active until it is closed:
    app.mainloop()


if __name__ == "__main__":
    main()