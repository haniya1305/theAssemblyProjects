import random
import string
from tkinter import *
from captcha.image import ImageCaptcha
from PIL import ImageTk, Image

# Simple program to make a Captcha text image from user input
# img = ImageCaptcha(width = 300, height = 100)   # Create image window
# text = input("Enter the Text for Captcha: ")    # Ask user for Text for captcha
# Cap_data = img.generate(text)                   # Generate the image of the text
# img.write(text, 'Captcha1.png')                 # Save the image

# Simple program to make a Captcha text image using random
# image = ImageCaptcha(width = 300, height = 100)                 # Create image window
# characters = string.ascii_letters + string.digits               # Set of all alphabets and digits
# string1 = ''.join(random.choice(characters) for i in range(8))  # Generate random text
# Captcha_data = image.generate(string1)                          # Generate the image of the text
# image.write(string1, 'Captcha2.png')                            # Save the image

# Program to make a Captcha text image at random and then having the user verify

# Creating user interactive window
window = Tk()
window.title("Captcha Verification App")
window.geometry("500x300")

# Create captcha image
cap = ImageCaptcha(width=300, height=100)
characters = string.ascii_letters + string.digits
val = ''.join(random.choice(characters) for i in range(4))
print(val)
images = cap.generate_image(val)
images.show()
images.save("Final_Captcha.png")
# cap.write(val, 'Final_Captcha.png')

# Ask for input
label1 = Label(window, text="Enter Captcha: ")
label1.pack(pady=10)

# Receive Input from User
input1 = StringVar()
entry = Entry(window, textvariable=input1)
entry.pack(pady=10)

def check():
    if val == input1.get():
        final_output.config(text="Captcha verified successfully!")
    else:
        final_output.config(text="Captcha failed.")

# Button
click = Button(window, text="Verify", command=check, width=10)
click.pack(pady=10)

# Screen Label
final_output = Label(window, text="")
final_output.pack(pady=10)

window.mainloop()