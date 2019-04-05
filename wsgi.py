from datetime import datetime
from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World! It is {}".format(datetime.now())

if __name__ == "__main__":
    application.run()
