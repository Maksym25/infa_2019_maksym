from graph import *

penColor("black")
brushColor("yellow")
circle(100,100, 50)

brushColor("black")
polygon([(50,55),(98,70),(95,75),(48,60),(50,55)])
polygon([(150,55),(105,70),(110,75),(150,60),(150,55)])

for eyes in range(2):
    if eyes == 0:
        eyesx = 80
    else:
        eyesx = 120
    brushColor("red")
    circle(eyesx,80,10)
    brushColor("black")
    circle(eyesx,80,5)


brushColor("black")
rectangle(80,120,120,130)

run()