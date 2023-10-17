import sys
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import yaml

try:
    with open(".local.yml", "r") as file:
        config = yaml.safe_load(file)
except:
    sys.exit("Config file not found")

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = config["dsn"]
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
db = SQLAlchemy(app)
app.app_context().push()

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/")
def hello():
    return "My First App"