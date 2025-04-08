'''
A project in Python and Flask integrating IBM's emotion detector
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion")

@app.route("/")
def render_index_page():
    '''
    Home page route
    '''
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_analyzer():
    '''
    Routing to the emotionDetector
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    answer = "For the given statement, the system response is"
    for emotion, score in response.items():
        if emotion != 'dominant_emotion':
            answer += f" {emotion}: {score},"
        else:
            answer += f" The dominant emotion is {score}."
    if response['dominant_emotion'] is not None:
        return answer
    return 'Invalid text! Please try again!.'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
