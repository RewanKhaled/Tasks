"""
Image Editing with Pillow
This program:
- Loads an image from your PC.
- Sets the left quarter of the image to black.
- Saves the modified image back to your PC.
- Opens the saved image automatically.
"""

from PIL import Image
from tkinter import Tk, filedialog
import os  # To open the image after saving

Tk().withdraw()  # Hide main tkinter window

# Ask user to choose an image file
image_path = filedialog.askopenfilename(
    title="Select an image",
    filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")]
)

if image_path:  # If user selected a file
    img = Image.open(image_path)

    # Get image size
    width, height = img.size

    # Create a black rectangle for the left quarter
    for x in range(width // 4):
        for y in range(height):
            img.putpixel((x, y), (0, 0, 0))  # Black pixel

    # Save the edited image
    save_path = filedialog.asksaveasfilename(
        title="Save edited image",
        defaultextension=".jpg",
        filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png")]
    )
    if save_path:
        img.save(save_path)
        print("Image saved successfully at:", save_path)
        
        # Open the saved image
        os.startfile(save_path)
    else:
        print("Save canceled.")
else:
    print("No image selected.")
