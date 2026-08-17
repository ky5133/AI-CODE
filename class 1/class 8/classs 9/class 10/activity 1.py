import cv2
import numpy as np
import matplotlib.pyplot as plt


def display_image(image, title="Image"):
    """Utility function to display an image using matplotlib"""
    plt.figure(figsize=(10, 10))
    if len(image.shape) == 2:
        plt.imshow(image, cmap='gray')
    else:
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()


def interactive_edge_detection(image_path):
    """Interactive edge detection using various algorithms with a menu"""
    image = cv2.imread(image_path)
    if image is None:
        print("Image not found")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    display_image(gray, "Original Grayscale Image")

    print("Select an option")
    print("1. Sobel Edge Detection")
    print("2. Canny Edge Detection")
    print("3. Laplacian Edge Detection")
    print("4. Gaussian Smoothing")
    print("5. Median Smoothing")
    print("6. Exit")

    while True:
        choice = input("Enter your choice (1-6): ")

        if not choice.isdigit():
            print("Invalid choice. Please enter a number (1-6).")
            continue

        choice = int(choice)

        if choice == 1:
            # Sobel Edge Detection
            sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
            sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
            combined_sobel = cv2.bitwise_or(
                np.uint8(np.absolute(sobel_x)),
                np.uint8(np.absolute(sobel_y))
            )
            display_image(combined_sobel, "Sobel Edge Detection")

        elif choice == 2:
            print("Adjust the thresholds for Canny edge (default: 100, 200)")
            lower_thresh = int(input("Enter lower threshold: "))
            upper_thresh = int(input("Enter upper threshold: "))
            canny_edges = cv2.Canny(gray, lower_thresh, upper_thresh)
            display_image(canny_edges, "Canny Edge Detection")

        elif choice == 3:
            # Laplacian Edge Detection
            laplacian = cv2.Laplacian(gray, cv2.CV_64F)
            display_image(np.uint8(np.absolute(laplacian)), "Laplacian Edge Detection")

        elif choice == 4:
            # Gaussian Smoothing
            print("Adjust Gaussian kernel size (must be odd, default: 5)")
            kernel_size = int(input("Enter kernel size: "))
            if kernel_size % 2 == 0:
                print("Kernel size must be odd. Adding 1.")
                kernel_size += 1
            blurred = cv2.GaussianBlur(gray, (kernel_size, kernel_size), 0)
            display_image(blurred, "Gaussian Smoothed Image")

        elif choice == 5:
            # Median Smoothing
            print("Adjust Median kernel size (must be odd, default: 5)")
            kernel_size = int(input("Enter kernel size: "))
            if kernel_size % 2 == 0:
                print("Kernel size must be odd. Adding 1.")
                kernel_size += 1
            median = cv2.medianBlur(gray, kernel_size)
            display_image(median, "Median Smoothed Image")

        elif choice == 6:
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select a valid option (1-6).")


if __name__ == "__main__":
    interactive_edge_detection(r"C:/Users/Dinesh Bachani/Desktop/kky code/images (2).jpg")