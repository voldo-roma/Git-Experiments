# Import the Processing library
from random import random

def setup():
    size(400, 400)  # Set the canvas size

def draw():
    # Set a random background color
    background(random()*255, random()*255, random()*255)
    
    # Generate and draw circles
    noFill()
    stroke(random()*255, random()*255, random()*255)
    strokeWeight(2)
    ellipse(random(width), random(height), 50, 50)

def keyPressed():
    if key == 's' or key == 'S':
        # Save a screenshot when 'S' is pressed
        save("generative_art.png")
