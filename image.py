# importing the module
import cv2
import os


def click_event(event, x, y, flags, params):


	if event == cv2.EVENT_LBUTTONDOWN:


		print(x, ' ', y)


		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(img, str(x) + ',' +
					str(y), (x,y), font,
					1, (255, 0, 0), 2)
		cv2.imshow('image', img)

	if event==cv2.EVENT_RBUTTONDOWN:


		print(x, ' ', y)

		font = cv2.FONT_HERSHEY_SIMPLEX
		b = img[y, x, 0]
		g = img[y, x, 1]
		r = img[y, x, 2]
		cv2.putText(img, str(b) + ',' +
					str(g) + ',' + str(r),
					(x,y), font, 1.0,
					(255, 255, 0), 2)
		cv2.imshow('image', img)


if __name__=="__main__":
    images = []
    folder = "/home/rohit/Desktop/opencvimagenotationtool/adv_project/wrapped_images"
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        cv2.imshow('image', img)
        cv2.setMouseCallback('image', click_event)
        cv2.waitKey(1000)

	