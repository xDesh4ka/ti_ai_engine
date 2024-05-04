from flask import Flask, request
from flask_swagger_ui import get_swaggerui_blueprint

from Answer import from_json
from OutputMessage import OutputMessage
from llamaEngine import AiEngine

app = Flask(__name__)
aiEngine = AiEngine()

SWAGGER_URL = '/api'
API_URL = '/'


swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Ti Ai Engine'
    }
)

app.register_blueprint(swagger_ui_blueprint)

@app.route('/getReport', methods=['POST'])
def get_report():
    data = request.get_json()
    message = OutputMessage(date=data['date'], text=data['text'])
    ai_response = aiEngine.ask_and_response(message.text).replace("\n", "")
    answer = from_json(ai_response).to_json()
    return answer


if __name__ == '__main__':
    app.run(port=8086, host="localhost", debug=True)
