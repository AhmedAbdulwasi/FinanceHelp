from flask import Blueprint, request, jsonify
from models import Stock, db
import requests

bp = Blueprint('stocks', __name__)

API_KEY = 'P8J3PZ7O4GLYVKUF'


@bp.route('/api/stocks', methods=['GET', 'POST'])
def handle_stocks():
    if request.method == 'POST':
        data = request.json
        new_stocks = Stock(symbol=data['symbol'])
        db.session.add(new_stocks)
        db.session.commit()
        return jsonify({"message": "Stock added to watchlist"}), 201
    elif request.method == 'GET':
        stocks = Stock.query.all()
        stockdata = []
        for stock in stocks:
            url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock.symbol}&interval=5min&apikey={API_KEY}'
            r = requests.get(url)
            data = r.json()['Global Quote']

            stockdata.append({'symbol': stock.symbol, 'high': data['03. high'], 'low': data['04. low'], 'price': data['05. price'], 'volume': data['06. volume'], 'change_percent': data['10. change percent']})

        return jsonify(stockdata), 200

