import os, json
from GCDatabaseMangment.GCDBSchema import Inventory, Category
from App.GearClosetMain.controlers import GCInv
from App.InventoryMangment.controlers import InvMangment
from flask import Flask, session
from flask_bootstrap import Bootstrap
from sqlalchemy import exists

from GCDatabaseMangment.GCDBSchema import db

app = Flask(__name__)

app.config.update(dict(SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.getcwd() + '/testGC.db',
                       SQLALCHEMY_TRACK_MODIFICATIONS = False,
                       SECRET_KEY='development key'))
# print("app config set")
Bootstrap(app)
db.init_app(app)


# with app.app_context():
#     db.create_all()
#     print(os.curdir)
#     with open(os.curdir + '/tests/inventoryGC.json') as data_file:
#         data = json.load(data_file)
#     for item in data['data'].values():
#         try:
#             cat = Category(category=item['itemCategory'])
#             db.session.add(cat)
#             db.session.commit()
#         except:
#             db.session.rollback()
#         temp = Inventory(item)
#         db.session.add(temp)
#     db.session.commit()


app.register_blueprint(GCInv)
app.register_blueprint(InvMangment, url_prefix='/api')

