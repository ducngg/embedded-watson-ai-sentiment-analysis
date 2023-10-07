"""Server module"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def sent_emotion_detector():
    """Sent text to Watson AI and get response"""
    text_to_analyze = request.args.get('textToAnalyze')
    res_emotions = emotion_detector(text_to_analyze)
    if res_emotions['dominant_emotion'] is None:
        return "Invalid input!"
    message = "For the given statement, the system response is"
    for key, value in res_emotions.items():
        if key != 'dominant_emotion':
            message += ' \'' + key + '\': '
            message += str(value) + ','
    message = message[:-1]
    message += '. The dominant emotion is ' + res_emotions['dominant_emotion'] + '.'
    return message

@app.route("/")
def render_index_page():
    """Render index.html(root)"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
