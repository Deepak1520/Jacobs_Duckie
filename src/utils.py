import pathlib
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def line_grid_detector(frame_shape, point):
    '''
    takes a frame and a center of a circle and determines in which 
    position of the grid the object is
    '''
    V = frame_shape[0]
    H = frame_shape[1]
    ww = H//3 
    vv = V//3
    x,y = point[0]
    if x < ww:
        if y < vv:
            return 1
        elif y >= vv and y < vv*2:
            return 4
        else:
            return 7
    elif x >= ww and x < ww*2:
        if y < vv:
            return 2
        elif y >= vv and y < vv*2:
            return 5
        else:
            return 8
    else:
        if y < vv:
            return 3
        elif y >= vv and y < vv*2:
            return 6
        else:
            return 9

def ht(img, threshold):
    """
    Performs hough transform with specified threshold
    """
    def houghline(image,thd):
    
        raw_img = cv.imread(img)
        noise_free_img=cv.medianBlur(raw_img,5)
        img=cv.cvtColor(noise_free_img,cv.COLOR_BGR2GRAY)
        plt.imshow(img)
        edges = cv.Canny(img,50,150,apertureSize=3)

        # Apply HoughLinesP method to
        # to directly obtain line end points
        lines_list =[]
        lines = cv.HoughLinesP(
                    edges, # Input edge image
                    1, # Distance resolution in pixels
                    np.pi/180, # Angle resolution in radians
                    threshold=100, # Min number of votes for valid line
                    minLineLength=90, # Min allowed length of line
                    maxLineGap=40 # Max allowed gap between line for joining them
                    )

        # Iterate over points
        for points in lines:
            # Extracted points nested in the list
            x1,y1,x2,y2=points[0]
            # Draw the lines joing the points
            # On the original image
            cv.line(image,(x1,y1),(x2,y2),(0,255,0),2)
            # Maintain a simples lookup list for points
            lines_list.append([(x1,y1),(x2,y2)])
            plt.imshow(image)
        
        return image,lines    

