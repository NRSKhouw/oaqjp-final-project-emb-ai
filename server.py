''' Executing this function initiates the application of emotion 
    detector to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package
from flask import Flask, render_template, request
# Import the sentiment_analyzer function from the package created
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    emotion_values = ", ".join(f"'{key}': {value}" for key, value in response.items() if key != "dominant_emotion")
    output = (
                f"For the given statement, the system response is {emotion_values}. "
                f"The dominant emotion is <b>{response['dominant_emotion']}</b>."
                )
    if response['anger'] is None:
        return "<b>Invalid text! Please try again!</b>"
    else:
        return output

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    app.run(host="0.0.0.0", port=5000)