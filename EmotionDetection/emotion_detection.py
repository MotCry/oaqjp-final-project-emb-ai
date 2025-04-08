import requests
import json

def emotion_detector(text_to_analyse):
    params = {
        'url': 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict',
        'headers': {
            "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
        },
        'json': {
            "raw_document": {
                "text": text_to_analyse
            }
        }
    }
    response = requests.post(params['url'], headers=params['headers'], json=params['json'])
    formatted_response = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
        }

    if response.status_code == 200: 
        respone_json = json.loads(response.text)['emotionPredictions'][0]['emotion']
        dominant_emotion_score = -1
        for emotion, score in respone_json.items():
            formatted_response[emotion] = score
            if score > dominant_emotion_score:
                formatted_response['dominant_emotion'] = emotion
                dominant_emotion_score = score
        
        

    return formatted_response