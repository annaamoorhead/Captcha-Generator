# Name:Anna Moorhead
# email: moorheaa@mail.uc.edu
# Assignment Number: Assignment 07
# Due Date: February 28, 2024
# Course/Section: IS 4010 - 001
# Semester/Year: Spring 2024
# Brief Description of the assignment: generating/ altering a Captcha function
# Citations:,
# Anything else that's relevant: 

import random
from PIL import Image, ImageFilter, ImageDraw, ImageFont

default_color_red = 228
default_color_green = 150
default_color_blue = 150

def generate_random_string(length):
    random_string = ""
    for i in range(0,length):
        random_string = random_string + random.choice('1234567890ABCDEFGHIJKLMNOPQRSTUVQXYZ')
    return random_string

def draw_random_ellipse(draw):
    # A random circle on the image
    a = random.randrange(10, 300, 1)
    b = random.randrange(10, 275, 1)
    c = a + random.randrange(10, 90, 1)
    d = b + random.randrange(10, 90, 1)
    draw.ellipse((a,b,c,d), fill=(default_color_red + random.randrange(-100,100,1), 
                                  default_color_green + random.randrange(-100,100,1), 
                                  default_color_blue + random.randrange(-100,100,1), 255), 
                                  outline = "black")

def generate_captcha():
    '''
    Generate a captcha
    :return: A tuple (image, captcha string encoded in the image)
    '''
    captcha_string = generate_random_string(6)
#   print(">" + captcha_string + "<")
    captcha_image = Image.new("RGBA", (400, 200), (default_color_red,default_color_green,default_color_blue))
    draw = ImageDraw.Draw(captcha_image, "RGBA")
    for i in range(1,20):
        draw_random_ellipse(draw)

    fontStyle = ImageFont.truetype("Aaargh.ttf", 48)     # font must be in the same folder as the .py file. 
    anotherFontStyle= ImageFont.truetype("BooksAndPens-1jGDZ.otf", 48)

    # Arbitrary starting co-ordinates for the text we will write
    x = 10 + random.randrange(0, 100, 1)
    y = 79 + random.randrange(-10, 10, 1)
    for letter in captcha_string:
#       print(letter)
        draw.text((x, y), letter, (0,0,0),font=fontStyle or anotherFontStyle)    # Write in black
        x = x + 35
        y = y +  random.randrange(-10, 10, 1)
    
    return (captcha_image, captcha_string)  # return a heterogeneous tuple
