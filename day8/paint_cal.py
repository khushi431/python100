# you are painting a wall

import math

def paint_calc(height , width , cover):
    area = height* width
    num_of_cans =math.ceil(area/cover)
    print(f"You will need {num_of_cans} cans of paint")

h = int(input("height: "))
w = int(input("width: "))
coverage = 5

paint_calc(height = h , width = w  , cover = coverage)

