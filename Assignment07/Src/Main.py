# Name:Anna Moorhead
# email: moorheaa@mail.uc.edu
# Assignment Number: Assignment 07
# Due Date: February 28, 2024
# Course/Section: IS 4010 - 001
# Semester/Year: Spring 2024
# Brief Description of the assignment: generating/ altering a Captcha function
# Citations:,
# Anything else that's relevant: 

from Src.Assignment07 import generate_captcha

result = generate_captcha()
myCaptcha = result[0]
captcha_string = result[1]
print(">" + captcha_string + "<")
myCaptcha.show()

