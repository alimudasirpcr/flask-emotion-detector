import requests
import json

def emotion_detector(text_to_analyze):
    if not text_to_analyze.strip():  # Check for blank or whitespace input
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_data = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, headers=headers, json=input_data)

    if response.status_code == 200:
        data = response.json()
        emotion_predictions = data.get('emotionPredictions', [{}])[0]
        emotions = emotion_predictions.get('emotion', {})
        emotion_scores = {
            'anger': emotions.get('anger', None),
            'disgust': emotions.get('disgust', None),
            'fear': emotions.get('fear', None),
            'joy': emotions.get('joy', None),
            'sadness': emotions.get('sadness', None)
        }
        dominant_emotion = max(emotion_scores, key=emotion_scores.get, default=None)
        emotion_scores['dominant_emotion'] = dominant_emotion
        return emotion_scores

    elif response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    else:
        return f"Error: {response.status_code}, {response.text}"
