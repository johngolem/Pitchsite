from . import db
#...

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))

    # __tablename__ = 'users'
    # id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # username = db.Column(db.String(20), unique=True,nullable=False)
    # email = db.Column(db.String(30), unique=True,nullable=False)
    # password = db.Column(db.String(80))
    # pitch = db.relationship('Pitch')
    # liked = db.relationship('PostLike', foreign_keys='PostLike.users_id', backref='users',lazy='dynamic')
    

    def __repr__(self):
        return f'User {self.username}'

