from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot(
    'Terminal',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch'
    ],
    database_uri='sqlite:///database.db'
)

bot.set_trainer(ListTrainer)

for files in os.listdir("data/english/"):
    data = open("data/english/" + files, 'r').readline()
    bot.train(data)

while True:
    message = input('You:')
    if message.strip() != 'Bye':
        reply = bot.get_response(message)
        print('ChatBot:', reply)
    if message.strip() == 'Bye':
        print('ChatBot: Bye')
        break
