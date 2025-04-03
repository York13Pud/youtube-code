# --- Import required libraries / modules:
from colored import cprint, Style          # https://pypi.org/project/colored/


# --- Display a line of text with green text and a black background:
cprint(text = "Bold green text on a black background\n",
       fore_rgb = (0, 255, 0), back_rgb = (0, 0, 0), 
       formatting = "bold")

# --- Note: The style resets automatically:
print("Hello\n")


# --- Display an underlined line of text with cyan text and a black background:
cprint(text = "Normal, underlined cyan text on a black background\n",
       fore_rgb = (0, 255, 255), back_rgb = (0, 0, 0), 
       formatting = "underline")


# --- Display a line of bold, underlined text in red with a white background:
cprint(text = f"{Style.bold}Bold, underlined red text on a white background",
       fore_rgb = (255, 0, 0), back_rgb = (255, 255, 255), 
       formatting = "underline")