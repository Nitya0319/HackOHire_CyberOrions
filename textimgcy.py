import pytesseract
from PIL import Image

# Set the path to Tesseract executable (if not in your PATH environment variable)
# pytesseract.pytesseract.tesseract_cmd = r'<path_to_tesseract_executable>'

# Open the image
image = Image.open(r"C:\Users\nitya mohta\Downloads\img.jpg")

# Use pytesseract to extract text from the image
extracted_text = pytesseract.image_to_string(image)

# Print the extracted text
print(extracted_text)
