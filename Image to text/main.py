from translate import Translator
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

image_path = 'E:\img2txt\Image to text\Images\image.png'

extracted_text = pytesseract.image_to_string(image_path)

print("Extracted Text:\n", extracted_text)

translator= Translator(to_lang="hi")
translation = translator.translate(extracted_text)
print("Translated Text:", translation)