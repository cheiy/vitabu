from flask import Flask
sam = Flask(__name__)

@sam.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

#if __name__ == "__main__":
#    main.run(host='0.0.0.0')

