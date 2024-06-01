from flask import Flask, render_template, request

from service.ChatBotService import ChatBotService
from service.TrainingService import TrainingService

app = Flask(__name__)
chatbotService = ChatBotService()


@app.route('/', methods=['GET', 'POST'])
def start():
    return render_template('chatbot.html')


@app.route('/general/train', methods=['GET'])
def trainGeneralModel():
    trainingService = TrainingService("general")
    trainingService.trainingModel()
    return "OK"


@app.route('/food/train', methods=['GET'])
def trainFoodModel():
    trainingService = TrainingService("food")
    trainingService.trainingModel()
    return "OK"


@app.route('/post', methods=['GET', 'POST'])
def getAnswer():
    question = request.form.get('question')
    return chatbotService.chat(question)


if __name__ == '__main__':
    app.run()
