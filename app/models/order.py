from app.extensions import db
from datetime import datetime, timezone

class Order(db.Model):
    __tablename__ = 'orders'
    
    id = db.Column(db.Integer, primary_key=True)
    date_ordered = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    total_price = db.Column(db.Numeric(10, 2), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='pendente')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    items = db.relationship('OrderItem', backref='order', cascade="all, delete-orphan", lazy=True)

    def __repr__(self):
        return f'<Order {self.id} - Status {self.status}>'


class OrderItem(db.Model):
    __tablename__ = 'order_items'
    
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    price_at_purchase = db.Column(db.Numeric(10, 2), nullable=False)

    book = db.relationship('Book', backref='sold_items')

    def __repr__(self):
        return f'<OrderItem BookID: {self.book_id} Qty: {self.quantity}>'