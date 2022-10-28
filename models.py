"""Models for Blogly."""
import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""
    with app.app_context():
        db.app = app
        db.init_app(app)

class User(db.Model):
    """User model"""
    __tablename__ = "users"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    first_name = db.Column(db.String(15),
                    nullable=False)
    last_name = db.Column(db.String(15), nullable=False)
    image_url = db.Column(db.String, default="/static/images/defaultpic.png")
    def __repr__(self):
        """Representation output"""
        return f"<Post {self.first_name} {self.last_name} {self.img_url}>"
    

    @property
    def full_name(self):
        """Return full name of user."""

        return f"{self.first_name} {self.last_name}"

    def get_full_name(self):
        """gets full name"""
        u = self
        return f"{u.first_name} {u.last_name}"

class Post(db.Model):
    """Post model"""
    __tablename__ = "posts"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    title = db.Column(db.String(50),
                    nullable=False)
    content = db.Column(db.String(1000),
                    nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', backref='posts')
    def __repr__(self):
        """Representation output"""
        return f"<Post {self.title} {self.content} {self.created_at} {self.user_id}>"
def get_posts_by_id(x):
    """returns posts with user id"""
    p = Post.query.filter_by(user_id=x).all()
    return p
def get_post(user, id):
    """returns single post from user with id of id"""
    p = Post.query.filter_by(user_id=user, id=id)
    return p
    
    

