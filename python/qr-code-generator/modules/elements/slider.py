# --- Import required libraries / modules:
from customtkinter import CTk, CTkFrame, CTkLabel, CTkSlider
from tkinter import IntVar


def create_slider(title: str, master: CTk, title_row: int, title_column: int,
                  frame_row: int, frame_column: int,
                  slider_row: int, slider_column: int, default_value: int, slider_from: int, slider_to: int,
                  label_row: int, label_column: int, sticky: str = "nsew") -> dict:
    
    slider_title = CTkLabel(text = title, master = master, font = ("", 16))
    slider_title.grid(row = title_row, column = title_column, sticky = sticky, 
                      columnspan = 2, pady = (10, 10))

    slider_frame = CTkFrame(master = master)
    slider_frame.grid(row = frame_row, column = frame_column, padx = 10, pady = 10, columnspan = 2)

    slider_value = IntVar()

    slider = CTkSlider(master = slider_frame, width = 260, 
                       from_ = slider_from, to = slider_to, variable = slider_value)

    slider.set(default_value)

    slider.grid(row = slider_row, column = slider_column, padx = 10, pady = 10)

    slider_label = CTkLabel(textvariable = slider_value, 
                            master = slider_frame, font = ("", 16), width = 20)
    
    slider_label.grid(row = label_row, column = label_column, 
                      sticky = sticky, columnspan = 2, padx = (0, 5))
        
    elements = dict()
    
    elements["slider_title"] = slider_title
    elements["slider_frame"] = slider_frame
    elements["slider"] = slider
    elements["slider_label"] = slider_label
    
    return elements