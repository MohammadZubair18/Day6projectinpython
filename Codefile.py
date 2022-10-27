import random
from sty import fg
#To run this code in your compiler,Please install package "STY"
#https://pypi.org/project/sty/#files(read this)

def generateRGB():
    red = random.randint(0,256)
    green = random.randint(0,256)
    blue = random.randint(0,256)
    return red, green, blue

def generateColour(red, green, blue):
    return fg(red, green, blue)

red, green, blue = generateRGB()
colour = generateColour(red, green, blue)

print(colour, "I'm randomly changing colours muahahahahahaha!!", fg.rs)
