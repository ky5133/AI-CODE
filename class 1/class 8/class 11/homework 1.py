import cv2
import numpy as np

def apply_color_filter(image,filter_type):
    filtered_image = image.copy()
    if filter_type == 'red tint':
        filtered_image[:,:,1] = 0  # Set green channel to 0
        filtered_image[:,:,0] = 0  # Set blue channel to 0

    elif filter_type == 'blue tint':
        filtered_image[:,:,2] = 0  # Set red channel to 0
        filtered_image[:,:,1] = 0  # Set green channel to 0

    elif filter_type == 'green tint':
        filtered_image[:,:,2] = 0  # Set red channel to 0  
        filtered_image[:,:,0] = 0  # Set blue channel to 0

    elif filter_type == 'increase red':
        filtered_image[:,:,2] = np.clip(filtered_image[:,:,2] + 50)  # Increase red channel

    elif filter_type == 'decrease blue':
        filtered_image[:,:,0] = np.clip(filtered_image[:,:,0] - 50)  # Decrease blue channel

    return filtered_image

image_path = r"C:/Users/Dinesh Bachani/Desktop/kky code/pngtree-butterfly-png-image_121554.jpg"    
image = cv2.imread(image_path)

if image is None:
    print("Error! Image is not found")

else:
    filter_type = "original"

print("press the following keys to apply filters:")
print("r- Red Tint")
print("b- Blue Tint")
print("g- Green Tint")
print("i- Increase Red")
print("d- Decrease Blue")
print("q- Quit")

while True:
    filtered_image = apply_color_filter(image, filter_type)
    cv2.imshow("Filtered Image", filtered_image)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('r'):
        filter_type = 'red tint'
    elif key == ord('b'):
        filter_type = 'blue tint'
    elif key == ord('g'):
        filter_type = 'green tint'
    elif key == ord('i'):
        filter_type = 'increase red'
    elif key == ord('d'):
        filter_type = 'decrease blue'
    elif key == ord('q'):
        print("Exiting...... the program.")
        break
    else:
        print("Invalid key pressed. Please press a valid key r,b,g,i,d,q.")


cv2.destroyAllWindows()                            

        