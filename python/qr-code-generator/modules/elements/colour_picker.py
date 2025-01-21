# --- Import required libraries / modules:
from customtkinter import CTk, CTkLabel
from CTkColorPicker import CTkColorPicker


def colour_picker(title: str, master: CTk, title_row: int, title_column: int, sticky: str,
                  colour_picker_row: int, colour_picker_column: int, default_colour: str) -> dict:
    
    elements: dict = dict()
    
    colour_picker_title = CTkLabel(text = title, master = master, font=("", 16))
    colour_picker_title.grid(row = title_row, column = title_column, sticky = sticky, 
                             columnspan = 2, pady = (10, 10))

    colour_picker = CTkColorPicker(master = master, initial_color = default_colour)
    colour_picker.grid(row = colour_picker_row, column = colour_picker_column, 
                       columnspan=2, padx = 10, pady = 10, sticky = sticky)
    
    elements["colour_picker_title"] = colour_picker_title
    elements["colour_picker"] = colour_picker
    
    return elements