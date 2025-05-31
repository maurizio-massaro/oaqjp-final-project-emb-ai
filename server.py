"""Flask app to run emotion detection via web interface."""

from flask import Flask, render_template, request
from  EmotionDetection.emotion_detection import emotion_detector

app = Flask("EmotionDetector")


@app.route("/emotionDetector")
def sent_analyzer():
    """Analyze emotions from user input provided via query parameter."""
    text_to_analyze = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyze)

    if response.get("status_code") == 200 or response.get("status_code") == 400:
        text_to_return = f"""
        For the given statement, the system response is:
        'anger': {response.get('anger')}, 'disgust': {response.get('disgust')}, 
        'fear': {response.get('fear')},
        'joy': {response.get('joy')}, 'sadness': {response.get('sadness')}.
        The dominant emotion is: {response.get('dominant_emotion')}  
        """
        return text_to_return
    return "Invalid input or an error occurred. Try again!", 500


@app.route("/")
def render_index_page():
    """Render the home page of the emotion detector."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
