import numpy as np
from typing import List, Dict, Any


def detect_abnormal_usage(history: List[float]) -> Dict[str, Any]:
    """
    Analyzes consumption history to detect statistical anomalies.
    
    Returns a dictionary containing the analysis results and descriptive patterns.
    """
    if not history or len(history) < 2:
        return {
            'abnormal': False, 
            'details': 'Insufficient data for anomaly detection (need at least 2 entries).'
        }

    values = np.array(history, dtype=float)
    mean = float(np.mean(values))
    std = float(np.std(values))
    last = float(values[-1])
    
    # Avoid division by zero
    divisor = mean if mean > 0 else 1.0
    ratio = last / divisor
    anomalies = []

    if last > mean + 1.5 * std and ratio >= 1.3:
        anomalies.append('Significant usage spike detected above typical baseline.')
    if len(values) >= 3 and values[-1] > values[-2] and values[-2] > values[-3]:
        anomalies.append('Three consecutive monthly increases detected; check for inefficient appliances.')
    elif last > mean * 1.5:
        anomalies.append('Current month consumption is 50% higher than your average.')

    return {
        'abnormal': bool(anomalies),
        'mean': round(mean, 2),
        'std': round(std, 2),
        'latest': round(last, 2),
        'pattern': anomalies if anomalies else ['Usage pattern remains within normal range.']
    }
