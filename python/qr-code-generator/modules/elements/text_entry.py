# --- Import required libraries / modules:
from customtkinter import CTkEntry, CTkFrame, CTkLabel


def text_elements(master: object) -> dict:
    """_summary_
    This function creates a text entry field, that includes a title and a frame.
    
    Args:
        master (object): The name of the master that the frame will belong to.

    Returns:
        dict: A dictionary containing all of the objects generated in this function.
    """
    
    text_title = CTkLabel(text = "Enter Your Text / URL", master = master, font=("", 16))
    text_title.grid(row = 0, column = 0, sticky="nsew", columnspan = 2, pady = (10, 0))
    
    text_frame = CTkFrame(master = master)
    text_frame.grid(row = 1, column = 0, padx = 10, pady = 5)

    text_label = CTkLabel(text = "Text:", master = text_frame, font=("", 16))
    text_label.grid(row = 0, column = 0, padx = 10, pady = 5)
    
    text_data = CTkEntry(master = text_frame, width = 230, placeholder_text = "Enter text / URL", font=("", 16))
    text_data.grid(row = 0, column = 1, padx = 10, pady = 5)
    
    # --- Create an empty dictionary:
    elements = dict()
    
    # --- Add the title, frame, text box and text box label to the elements dictionary:
    elements["text_title"] = text_title
    elements["text_frame"] = text_frame
    elements["text_label"] = text_label
    elements["text_data"] = text_data
    
    return elements

# a=1