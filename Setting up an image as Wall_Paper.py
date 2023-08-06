

import ctypes

def set_wallpaper(image_path):
    # Select the appropriate SPI constant for setting the desktop background
    SPI_SETDESKWALLPAPER = 0x0014

    # Call the SystemParametersInfo function from user32.dll
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)

# Specify the path to your image file
image_path = r"C:/Users/Jugal/Desktop/1 June 2023.jpg"

# Set the wallpaper using the specified image
set_wallpaper(image_path)