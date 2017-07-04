from flask import  request, redirect, url_for, \
     render_template, flash,Blueprint, jsonify, session
from GCDatabaseMangment.GCDBSchema import db, Inventory, Processing, Client, Category, checkedOut
from GCDatabaseMangment.InventroyForms import Checkout
import json

InvMangment = Blueprint('InvMangment', __name__, template_folder='templates')

#https://www.dynatable.com/?perPage=50
#cool table plug in just would need to add checkout box for it and also editablity

@InvMangment.route("/editItemName")
def editItemName():
    # for this id thing what we will do is give each row the id atibute of the item id in inv
    id = request.args.get('itemID',0,type=int)
    newName = request.args.get('new_name_'+id,0,type=int)
    item = Inventory.query.filter_by(id = id).first()
    item.itemName = newName
    db.session.commit()
    return Inventory.query.filter_by(id = id).first().itemName #get the new name from the inventory


@InvMangment.route("/editQuantityAvailable")
def editQuanityAvalible():
    pass


@InvMangment.route("/editQuantityOut")
def editQuantityOut():
    pass


@InvMangment.route("/editProcessing")
def editProcessing():
    pass


@InvMangment.route("/editPrice")
def editPrice():
    pass


@InvMangment.route("/editCatagory")
def editCatagory():
    pass


@InvMangment.route("/addCatagory")
def addCatagoty():
    pass


@InvMangment.route("/getInv")
def getInv():
    invList = Inventory.query.all()
    return jsonify(records=[i.serializeTable for i in invList])
                  


@InvMangment.route("/getbackpack")
def getBackpack():
    # session.pop("backpack", None)
    if "backpack" not in session:
        return jsonify(records={"Error": "No Backpack Found in session"})
    else:
        tableData = []
        for item in session["backpack"]:
            data = Inventory.query.filter_by(id=item["id"]).first().serializePopUp
            data["numberToCheckout"] = item["numToCheckout"]
            print(data)
            tableData += data
        return jsonify(records=tableData)



@InvMangment.route("/getItem/<int:itemID>",  methods=['POST', 'GET'])
def getItem(itemID):
    item = Inventory.query.filter_by(id=itemID).first()
    numAvalible =  item.quantityAvailable
    choices = [(n, n) for n in range(1, numAvalible+1, 1)]
    form = Checkout()
    form.numberToCheckout.choices = choices
    if request.method == 'POST':
        if "backpack" in session:
            session["backpack"] += [{"itemName":item.itemName, "id":item.id, "numToCheckout":int(form.data['numberToCheckout'])}]
        else:
            session["backpack"] = [{"itemName":item.itemName, "id":item.id, "numToCheckout":int(form.data['numberToCheckout'])}]
        print(session["backpack"], len(session["backpack"]))
        return redirect(url_for('GCInv.table'))
    elif request.method == 'GET':# this route should only be called internally
        return render_template("itemCheckoutPop.html", item=item, form=form)


@InvMangment.route("/checkout")
def checkout():
    cart = session["backpack"]
    client = Client.query.filter_by(id=session["clientID"])
    for item in cart:
        Inventory.query.checkItemOut(client=client, Itemid=item["id"], ItemNum=item["numToCheckout"])


