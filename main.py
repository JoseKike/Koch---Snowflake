from turtle import *


# funcion para crear el koch
def koch(largo, grado): 
    if grado == 0: 
        forward(largo)
        return


    largo /= 3.0
    koch(largo, grado-1)
    left(60)
    koch(largo, grado-1)
    right(120)
    koch(largo, grado-1)
    left(60)
    koch(largo, grado-1)

if __name__ == "__main__":
    speed(9999)

    length = 300.0
  
    penup()
  
    backward(length/2.0)
        
    pendown()
    for i in range(3):
        koch(length, 4)
        right(120)

    mainloop()