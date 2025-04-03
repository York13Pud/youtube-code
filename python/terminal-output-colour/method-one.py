# --- Method One: Built-In:

# Link to colour and style numbers:
# https://ozzmaker.com/add-colour-to-text-in-python/#:~:text=To%20make%20some%20of%20your,right%20into%20the%20print%20statement.&text=1%20%3D%20Style%2C%201%20for%20normal.


# --- Display a line of text using the terminal default settings:
print("This is coloured and styled with the default settings for the terminal\n")

# --- Display a line of text with green text and a black background:
print("\033[1;32;40m\
Bold (1) green (32) text on a black background(40m)\
\033[0;30;40m\n")

# --- Note: The colour and style will persist until it is changed.
# --- If you want it to go back to normal, you will need to change it to match
# --- the colour settings of your terminal theme.


# --- Display an underlined line of text with cyan text and a black background:
print("\033[4;36;40m\
Normal, underlined (4) cyan text (36) on a black background (40m)\
\033[0;30;40m\n")


# --- Display a line of bold, underlined text in red with a white background:
print("\033[1;31;47m\
Bold, underlined red text on a white background")

# Note: Cannot do bold and underlined together with this method. 
# Have a look at methods two and three.


# --- Reset the terminal to white text with a black background.
# --- Mostly applies if you don't have a theme applied to your
# --- terminal or PowerShell prompt:

print("\033[0;37;40m")