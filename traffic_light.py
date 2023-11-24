import cv2
import numpy as np
import time

# Create blank background image
img = np.zeros((700, 900, 3), np.uint8)

# Define traffic light colors
green = (0, 255, 0) 
yellow = (0, 255, 255)
red = (0, 0, 255)

red_us = (34, 34, 162)
yellow_us = (81, 165, 165)
green_us = (40, 151, 40)

# Initial color is green
color = green

# Set countdown timer
x = 5 #xanh
y = 3 #vang
z = x + y #do

cor_x = 250
cor_y = 570

timer = x

while True:
    # Draw colored circle for traffic light
    cv2.circle(img,(250, 130), 100, red_us, -1)
    cv2.circle(img,(250, 350), 100, yellow_us, -1)
    cv2.circle(img,(250, 570), 100, green, -1)
    
    # Display countdown text
    cv2.putText(img, str(timer), (cor_x, cor_y), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 3)
    
    # Display image
    cv2.imshow('Traffic light', img)
    
    # Count down each second 
    if timer > 0:
        timer -= 1
        time.sleep(1)
    
    # Change light color
    # if timer == 0 and color == green:
    #     timer = y
    #     yellow_us = yellow
    #     green = green_us
    #     cor_y = 350
    # elif timer == 0 and color == yellow:
    #     timer = z
    #     red_us = red
    #     yellow = yellow_us
    #     cor_y = 570
    # elif timer == 0 and color == red:
    #     timer = x
    #     red = red_us
    #     green_us = green
    #     cor_y = 130
        
    if timer == 0:
        if color == green: #yellow
            timer = y
            color = yellow
            yellow_us = yellow
            cor_y = 350
            green = green_us
        elif color == yellow: #red
            timer = z
            color = red
            red_us = red
            cor_y = 130
            yellow = yellow_us
        elif color == red: #green
            timer = x
            color = green
            green_us = green
            red = red_us
            cor_y = 570
            
    # Check for ESC key to exit
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cv2.destroyAllWindows()
