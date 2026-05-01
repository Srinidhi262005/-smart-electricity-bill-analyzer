from models.ml_model import load_model, predict_bill as predict_bill_from_model

# Load model once to keep prediction fast and consistent.
_model = load_model()


def predict_bill(units):
    """Predict the bill for a given unit consumption."""
    return predict_bill_from_model(units, _model)


def predict_with_range(units):
    """Provide a bill estimate range around the base prediction."""
    base = predict_bill(units)
    return {
        'estimate': base,
        'low': round(max(base - 10, 0), 2),
        'high': round(base + 15, 2)
    }
