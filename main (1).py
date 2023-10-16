import cv2
import imutils
import numpy as np
from skimage.metrics import structural_similarity as ssim

# Load the two images
img1 = cv2.imread("sample_images/img_1_2.jpg")
img2 = cv2.imread("sample_images/img_1_1.jpg")

# Resize images if necessary
img1 = cv2.resize(img1, (700, 480))
img2 = cv2.resize(img2, (700, 480))

img_height = img1.shape[0]

# Grayscale
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

(similar, diff) = ssim(gray1, gray2, full=True)
print("Level of similarity : {}".format(similar))

diff = (diff * 255).astype("uint8")
cv2.imshow("Difference", diff)

# Apply threshold. Apply both THRESH_BINARY_INV and THRESH_OTSU
thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

# Create an image with saturated blue color
saturated_blue_image = np.zeros_like(img1)
saturated_blue_image[:, :, 0] = 255  # Set blue channel to 255 (full blue)
saturated_blue_image[:, :, 1] = 0    # Set green channel to 0
saturated_blue_image[:, :, 2] = 0    # Set red channel to 0

# Keep only the differences as red
saturated_blue_image[thresh > 0] = [0, 0, 255]  # Set red channel to 255 where differences are present

# Calculate contours
contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)

# Create a copy of the saturated blue image to draw contours on
contour_image = saturated_blue_image.copy()

# Draw contours on the image
cv2.drawContours(contour_image, contours, -1, (0, 0, 0), 1)  # Draw contours in black color

# Apply Canny edge detection
edges = cv2.Canny(gray1, 100, 200)  # Adjust the thresholds as needed

# Find and draw contours for edges
edge_contours = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
edge_contours = imutils.grab_contours(edge_contours)
cv2.drawContours(contour_image, edge_contours, -1, (0, 0, 0), 1)  # Draw edge contours in green color

# Convert the similarity score to a formatted string
score_text = f"Similarity Score: {similar:.2f}"

# Add the similarity score as text on the image
cv2.putText(contour_image, score_text, (10, img_height - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

# Show the modified image with saturated blue color and red differences
cv2.imshow("Saturated Blue with Red Differences", contour_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
