from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

my_bot = ChatBot('My Chat')

trainer = ListTrainer(my_bot)
conversation = open('chatref', 'r').readlines()
trainer.train(conversation)

@app.route("/")
def home():
    return render_template("index.html")



@app.route("/get")
def getBotResponse():
    userText = request.args.get('msg')
    return str(my_bot.get_response(userText))


if __name__ == "__main__":
    app.run()