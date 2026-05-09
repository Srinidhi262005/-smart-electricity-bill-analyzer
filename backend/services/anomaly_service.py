import numpy as np
from typing import List, Dict, Any


# Constants for statistical thresholds
Z_SCORE_THRESHOLD = 2.0
SPIKE_RATIO_THRESHOLD = 1.3

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
    
    # Avoid division by zero for new or flat-usage accounts
    divisor = mean if mean > 0 else 1.0
    ratio = last / divisor
    anomalies = []

    # 1. Statistical Spike Detection (Z-Score approximation)
    if std > 0 and last > (mean + Z_SCORE_THRESHOLD * std) and ratio >= SPIKE_RATIO_THRESHOLD:
        anomalies.append('Significant usage spike detected (statistically outside normal variance).')
    
    # 2. Trend Analysis
    if len(values) >= 3 and values[-1] > values[-2] and values[-2] > values[-3]:
        anomalies.append('Three consecutive monthly increases detected; potential appliance inefficiency.')
    elif last > mean * 1.5:
        anomalies.append('Current month consumption is >50% higher than your historical average.')

    return {
        'abnormal': bool(anomalies),
        'mean': round(mean, 2),
        'std': round(std, 2),
        'latest': round(last, 2),
        'pattern': anomalies if anomalies else ['Usage pattern remains within normal range.']
    }
