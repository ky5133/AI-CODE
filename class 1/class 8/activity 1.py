import cv2
import matplotlib.pyplot as plt
image=cv2.imread(r"C:/Users/Dinesh Bachani/Downloads/download.jpg")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title("RGB Image")
plt.show()
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image,cmap='gray')
plt.title("RGB Image")
plt.show()
cropped_image=image[100:120,100:120]
cropped_rgb = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
plt.imshow(cropped_rgb)
plt.title("Cropped Region")
plt.show()