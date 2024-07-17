from flask import Blueprint, request, jsonify
from models import Expense, db

bp = Blueprint('expenses', __name__)

@bp.route('/api/expenses', methods=['GET', 'POST'])
def handle_expenses():
    if request.method == 'POST':
        data = request.json
        new_expense = Expense(amount=data['amount'],category=data['category'],description=data['description'],date=data['date'])
        db.session.add(new_expense)
        db.session.commit()
        return jsonify({"message": "Expense added successfully"}), 201
    
    elif request.method == 'GET':
        expenses = Expense.query.all()
        return jsonify([{"id": e.id, "amount": e.amount, "category": e.category, "description": e.description, "date": e.date.isoformat()} for e in expenses]), 200






