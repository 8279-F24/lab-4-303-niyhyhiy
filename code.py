import time
from adafruit_circuitplayground import cp

cp.pixels.auto_write = False
cp.pixels.brightness = 0.3

restart = 0
try:
    while restart != 'q':
        
        colorOption = int(input("Please enter a number:  red color (option 1), the green color (option 2), or the blue color (option 3)"))
        max = 255
        while max > 0:
            if colorOption == 1:
                for i in range(10):
                    cp.pixels[i] = (max, 0, 0) 
            elif colorOption == 2:
                for i in range(10):
                    cp.pixels[i] = (0, max, 0)
            elif colorOption == 3:
                for i in range(10):
                    cp.pixels[i] = (0, 0, max)
            else:
                print("Number out of range.")
            cp.pixels.show()
            time.sleep(0.3)
            max = max - 1
        
        restart = input("Press 'q' to exit, any other to continue.")

except ValueError:
    print("Not a valid number.")