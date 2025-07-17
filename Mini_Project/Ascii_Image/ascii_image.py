import ascii_magic

# Create AsciiArt object from the image file
art = ascii_magic.AsciiArt.from_image("E:/faizan's pic/SKI03778.jpg")

# Display ASCII art in terminal with custom settings
art.to_terminal(columns=100, char="#")


