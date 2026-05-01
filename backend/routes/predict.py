from flask import Blueprint, request, jsonify
from services.prediction_service import predict_with_range
from services.database_service import save_usage_history

predict_bp = Blueprint('predict', __name__)


@predict_bp.route('/predict', methods=['POST'])
def predict():
    """Predict the electricity bill from units consumed."""
    payload = request.get_json(force=True)
    units = payload.get('units')
    user_id = payload.get('user_id', 1)  # Default user for now

    if units is None:
        return jsonify({'error': 'Missing units field'}), 400

    try:
        prediction = predict_with_range(units)

        # Save to database
        save_usage_history(user_id, units, prediction['estimate'])

        return jsonify({'success': True, 'predicted_bill': prediction})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
