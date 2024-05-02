import json
import datetime

from flask import Flask, request

from Answer import Answer, from_json
from OutputMessage import OutputMessage
from llamaEngine import AiEngine

app = Flask(__name__)
aiEngine = AiEngine()


@app.route('/getReport', methods=['POST'])
def get_report():
    data = request.get_json()
    message = OutputMessage(date=data['date'], text=data['text'])
    ai_responce = aiEngine.ask_and_response(message.text).replace("\n", "")
    answer = from_json(ai_responce).to_json()
    return answer


if __name__ == '__main__':
    app.run(debug=True)