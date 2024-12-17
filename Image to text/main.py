from translate import Translator

from PIL import Image
import pytesseract

# Set the path to the tesseract executable (update the path as per your system)
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

# Load the image
image_path = 'E:/Final Yr Project/Image to text/image.png'  # Replace with your image path
image = Image.open(image_path)

# Extract text from the image
extracted_text = pytesseract.image_to_string(image)

# Print the extracted text
print("Extracted Text:\n", extracted_text)

# Translate the extracted text
translator= Translator(to_lang="hi")
translation = translator.translate(extracted_text)
print("Translated Text:", translation)