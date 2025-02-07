# --- Import required libraries / modules:
from customtkinter import CTkFrame, CTkLabel, CTkSlider
from tkinter import IntVar


def create_slider(title: str, master: object, title_row: int, title_column: int,
                  frame_row: int, frame_column: int,
                  slider_row: int, slider_column: int, default_value: int, slider_from: int, slider_to: int,
                  label_row: int, label_column: int, sticky: str = "nsew") -> dict:
    """_summary_

    Args:
        title (str): The title for the slider.
        master (object): The name of the master that the sliders frame will belong to.
        title_row (int): The row number for the title.
        title_column (int): The column number for the title.
        frame_row (int): The row number for the frame.
        frame_column (int): The column number for the frame.
        slider_row (int): The row number for the slider.
        slider_column (int): The column number for the slider.
        default_value (int): The default / starting value for the slider.
        slider_from (int): The lowest value for the slider.
        slider_to (int): The highest value for the slider.
        label_row (int): The row number for the label with the current value.
        label_column (int): The column number for the label with the current value.
        sticky (str, optional): The position that the title and label will align to. Defaults to "nsew".

    Returns:
        dict: A dictionary containing all of the objects generated in this function.
    """
    
    
    slider_title = CTkLabel(text = title, master = master, font = ("", 16))
    slider_title.grid(row = title_row, column = title_column, sticky = sticky, 
                      columnspan = 2, pady = (10, 10))

    slider_frame = CTkFrame(master = master)
    slider_frame.grid(row = frame_row, column = frame_column, padx = 10, pady = 5, columnspan = 2)

    slider_value = IntVar()

    slider = CTkSlider(master = slider_frame, width = 260, 
                       from_ = slider_from, to = slider_to, variable = slider_value)

    slider.set(default_value)

    slider.grid(row = slider_row, column = slider_column, padx = 10, pady = 5)

    slider_label = CTkLabel(textvariable = slider_value, 
                            master = slider_frame, font = ("", 16), width = 20)
    
    slider_label.grid(row = label_row, column = label_column, 
                      sticky = sticky, columnspan = 2, padx = (0, 5))
    
    # --- Create an empty dictionary:
    elements = dict()
    
    # --- Add the title, frame, slider and slider label to the elements dictionary:
    elements["slider_title"] = slider_title
    elements["slider_frame"] = slider_frame
    elements["slider"] = slider
    elements["slider_label"] = slider_label
    
    return elements