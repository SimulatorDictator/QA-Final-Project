# This is the structure of the databases.
from application import db

# These two tables will have a many-to-many relationship.
class Board_Games(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_name = db.Column(db.String(30), nullable=False)
    player_count_min = db.Column(db.Integer, nullable=False)
    player_count_max = db.Column(db.Integer, nullable=False)
    game_order = db.relationship(db.Column('Game_Order', backref='customers'))

class Customers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.Integer(11), nullable=False)
    customer_order = db.relationship(db.Column('Game_Order', backref='board_games'))

# This is the association table.
class Game_Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column('boardgame_id', db.Integer, db.ForeignKey(Board_Games.id))
    customer_id = db.Column('customer_id', db.Integer, db.ForeignKey(Customers.id))