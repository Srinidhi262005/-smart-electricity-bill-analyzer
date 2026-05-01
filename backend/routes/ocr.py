from flask import Blueprint, request, jsonify
from services.ocr_service import extract_text_from_path, extract_meter_reading, save_upload

ocr_bp = Blueprint('ocr', __name__)


@ocr_bp.route('/ocr', methods=['POST'])
def ocr():
    """Extract meter reading text from an uploaded image."""
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    try:
        image_path = save_upload(file)
        extracted_text = extract_text_from_path(image_path)
        meter_value = extract_meter_reading(image_path)
        return jsonify({'success': True, 'text': extracted_text, 'meter_reading': meter_value})
    except ValueError as exc:
        return jsonify({'error': str(exc)}), 400
    except Exception:
        return jsonify({'error': 'OCR extraction failed'}), 500
