# importing the module
import cv2
import os
import csv
import numpy as np
import pandas as pd
import pandas
emptylist= []

def list_df(l):
    d1={}
    s1 = 'c'
    s2 = list(np.arange(len(l)//2))
    s = []
    for i in range(len(s2)):
        s.append(s1 + str(s2[i]))
        if i%2==0:
            d1[s[i]] =  l[0:3:2]
            for i in d1.values():
                for j in i:
                    if j in l:
                        l.remove(j)
        else:
            d1[s[i]] = l[0:2]
            for i in d1.values():
                for j in i:
                    if j in l:
                        l.remove(j)
    df = pd.DataFrame(data=d1)
    print(df)
    np.savetxt("file_name.csv", df, delimiter=",", fmt='%s')
    data = emptylist
        out = csv.writer(open("datapoint.csv","w"), delimiter=',',quoting=csv.QUOTE_ALL)
        out.writerow(data)
    return df


def click_event(event, x, y, flags, params):

    if event == cv2.EVENT_LBUTTONDOWN:
        emptylist.append(x)
        emptylist.append(y)
        list_df(emptylist)
        #np.savetxt("file_name.csv", list_df.df, delimiter=",", fmt='%s')
        
        
        
    
        
                
       #print(x, ' ', y)
        

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
        

        cv2.waitKey(100000)
        
   
	
