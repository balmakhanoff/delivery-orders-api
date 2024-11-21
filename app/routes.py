from flask import Blueprint, jsonify, request
from .models import Order, Comment
from . import db

api_bp = Blueprint('api', __name__)

# Создание заявки на доставку


@api_bp.route('/api/orders', methods=['POST'])
def create_order():
    data = request.json
    if not data or 'delivery_address' not in data:
        return jsonify({'error': 'Delivery address is required'}), 400

    # Создаем заказ
    new_order = Order(delivery_address=data['delivery_address'])
    db.session.add(new_order)
    db.session.commit()

    return jsonify(new_order.to_dict()), 201

# Получение информации о заявке


@api_bp.route('/api/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = Order.query.get(order_id)
    if not order:
        return jsonify({'error': 'Order not found'}), 404

    return jsonify(order.to_dict())

# Переключение статуса заявки на "не активна"


@api_bp.route('/api/orders/<int:order_id>/deactivate', methods=['PUT'])
def deactivate_order(order_id):
    order = Order.query.get(order_id)
    if not order:
        return jsonify({'error': 'Order not found'}), 404

    if not order.is_active:
        return jsonify({'error': 'Order is already inactive'}), 400

    order.is_active = False
    db.session.commit()

    return jsonify({'message': f'Order {order_id} status updated to inactive'}), 200

# Добавление комментария к заказу


@api_bp.route('/api/orders/<int:order_id>/comments', methods=['POST'])
def add_comment(order_id):
    order = Order.query.get(order_id)
    if not order:
        return jsonify({'error': 'Order not found'}), 404

    data = request.json
    if not data or 'text' not in data:
        return jsonify({'error': 'Comment text is required'}), 400

    # Создаем комментарий
    new_comment = Comment(text=data['text'], order_id=order_id)
    db.session.add(new_comment)
    db.session.commit()

    return jsonify(new_comment.to_dict()), 201

# Получение комментариев для заказа


@api_bp.route('/api/orders/<int:order_id>/comments', methods=['GET'])
def get_comments(order_id):
    order = Order.query.get(order_id)
    if not order:
        return jsonify({'error': 'Order not found'}), 404

    comments = Comment.query.filter_by(order_id=order_id).all()
    if not comments:
        return jsonify({'message': 'No comments found for this order'}), 404

    return jsonify([comment.to_dict() for comment in comments]), 200