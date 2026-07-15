import cv2
image=cv2.imread(r"C:/Users/Dinesh Bachani/Downloads/ChatGPT Image May 24, 2026, 11_25_19 AM.png")
cv2.namedWindow('Loaded Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Loaded Image',300,300)
cv2.imshow('Loaded Image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
