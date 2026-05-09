from datetime import datetime


def detect_intent(message):
    """Classifies user intent based on keyword matching."""
    text = message.strip().lower()
    if not text:
        return 'unknown'

    bill_keywords = ['bill', 'predict', 'units', 'amount', 'charge', 'estimate']
    usage_keywords = ['usage', 'abnormal', 'spike', 'history', 'consumption', 'pattern']
    saving_keywords = ['save', 'reduce', 'tips', 'cut', 'lower', 'efficiency', 'savings']

    if any(word in text for word in bill_keywords):
        return 'bill'
    if any(word in text for word in usage_keywords):
        return 'usage'
    if any(word in text for word in saving_keywords):
        return 'saving'
    if 'ocr' in text or 'image' in text or 'meter' in text or 'read' in text:
        return 'ocr'

    return 'unknown'


def respond_to_message(message, lang='en'):
    """Return a chat response in English or Telugu based on detected intent."""
    intent = detect_intent(message)
    current_hour = datetime.now().hour

    responses = {
        'te': {
            'bill': 'మీ బిల్ తగ్గించాలంటే AC వినియోగాన్ని తగ్గించండి.',
            'usage': 'మీ యూనిట్లు ఎక్కువగా ఉన్నాయి. ఇంటర్‌నల్ పరికరాలను తనిఖీ చేయండి.',
            'saving': 'బిల్ తగ్గించడానికి LED లైట్లు ఉపయోగించండి మరియు అపరాధ పరికరాలను ఆఫ్ చేయండి.',
            'ocr': 'మీ మీటర్ చిత్రం అప్లోడ్ చేయండి, నేను రీడింగ్‌ను తీయగలను.',
            'unknown': 'నన్ను మీ బిల్ లేదా వినియోగం గురించి చెప్పండి, నేను సహాయం చేస్తా.'
        },
        'en': {
            'bill': 'To estimate your bill, share your current unit consumption and I will predict the amount.',
            'usage': 'Send your recent usage history so I can detect any abnormal patterns.',
            'saving': 'Use LED lights, unplug idle devices, and run heavy appliances during off-peak hours.',
            'ocr': 'Upload a meter image and I will extract the reading using OCR.',
            'unknown': 'I can help with bill prediction, usage insights, and energy saving tips.'
        }
    }

    # Get language specific responses, default to English
    lang_responses = responses.get(lang, responses['en'])
    response_text = lang_responses.get(intent, lang_responses['unknown'])

    # Professional greeting for English responses during morning hours
    if lang == 'en' and current_hour < 12:
        greeting = "Good morning! "
        return f"{greeting}{response_text}"

    return response_text
