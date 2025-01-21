# --- Import required libraries / modules:
from customtkinter import CTk, CTkEntry, CTkFrame, CTkLabel


def text_elements(master: CTk) -> dict:
    elements: dict = dict()
    
    text_title = CTkLabel(text = "Enter Your Text / URL", master = master, font=("", 16))
    text_title.grid(row = 0, column = 0, sticky="nsew", columnspan = 2, pady = (10, 0))
    
    text_frame = CTkFrame(master = master)
    text_frame.grid(row = 1, column = 0, padx = 10, pady = 10)

    text_label = CTkLabel(text = "URL:", master = text_frame, font=("", 16))
    text_label.grid(row = 0, column = 0, padx = 10, pady = 10)
    
    text_data = CTkEntry(master = text_frame, width = 230, placeholder_text = "Enter text / URL", font=("", 16))
    text_data.grid(row = 0, column = 1, padx = 10, pady = 10)
    
    elements["text_title"] = text_title
    elements["text_frame"] = text_frame
    elements["text_label"] = text_label
    elements["text_data"] = text_data
    
    return elements

# a=1