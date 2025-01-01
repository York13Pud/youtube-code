# --- Import required libraries / modules
import tkinter as tk
from tkinter.ttk import Label, Combobox, Entry, Button

def main() -> None:
    
    window = tk.Tk()
    window.title(string = "QR Code Generator")
    
    greeting_themed = Label(text="Hello, Tkinter")
    
    
    # --- Colour picker for the qr code background
    
    # --- Colour picker for the qr code foreground
    
    # --- Text box to put data into for the qr code
    qr_code_data = Entry()
    
    # --- Drop down list with box sizes
    qr_code_size = Combobox(values = ["One", "Two"])
    
    # --- Build the UI:
    greeting_themed.pack()
    qr_code_size.pack()
    qr_code_data.pack()
    
    window.mainloop()

if __name__ == "__main__":
    main()