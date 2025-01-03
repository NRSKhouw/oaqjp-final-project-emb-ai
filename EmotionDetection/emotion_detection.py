import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json = myobj, headers = headers)
    formatted_response = json.loads(response.text)
    emotion_score = formatted_response["emotionPredictions"][0]["emotion"]
    dominant_emotion_key = max(emotion_score, key = emotion_score.get)

    emotion_score['dominant_emotion'] = dominant_emotion_key

    return emotion_score