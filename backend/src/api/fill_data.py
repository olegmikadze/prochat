"""
File for inserting into db fake data.
Available modes:
    - test (all tables are filled);
    - production (statuses tables are filled only).
"""

# import sys
# import random
# from random import randint
# from datetime import datetime, timedelta
# from faker import Faker
# from flask import Flask

# from models import (db, User)


# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:1@prochat'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# db.init_app(app)
# app.app_context().push()

# some img url for random.choice() data
# user_img_urls = ( 'https://pngimage.net/wp-content/uploads/2018/06/logo-user-png-6.png',
#                   'https://banner2.kisspng.com/20180716/lra/kisspng-logo-person-user-person-icon-5b4d2bd2236ca6.6010202115317841461451.jpg',
#                   'https://pngimage.net/wp-content/uploads/2018/06/user-logo-png-4.png',
#                 )




#  function for inserting data into user table
# def users(fake):
#     user_default_settings = {'email_notification':True,
#                              'conformation_of_app':True,
#                              'telegram_notification':False, }

#     with app.app_context():
#         data_in_db = User.query.all()

#     if not data_in_db:
#         with app.app_context():
#             for i in range(10):
#                 first_name = fake.first_name()
#                 last_name = fake.last_name()
#                 nickname = first_name + last_name
#                 new_User = User(nickname = nickname,
#                                 email = fake.email(),
#                                 phone = fake.phone_number(),
#                                 password = fake.password(length=10),
#                                 first_name = first_name,
#                                 last_name = last_name,
#                                 birth_date = fake.date_between(start_date="-30y",
#                                    end_date="-20y").strftime('%Y-%m-%d'),
#                                 rating =  round(random.uniform(3, 5),2),
#                                 # image_url = random.choice(user_img_urls),
#                                 description = fake.text(max_nb_chars=200),
#                                 viber_account = '1',
#                                 telegram_account = '1',
#                                 settings = user_default_settings,
#                                 status_id = 1)
#                 db.session.add(new_User)
#             db.session.commit()

