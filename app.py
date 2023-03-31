from flask import Flask
#create a flask object
app = Flask(__name__)
#we will give routing
@app.route('/')
def hello():
    return "Hey all how are you?"
#run the application
app.run()
