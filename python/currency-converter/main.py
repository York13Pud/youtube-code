# --- Import the required libraries / modules:
from customtkinter import *
from PIL import ImageTk
from tkinter import messagebox

from modules.env.env_vars import load_env_vars
from modules.currency.currency_list import currencies
from modules.currency.convert import convert_currency, check_value_is_numeric
from modules.image_check.image_check import check_image_present

import os


def main() -> None:
    """_summary_
    This is the main function for the application
    """
    
    # --- Load the environment variables:
    load_env_vars()
    
    # --- Get the absolute path for main.py:
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__)))

    # --- Check to see if the icon image is present and apply it if so:
    icon_check = check_image_present(image_path = f"{BASE_DIR}/images/icon.png", 
                                     error_message = f"Check that the icon file exists in that directory with the name icon.png.\n\nPress Ok to close.")
    
    header_check = check_image_present(image_path = f"{BASE_DIR}/images/header.png", 
                                       error_message = f"Check that the header image file exists in that directory with the name icon.png.\n\nPress Ok to close.")
    
    # --- Set the name and defaults for the app:
    app_name: str = "Currency Converter"
    default_font_size: int = 24
    
    # --- Setup the application and window:
    app = CTk()
    app.title(app_name)
    app.geometry(geometry_string = "450x840")
    app.resizable(width = False, height = False)

    # --- Set the icon for the app:    
    icon = ImageTk.PhotoImage(icon_check)
    app.wm_iconphoto(True, icon)
    
    # --- Set icon for Windows 10 / 11:
    app.wm_iconbitmap()
    
    # --- Define the variables to store the combo boxes values:
    from_currency: StringVar = StringVar()
    to_currency: StringVar = StringVar()
    
    # --- Build the UI --- #
    
    # --- 1. The header for the app with the name:
    header_image = CTkImage(light_image = header_check, 
                            dark_image = header_check, 
                            size = (450, 160))
    
    header_label = CTkLabel(master = app, width = 450, height = 160, 
                            text = app_name, font=("", 38),image = header_image,
                            text_color = "white")
    header_label.grid(row = 0, column = 0)
    
        
    # --- 2. The frame and entry box for the value to convert:
    value_frame = CTkFrame(master = app, width = 400, height = 150)
    value_frame.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = "nesw")
    
    value_label = CTkLabel(text = "Convert:", master = value_frame, width = 413, 
                           font=("", default_font_size), anchor = "w")
    value_label.grid(row = 0, column = 0, padx = 10, pady = 10)
    
    value_entry = CTkEntry(master = value_frame, width = 413, 
                           placeholder_text = "Enter a number to convert", 
                           font=("", default_font_size), justify = CENTER)
    value_entry.grid(row = 1, column = 0, padx = 10, pady = 5)
        
    
    # --- 3. The frame and combo box for the currency to convert from:
    convert_from_frame = CTkFrame(master = app)
    convert_from_frame.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = "nesw")    
    
    from_currency_label = CTkLabel(text = "From:", master = convert_from_frame, width = 413, 
                                   font=("", default_font_size), anchor = "w")
    from_currency_label.grid(row = 0, column = 0, padx = 10, pady = 10)
    
    from_currency_code = CTkComboBox(master = convert_from_frame, width = 413, values = currencies, 
                                     font=("", default_font_size), justify = LEFT, 
                                     variable = from_currency, state = "readonly")
    from_currency_code.grid(row = 1, column = 0, padx = 10, pady = 5)       
    from_currency_code.set(currencies[0])
    
    
    # --- 4. The frame and combo box for the currency to convert to:
    convert_to_frame = CTkFrame(master = app)
    convert_to_frame.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = "nesw")
    
    to_currency_label = CTkLabel(text = "To:", master = convert_to_frame, width = 413, 
                                 font=("", default_font_size), anchor = "w")
    to_currency_label.grid(row = 0, column = 0, padx = 10, pady = 10)
        
    to_currency_code = CTkComboBox(master = convert_to_frame, width = 413, values = currencies, 
                                   font=("", default_font_size), justify = LEFT, 
                                   variable = to_currency, state = "readonly")
    to_currency_code.grid(row = 1, column = 0, padx = 10, pady = 5)
    to_currency_code.set(currencies[1])


    # --- 5. The frame and label for the converted amount to be shown in. No value initially is shown:
    to_currency_value = CTkLabel(master = app, width = 413, height = 260, 
                                 text = "The converted amount\nwill be shown here.", 
                                 font=("", default_font_size), justify = CENTER)
    to_currency_value.grid(row = 4, column = 0, padx = 10, pady = 5)


    # --- 6a. The function that is used by the convert button to perform the currency conversion:
    def convert_currency_button_command() -> None:
        """_summary_
        This function will check that the value to convert is valid (numeric and > 0). If so, it will then convert it.
        
        Raises:
            Exception: If a boolean is returned, an error message will be shown indicating that the value entered is not valid.
        """
        
        # --- 1. Check that the from and to currencies are not the same:
        if from_currency.get() == to_currency.get():
            messagebox.showinfo("Info", f"Both the from and to currencies are the same. Please specify a different one for one of the two currencies.")
            raise Exception()
        
        # --- 2. Check that the value is numeric:
        convert_from_value = check_value_is_numeric(value = value_entry.get())
        
        if convert_from_value == False:
            messagebox.showerror("Error", f"Please check the value you entered is a number and it is higher than 0.")
            raise Exception()
        
        # --- 3. If so, perform conversion:
        converted_value = convert_currency(from_currency = str(from_currency.get()), 
                                           to_currency = str(to_currency.get()), 
                                           value = convert_from_value)
        
        # --- 4. Update the to_currency_value label with the original and converted currencies:
        to_currency_value.configure(text = f'{convert_from_value} {str(from_currency.get()).split(sep = " ")[0]}\n=\n{converted_value} {str(to_currency.get()).split(sep = " ")[0]}')
    
        
    # --- 6b. The button to execute the conversion and update the to_currency_value label:
    convert_button = CTkButton(master = app, text = "Convert", font=("", default_font_size), 
                               fg_color="green", hover_color=("#38B215"), 
                               height = 50, command = convert_currency_button_command)
    convert_button.grid(row = 5, column = 0, padx = 10, pady = 10, sticky = "nesw")


    # --- Keep the window active until it is closed:
    app.mainloop()


if __name__ == "__main__":    
    main()