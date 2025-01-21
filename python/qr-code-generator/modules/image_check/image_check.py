# --- Import required libraries / modules:
from PIL import Image, ImageTk
from tkinter import messagebox


def check_image_present(image_path: str, error_message: str) -> ImageTk:
    
    try:
        image_file = Image.open(image_path)
        
    except FileNotFoundError as error:
        messagebox.showerror("Error", f"{error}.\n\n{error_message}")
        raise Exception(error)
    
    return image_file

    
    # # --- Get the default placeholder image for the preview area:
    # try:
    #     preview_image_path = Image.open(f"{BASE_DIR}/images/placeholder.png")
        
    # except FileNotFoundError as error:
    #     messagebox.showerror("Error", f"{error}.\n\nCheck that the placeholder file exists in that directory with the name placeholder.png.\n\nPress Ok to close.")
    #     raise Exception(error)
    
    # preview_image = CTkImage(dark_image = preview_image_path,
    #                          size = (preview_image_path.width, preview_image_path.height))