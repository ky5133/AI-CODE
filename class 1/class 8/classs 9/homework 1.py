import cv2
import matplotlib.pyplot as plt
image_path = (r"C:/Users/Dinesh Bachani/Desktop/kky code/images.png")
image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
height, width, _ = image_rgb.shape

rect1_width, rect1_height = 150, 150
top_left1=20,20
bottom_right1= top_left1[0] + rect1_width, top_left1[1] + rect1_height
cv2.rectangle(image_rgb, top_left1, bottom_right1, (255, 0, 0), 2)


rect2_width, rect2_height = 200, 150
top_left2= (width-rect2_width-20, height-rect2_height-20)
bottom_right2= (width-rect2_width, height-rect2_height-20)
cv2.rectangle(image_rgb, top_left2, bottom_right2, (255, 0, 255), 3)


center1x = top_left1[0]+rect1_width//2
center1y = top_left1[1]+rect1_height//2
center2x = top_left2[0]+rect2_width//2
center2y = top_left2[1]+rect2_height//2


cv2.circle(image_rgb,(center1x,center1y),5,(0,255,255),-1)
cv2.circle(image_rgb,(center2x,center2y),5,(255,0,255),-1)

cv2.line(image_rgb,(center1x,center1y),(center2x,center2y),(255,255,0),2)
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image_rgb,"Rectangle 1",(top_left1[0],top_left1[1]-10),font,0.5,(255,255,255),1)
cv2.putText(image_rgb,"Rectangle 2",(top_left2[0],top_left2[1]-10),font,0.5,(255,255,255),1)
cv2.putText(image_rgb,"Circle 1",(center1x+10,center1y),font,0.5,(255,255,150),1)
cv2.putText(image_rgb,"Circle 2",(center2x+10,center2y),font,0.5,(255,150,255),1)

arrow_start1 =(30,30)
arrow_end1=(50,50)
cv2.arrowedLine(image_rgb,arrow_start1,arrow_end1,(255,0,255),5,tipLength=0.5)

arrow_start2 =(10,10)
arrow_end2=(40,40)
cv2.arrowedLine(image_rgb,arrow_end2,arrow_start2,(255,0,255),5,tipLength=0.9)

plt.imshow(image_rgb)
plt.axis('off')
plt.title("Rectangles,circles and arrows")
plt.show()





