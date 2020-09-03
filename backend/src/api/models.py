from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.ext.hybrid import hybrid_property

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.Text, nullable=False, unique=True)
    email = db.Column(db.Text, nullable=False, unique=True)
    phone = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=True, unique=False)
    first_name = db.Column(db.Text, nullable=False, unique=False)
    last_name = db.Column(db.Text, nullable=False, unique=False)
    birth_date = db.Column(db.DateTime, nullable=False, unique=False)
    rating = db.Column(db.Float, nullable=True, unique=False)
    image_url = db.Column(db.Text, nullable=True, unique=False)
    description = db.Column(db.Text, nullable=True, unique=False)
    viber_account = db.Column(db.Text, nullable=True, unique=False)
    telegram_account = db.Column(db.Text, nullable=True, unique=False)
    settings = db.Column(db.JSON, nullable=False, unique=False)

    status_id = db.Column(db.Integer, db.ForeignKey('user_status.id'), nullable=False, unique=False)

    @staticmethod
    def update_rating(user_id):
        """
        Method that replaces a trigger in database (but not entirely, it'll not be updated ).
        It will count current rating of a user and update it.
        :return:
        """
        user = db.session.query(User).filter(
            User.id == user_id,
        ).first()
        user.rating = db.session.query(func.avg(Feedback.rating).label('avg_rate')).filter(
            Feedback.user_to_id == user_id,
        )

        db.session.commit()

