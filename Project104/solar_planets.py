import cv2

# Read the image file
img = cv2.imread("solar-system.jpg")

# Add text below each planet
font = cv2.FONT_HERSHEY_SIMPLEX
scale = 0.8
thickness = 2
color = (255, 255, 255)

# Add text for Mercury
cv2.putText(img, 'Mercury', (80, 130), font, scale, color, thickness, cv2.LINE_AA)

# Add text for Venus
cv2.putText(img, 'Venus', (280, 180), font, scale, color, thickness, cv2.LINE_AA)

# Add text for Earth
cv2.putText(img, 'Earth', (480, 230), font, scale, color, thickness, cv2.LINE_AA)

# Add text for Mars
cv2.putText(img, 'Mars', (600, 300), font, scale, color, thickness, cv2.LINE_AA)

# Add text for Jupiter
cv2.putText(img, 'Jupiter', (680, 400), font, scale, color, thickness, cv2.LINE_AA)

# Add text for Saturn
cv2.putText(img, 'Saturn', (720, 500), font, scale, color, thickness, cv2.LINE_AA)

# Add text for Uranus
cv2.putText(img, 'Uranus', (690, 600), font, scale, color, thickness, cv2.LINE_AA)

# Add text for Neptune
cv2.putText(img, 'Neptune', (660, 680), font, scale, color, thickness, cv2.LINE_AA)

# Display the image
cv2.imshow("output", img)
cv2.waitKey(0)

# Save the final image
cv2.imwrite("Solar_systemwithname.jpg", img)
