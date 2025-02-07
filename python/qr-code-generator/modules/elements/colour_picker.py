# --- Import required libraries / modules:
from customtkinter import CTkLabel
from CTkColorPicker import CTkColorPicker


def colour_picker(title: str, master: object, title_row: int, title_column: int, 
                  colour_picker_row: int, colour_picker_column: int, 
                  default_colour: str, sticky: str = "nsew")-> dict:
    
    """_summary_

    This function will return a dictionary that contains a colour picker.
    
    Args:
        title (str): The title for the colour picker.
        master (object): The name of the master that the colour picker will belong to.
        title_row (int): The row number for the title.
        title_column (int): The column number for the title.
        colour_picker_row (int): The row number for the colour picker.
        colour_picker_column (int): The column number for the colour picker.
        default_colour (str): The default / starting colour that is applied to the colour picker.
        sticky (str, optional): The position that the colour picker will align to. Defaults to "nsew".

    Returns:
        dict: A dictionary containing all of the objects generated in this function.
    """
    
    colour_picker_title = CTkLabel(text = title, master = master, font=("", 16))
    colour_picker_title.grid(row = title_row, column = title_column, sticky = sticky, 
                             columnspan = 2, pady = (5, 5))

    colour_picker = CTkColorPicker(master = master, initial_color = default_colour)
    colour_picker.grid(row = colour_picker_row, column = colour_picker_column, 
                       columnspan=2, padx = 10, pady = 5, sticky = sticky)
    
    # --- Create an empty dictionary:
    elements = dict()
    
    # --- Add the title and picker to the elements dictionary:
    elements["colour_picker_title"] = colour_picker_title
    elements["colour_picker"] = colour_picker
    
    return elements