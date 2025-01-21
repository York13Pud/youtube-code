from customtkinter import *
from CTkColorPicker import *
from PIL import Image
import shutil


from modules.qr_code import generate_qr_code

import tkinter


def url_check() -> None:
    print("Hello")


# --- Setup the application and window:
app = CTk()
app._set_appearance_mode("dark")
app.title("QR Code Generator")
app.geometry(geometry_string = "1255x900")
app.resizable(width = False, height = False)


qr_code_frame = CTkFrame(master = app, width=900)
qr_code_frame.grid(row = 0, column = 1, padx = (0,5), pady = 10, sticky = "nesw")


# --- Define the sidebar that contains all the adjustable settings:
sidebar = CTkFrame(master = app)
sidebar.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "nesw")


# --- URL Entry and checker:
url_frame_title = CTkLabel(text = "Enter Your Text / URL", master = sidebar, font=("", 16))
url_frame_title.grid(row = 0, column = 0, sticky="nsew", columnspan = 2, pady = (10, 0))

url_frame = CTkFrame(master = sidebar)
url_frame.grid(row = 1, column = 0, padx = 10, pady = 10)

url_label = CTkLabel(text = "URL:", master = url_frame, font=("", 16))
url_label.grid(row = 0, column = 0, padx = 10, pady = 10)

url_text = CTkEntry(master = url_frame, width = 230, placeholder_text = "Enter a valid URL", font=("", 16))
url_text.grid(row = 0, column = 1, padx = 10, pady = 10)

# check_url = CTkButton(master = url_frame, text = "Check URL", command = url_check, hover=False, font=("", 16))
# check_url.grid(row = 1, column = 1, padx = 10, pady = 10, sticky = "e")


# --- QR code box size:
qr_code_size_title = CTkLabel(text = "QR Code Box Size", master = sidebar, font=("", 16))
qr_code_size_title.grid(row = 2, column = 0, sticky="nsew", columnspan = 2, pady = (10, 10))

qr_code_size_frame = CTkFrame(master = sidebar)
qr_code_size_frame.grid(row = 3, column = 0, padx = 10, pady = 10, columnspan = 2)

min_steps: int = 4
max_steps: int = 20

qr_code_size_value = tkinter.IntVar()

qr_code_size = CTkSlider(master = qr_code_size_frame, width = 260, from_ = min_steps, to = max_steps, 
                         #command = lambda e: print(int(e)), number_of_steps = (max_steps - min_steps), 
                         variable = qr_code_size_value)

qr_code_size.set(10)
qr_code_size.grid(row = 0, column = 0, padx = 10, pady = 10)

print(int(qr_code_size.get()))

qr_code_size_value_label = CTkLabel(textvariable = qr_code_size_value, master = qr_code_size_frame, font=("", 16), width = 10)
qr_code_size_value_label.grid(row = 0, column = 1, sticky="nsew", columnspan = 2, padx = (0, 5))


# --- QR code foreground colour:
qr_code_fg_colour_title = CTkLabel(text = "QR Code Foreground Colour", master = sidebar, font=("", 16))
qr_code_fg_colour_title.grid(row = 4, column = 0, sticky="nsew", columnspan = 2, pady = (10, 10))

qr_code_fg_colour = CTkColorPicker(master = sidebar, initial_color="#000000") #command = lambda e: print(e))
qr_code_fg_colour.grid(row = 5, column = 0, columnspan=2, padx = 10, pady = 10, sticky = "nesw")


# --- QR code background colour:
qr_code_bg_colour_title = CTkLabel(text = "QR Code Background Colour", master = sidebar, font=("", 16))
qr_code_bg_colour_title.grid(row = 6, column = 0, sticky="nsew", columnspan = 2, pady = (10, 10))

qr_code_bg_colour = CTkColorPicker(master = sidebar, initial_color="#FFFFFF")
                                #    command = lambda e: print(e, tuple(qr_code_bg_colour.rgb_color))
qr_code_bg_colour.grid(row = 7, column = 0, columnspan=2, padx = 10, pady = 10, sticky = "nesw")






#preview_image_path = "images/placeholder.png"
preview_image_path = Image.open("images/placeholder.png")

preview_image = CTkImage(
    dark_image = preview_image_path,
    #light_image = preview_image_path,
    size = (preview_image_path.width,preview_image_path.height)
)

preview_area = CTkLabel(master = qr_code_frame, image = preview_image, text="")


def update_image():
    new_image = generate_qr_code(url = url_text.get(), box = int(qr_code_size.get()),
                                 fg_colour = tuple(qr_code_fg_colour.rgb_color), 
                                 bg_colour = tuple(qr_code_bg_colour.rgb_color))
    
    print(new_image.get_image().height)
    
    preview_image.configure(
        #light_image = new_image.get_image(),
        dark_image = new_image.get_image(),
        size = (new_image.get_image().width, new_image.get_image().height)
    )
    
    
# --- QR code preview button:
preview_qr_code = CTkButton(master = sidebar, text = "Preview", hover=False, font=("", 16),
                            command =  update_image #lambda: preview_image.configure(
                                                                    # dark_image = generate_qr_code(url = url_text.get(), box = int(qr_code_size.get()),
                                                                    #                fg_colour = tuple(qr_code_fg_colour.rgb_color), 
                                                                    #                bg_colour = tuple(qr_code_bg_colour.rgb_color)).get_image(),
                                                                    #  size = (600,600)
                                                                    #   light_image = generate_qr_code(url = url_text, box = int(qr_code_size.get()),
                                                                    #                fg_colour = tuple(qr_code_fg_colour.rgb_color), 
                                                                    #                bg_colour = tuple(qr_code_bg_colour.rgb_color)).get_image(),
                                                                                   
                                                                  )

                            


preview_qr_code.grid(row = 8, column = 0, padx = 10, pady = 10, sticky = "w")





def save_image() -> None:
    save_image = preview_image._dark_image
    save_image.save("images/test.png")
    


# --- QR code save button:
save_qr_code = CTkButton(master = sidebar, text = "Save", command = save_image, hover=False, font=("", 16))
save_qr_code.grid(row = 8, column = 0, padx = 10, pady = 10, sticky = "e")


# --- QR Code preview area:
# qr_code_frame = CTkFrame(master = app, width=900)
# qr_code_frame.grid(row = 0, column = 1, padx = (0,5), pady = 10, sticky = "nesw")



# preview_image = CTkImage(light_image = Image.open("images/placeholder.png"),
#                          dark_image = Image.open("images/placeholder.png"), 
#                          size = (400,400))


# preview_area = CTkLabel(master = qr_code_frame, image = preview_image, text="")
preview_area.grid(row = 0, column = 0, padx = 10, pady = 10)
preview_area.place(x = 450, y = 450, anchor = tkinter.CENTER)


# --- Keep the window active until it is closed:
app.mainloop()


