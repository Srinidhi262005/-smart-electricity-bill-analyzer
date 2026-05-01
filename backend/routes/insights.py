from flask import Blueprint, request, jsonify
from services.suggestion_service import generate_suggestions
from services.anomaly_service import detect_abnormal_usage
from services.database_service import save_insight_log, get_user_history

insights_bp = Blueprint('insights', __name__)


def parse_history(history_input):
    if history_input is None:
        return []

    if isinstance(history_input, str):
        return [float(value.strip()) for value in history_input.split(',') if value.strip()]

    if isinstance(history_input, list):
        return [float(value) for value in history_input if value is not None]

    return []


@insights_bp.route('/usage/analyze', methods=['POST'])
def analyze_usage():
    """Analyze recent usage history and detect anomalies."""
    payload = request.get_json(force=True)
    history = parse_history(payload.get('history'))

    if not history:
        return jsonify({'error': 'History is required for usage analysis.'}), 400

    try:
        anomaly_report = detect_abnormal_usage(history)
        return jsonify({'success': True, 'anomaly_report': anomaly_report})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@insights_bp.route('/suggestions', methods=['GET'])
def suggestions():
    """Provide usage-based bill reduction suggestions."""
    units = request.args.get('units', type=float)
    history_string = request.args.get('history', '')
    user_id = request.args.get('user_id', type=int, default=1)

    if units is None:
        return jsonify({'error': 'Query parameter units is required.'}), 400

    try:
        history = parse_history(history_string)
        anomaly_report = detect_abnormal_usage(history)
        suggestions = generate_suggestions(units, anomaly_report)

        # Save insights to database for later review
        for suggestion in suggestions:
            save_insight_log(user_id, suggestion)

        return jsonify({'success': True, 'suggestions': suggestions, 'anomaly_report': anomaly_report})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@insights_bp.route('/insights', methods=['GET'])
def insights():
    """Legacy alias for suggestions endpoint."""
    return suggestions()


@insights_bp.route('/history/<int:user_id>', methods=['GET'])
def get_history(user_id):
    """Get usage history for a user."""
    try:
        history_records = get_user_history(user_id)
        history_data = [{
            'id': record.id,
            'units': record.units,
            'predicted_bill': record.predicted_bill,
            'date': record.date.isoformat()
        } for record in history_records]

        return jsonify({'success': True, 'history': history_data})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
