import os
from flask import Flask
if os.path.exists("env.py"):
    import env

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World ... again"

# This tells the app how and where to run the application


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            # make sure to turn this to false for deployment
            debug=True)
