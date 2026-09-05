import cv2 
import numpy as np

def apply_filter(image, filter_type):
    """""Apply a filter to the image based on the filter type"""
    img=image.copy()

    if filter_type == 'red tint':
        img[:,:,1]=img[:,:,0]=0

    elif filter_type == 'green tint':
        img[:,:,0]=img[:,:,2]=0

    elif filter_type == 'blue tint':
        img[:,:,1]=img[:,:,2]=0

    elif filter_type == 'sobel':
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        sx=cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=3)    
        sy=cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=3)
        sob=cv2.bitwise_or(sx.astype(np.uint8),sy.astype(np.uint8))
        img=cv2.cvtColor(sob,cv2.COLOR_GRAY2BGR)

    elif filter_type == 'canny':
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        canny=cv2.Canny(gray,100,200)
        img=cv2.cvtColor(canny,cv2.COLOR_GRAY2BGR)

    elif filter_type == 'cartoon':
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        gray=cv2.medianBlur(gray,5)
        edges=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)
        color=cv2.bilateralFilter(img,9,250,250)
        img=cv2.bitwise_and(color,color,mask=edges)
    return img

def main():
    cap=cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error! Camera is not found")
        return
    filter_type='original'
    print("Keys: r=red tint , g=green tint , b=blue tint , s=sobel , c=canny , t=cartoon , o=original , q=quit")
    while True:
        ret,frame=cap.read()
        if not ret:
            print("Can't receive frame ")       
            break        
        out=apply_filter(frame,filter_type)
        cv2.imshow("Filtered Video",out)
        key=cv2.waitKey(1) & 0xFF
        if key==ord('r'):
            filter_type='red tint'
        elif key==ord('g'):
            filter_type='green tint'
        elif key==ord('b'):
            filter_type='blue tint'
        elif key==ord('s'):
            filter_type='sobel'
        elif key==ord('c'):
            filter_type='canny'
        elif key==ord('t'):
            filter_type='cartoon'
        elif key==ord('o'):
            filter_type='original'
        elif key==ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__== "__main__":
    main()    