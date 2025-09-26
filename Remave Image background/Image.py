from rembg import remove
from PIL import Image

# Correct file paths (no trailing space and different output file name)
input_path = 'images.png'
output_path = 'Image_output.png'

# Open input image
inp = Image.open(input_path)

# Remove background
output = remove(inp)

# Save the output
output.save(output_path)

# Open and display the result
Image.open(output_path).show()
