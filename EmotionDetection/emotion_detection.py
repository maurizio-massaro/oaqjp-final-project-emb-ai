import requests
import json

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    data = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        emotion_scores = result['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        emotion_scores["dominant_emotion"] = dominant_emotion
        emotion_scores["status_code"] = response.status_code
        return emotion_scores
    else:
        return {"status_code": response.status_code, "dominant_emotion":"failed to execute the query"}