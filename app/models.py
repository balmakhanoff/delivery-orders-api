from datetime import datetime
from . import db
from enum import Enum

# Модель для заказа


class OrderStatus(Enum):
    CREATED = "created"
    IN_DELIVERY = "in delivery"
    DELIVERED = "delivered"


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    delivery_address = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)
    status = db.Column(db.Enum(OrderStatus), default=OrderStatus.CREATED)
    # Связь с комментариями
    comments = db.relationship('Comment', backref='order', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'delivery_address': self.delivery_address,
            'created_at': self.created_at,
            'is_active': self.is_active,
            'status': self.status.name
        }

# Модель для комментариев


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'text': self.text,
            'order_id': self.order_id
        }
