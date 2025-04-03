# --- Import required libraries / modules:
from colored import Back, Fore, Style       # https://pypi.org/project/colored/


# --- Define the colours and styles to use
text_colour_one: str = f"{Back.black}{Fore.green}{Style.bold}"
text_colour_two: str = f"{Back.black}{Fore.cyan}{Style.underline}"
text_colour_three: str = f"{Back.rgb(255, 255, 255)}{Fore.rgb(255, 0, 0)}{Style.bold}{Style.underline}"
# --- Note: You can use percentages for the rgb values:


# --- Display a line of text with green text and a black background:
print(f"{text_colour_one}Bold green text on a black background\n")
print("Hello\n")
print(f"Hello{Style.reset}\n")
print("Text is back to normal\n")


# --- Display an underlined line of text with cyan text and a black background:
print(f"{text_colour_two}Normal, underlined cyan text on a black background\n")


# --- Display a line of bold, underlined text in red with a white background:
print(f"{text_colour_three}Bold, underlined red text on a white background{Style.reset}\n")
