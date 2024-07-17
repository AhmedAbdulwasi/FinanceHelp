from flask import Flask
from flask_cors import CORS
from config import config_dict
from models import db



def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(config_dict[config_name])
    CORS(app)

    db.init_app(app)

    with app.app_context():
        db.create_all()
        from Routes.expenses import bp as expenses_bp
        from Routes.income import bp as income_bp
        from Routes.stocks import bp as stocks_bp

        app.register_blueprint(expenses_bp)
        app.register_blueprint(income_bp)
        app.register_blueprint(stocks_bp)

        return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
