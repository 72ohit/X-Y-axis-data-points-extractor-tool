# importing the module
import cv2
import os
import csv
import numpy as np
import pandas as pd
import pandas
emptylist= []


def click_event(event, x, y, flags, params):

    if event == cv2.EVENT_LBUTTONDOWN:
       #print(x, ' ', y)
       #emptylist.append(x)
       #emptylist.append(y)
        mydict = []
        mydict = { "x":x,"y":y}
        df1 = pandas.DataFrame(mydict, index= range(1))
        print(df1)
        #print(df)
        #df.to_csv("/home/rohit/Desktop/opencvimagenotationtool/datapoint.csv", sep=',',index=False)
        #import numpy as np
        #np.savetxt("file_name.csv", emptylist, delimiter=",", fmt='%s')
        # out = csv.writer(open("datapoint.csv","w"), delimiter=',',quoting=csv.QUOTE_ALL)
        # out.writerow(df1) 
        
        # f  = open('datapoint.csv','wb')
        # w = csv.DictWriter(f,mydict.keys())
        # w.writerow(mydict)
        # f.close()
        # with open('datapoint.csv', 'w') as f:
        #     [f.writelines('{0},{1}\n'.format(key, value)) for key, value in mydict.items()] 

        
  
        coordinates = ['x', 'y']
  
        new_dict = [{'x': x, 'y': y}]
  
        with open('datapoint.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = coordinates)
            writer.writeheader()
            writer.writerows(new_dict)

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
   
	
