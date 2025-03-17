# --- Import the required libraries / modules:
from PIL import Image, ImageTk
from tkinter import messagebox


def check_image_present(image_path: str, error_message: str) -> ImageTk:
    """_summary_
    This function will check if a file is present in the specified directory.
    Args:
        image_path (str): The full path and file name to check.
        error_message (str): The error that needs to be displayed.

    Raises:
        Exception: Raise an exception if the file is not present.

    Returns:
        ImageTk: The image.
    """
    try:
        image_file = Image.open(image_path)
        
    except FileNotFoundError as error:
        messagebox.showerror("Error", f"{error}.\n\n{error_message}")
        raise Exception(error)
    
    return image_file