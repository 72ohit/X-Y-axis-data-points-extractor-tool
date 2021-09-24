# importing the module
import cv2
import os
import csv
#import pandas 

def click_event(event, x, y, flags, params):
    emptylist= []

    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ' ', y)
        emptylist.append(x)
        emptylist.append(y)
        df = emptylist
        #df.to_csv("/home/rohit/Desktop/opencvimagenotationtool/datapoint.csv", sep=',',index=False)

        

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(x) + ',' + str(y), (x,y), font, 0.5, (255, 0, 0), 1)
        
        cv2.imshow('image', img)
        #print(emptylist)


    if event==cv2.EVENT_RBUTTONDOWN:
        #print(x, ' ', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        cv2.putText(img, str(b) + ',' + str(g) + ',' + str(r), (x,y), font, 1.0,(255, 255, 0), 2)
        cv2.imshow('image', img)


if __name__=="__main__":
    images = []
    folder = "/home/rohit/Desktop/opencvimagenotationtool/adv_project/frames"
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        cv2.imshow('image', img)
        cv2.setMouseCallback('image', click_event)

        cv2.waitKey(3000)
	