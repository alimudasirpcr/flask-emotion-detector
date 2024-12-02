"""
This module contains the Flask server for deploying an emotion detection application.
"""

from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector


app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    """
    Handle POST requests to /emotionDetector endpoint.

    Returns:
        JSON: Response with emotion detection results or error message.
    """
    data = request.get_json()
    text_to_analyze = data.get('text', '')

    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return jsonify({"response": "Invalid text! Please try again!"}), 400

    response = (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} "
        f"and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    