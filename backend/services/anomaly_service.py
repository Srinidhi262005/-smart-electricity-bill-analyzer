import numpy as np


def detect_abnormal_usage(history):
    if not history or len(history) < 2:
        return {'abnormal': False, 'details': 'History too short for anomaly detection.'}

    values = np.array(history, dtype=float)
    mean = float(np.mean(values))
    std = float(np.std(values))
    last = float(values[-1])
    ratio = last / max(mean, 1)
    anomalies = []

    if last > mean + 1.5 * std and ratio >= 1.3:
        anomalies.append('Recent usage spike above typical consumption.')
    if len(values) >= 3 and values[-1] > values[-2] and values[-2] > values[-3]:
        anomalies.append('Three consecutive increases suggest inefficient usage.')
    if last > mean * 1.5:
        anomalies.append('Current month is significantly above average consumption.')

    return {
        'abnormal': bool(anomalies),
        'mean': round(mean, 2),
        'std': round(std, 2),
        'latest': round(last, 2),
        'pattern': anomalies or ['Usage pattern looks normal.']
    }
