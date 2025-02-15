from translate import Translator
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

#     extracted_text = pytesseract.image_to_string(image_path)
#
#     print("Extracted Text:\n", extracted_text)
#
#     translator = Translator(to_lang="hi")
#     translation = translator.translate(extracted_text)
#     print("Translated Text:", translation)

if __name__ == '__main__':
    image_path = r'E:\img2txt\Images\image.png'
    img = Image.open(image_path)
    print(img.size)
    char_map = pytesseract.image_to_boxes(img, output_type=pytesseract.Output.DICT)
    chars = char_map["char"]
    left = char_map["left"]
    right = char_map["right"]


