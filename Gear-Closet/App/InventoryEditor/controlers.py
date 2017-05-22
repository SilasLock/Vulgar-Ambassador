from flask import  request, redirect, url_for, \
     render_template, flash,Blueprint, jsonify
from GCDatabaseMangment.GCDBSchema import db, Inventory, Processing, Client, Category, checkedOut

InvEditor = Blueprint('InvEditor', __name__, template_folder='templates')

#https://www.dynatable.com/?perPage=50
#cool table plug in just would need to add checkout box for it and also editablity

@InvEditor.route("/editItemName")
def editItemName():
    # for this id thing what we will do is give each row the id atibute of the item id in inv
    id = request.args.get('itemID',0,type=int)
    newName = request.args.get('new_name_'+id,0,type=int)
    item = Inventory.query.filter_by(id = id).first()
    item.itemName = newName
    db.session.commit()
    return Inventory.query.filter_by(id = id).first().itemName #get the new name from the inventory

@InvEditor.route("/editQuantityAvailable")
def editQuanityAvalible():
    pass

@InvEditor.route("/editQuantityOut")
def editQuantityOut():
    pass

@InvEditor.route("/editProcessing")
def editProcessing():
    pass

@InvEditor.route("/editPrice")
def editPrice():
    pass

@InvEditor.route("/editCatagory")
def editCatagory():
    pass

@InvEditor.route("/addCatagory")
def addCatagoty():
    pass



