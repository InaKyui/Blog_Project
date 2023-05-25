import config
from flask import Flask
from models import UserModel
from extends import db, mail, cache
from blueprints.qa import bp as bp_qa
from blueprints.auth import bp as bp_auth
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)
mail.init_app(app)
cache.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(bp_qa)
app.register_blueprint(bp_auth)

if __name__ == "__main__":
    app.run(debug=True)