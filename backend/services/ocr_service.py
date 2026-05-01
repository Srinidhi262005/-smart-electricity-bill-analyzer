import os
import re
import cv2
from PIL import Image
import pytesseract
from werkzeug.utils import secure_filename
from utils.config import Config

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'bmp', 'tiff'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def save_upload(file_storage):
    if not allowed_file(file_storage.filename):
        raise ValueError('Unsupported file type')

    os.makedirs(Config.OCR_UPLOAD_PATH, exist_ok=True)
    filename = secure_filename(file_storage.filename)
    path = os.path.join(Config.OCR_UPLOAD_PATH, filename)
    file_storage.save(path)
    return path


def extract_text_from_path(image_path):
    """Extract raw OCR text directly from an image path."""
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image, lang='eng')
    return text.strip()


def preprocess_image_for_ocr(image_path):
    """Preprocess image using OpenCV to improve OCR accuracy."""
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f'Unable to load image at {image_path}')

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 9, 75, 75)
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    cleaned = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=1)
    return cleaned


def extract_numeric_from_text(text):
    """Return only numeric characters from OCR output."""
    digits = re.findall(r'\d+', text or '')
    if not digits:
        return ''
    longest = max(digits, key=len)
    return longest


def extract_meter_reading(image_path):
    """Extract a numeric meter reading from an image file."""
    cleaned_image = preprocess_image_for_ocr(image_path)
    pil_image = Image.fromarray(cleaned_image)
    text = pytesseract.image_to_string(pil_image, lang='eng', config='--psm 6 digits')
    return extract_numeric_from_text(text)


def extract_text_from_image(file_storage):
    if not allowed_file(file_storage.filename):
        raise ValueError('Unsupported file type')

    path = save_upload(file_storage)
    return extract_text_from_path(path)
