from PIL import Image

# Specify file paths using double backslashes or a raw string
original_image = Image.open("C:/Users/SHAKIRA/Pictures/yoh.jpeg")

# Save the compressed image
original_image.save("yoh.jpeg", "JPEG", quality=20)

# Open the compressed image
compressed_image = Image.open("yoh.jpeg")

# Display the original and compressed images
original_image.show()
compressed_image.show()
