from cv2 import *

if __name__ == "__main__":

    cam = VideoCapture(0)
    success, img = cam.read()

    if success:
        imshow("cam-test",img)
        waitKey(0)
        destroyWindow("cam-test")
        imwrite("filename.jpg",img) #save image

