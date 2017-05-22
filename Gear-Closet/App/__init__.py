import os

from App.GearClosetMain.controlers import GCInv
from App.InventoryEditor.controlers import InvEditor
from flask import Flask
from flask_bootstrap import Bootstrap

from GCDatabaseMangment.GCDBSchema import db

app = Flask(__name__)

app.config.update(dict(SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.getcwd() + '/testGC.db',
                       SQLALCHEMY_TRACK_MODIFICATIONS = False,
                       SECRET_KEY='development key'))
# print("app config set")
Bootstrap(app)
db.init_app(app)
with app.app_context():
    db.create_all()


app.register_blueprint(GCInv)
app.register_blueprint(InvEditor, url_prefix='/edit')
# print(app.url_map)