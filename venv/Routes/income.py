from flask import Blueprint, request, jsonify
from models import Income, db

bp = Blueprint('income', __name__)

@bp.route('/api/income', methods=['GET', 'POST'])
def handle_income():
    
    if request.method == 'POST':
        data = request.json
        new_income= Income(amount=data['amount'],source=data['source'],description=data['description'],date=data['date'])
        db.session.add(new_income)
        db.session.commit()
        return jsonify({"message": "Income added successfully"}), 201
    
    elif request.method == 'GET':
        income = Income.query.all()
        return jsonify([{"id": i.id, "amount": i.amount, "source": i.source, "description": i.description, "date": i.date.isoformat()} for i in income]), 200