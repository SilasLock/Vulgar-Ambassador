from flask import request, redirect, url_for, \
    render_template, flash, Blueprint, jsonify, session
from GCDatabaseMangment.GCDBSchema import db, Inventory, Processing, Client, Category, checkedOut
from GCDatabaseMangment.InventroyForms import Checkout, CreateClient, HandleItem
from sqlalchemy import update
import json

InvMangment = Blueprint('InvMangment', __name__, template_folder='templates')


@InvMangment.route("/editItemName")
def editItemName():
    # for this id thing what we will do is give each row the id atibute of the item id in inv
    id = request.args.get('itemID', 0, type=int)
    newName = request.args.get('new_name_' + id, 0, type=int)
    item = Inventory.query.filter_by(id=id).first()
    item.itemName = newName
    db.session.commit()
    return Inventory.query.filter_by(id=id).first().itemName  # get the new name from the inventory


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


@InvMangment.route("/editItem/<int:itemID>", methods=['POST', 'GET'])
def editItem(itemID):
    item = Inventory.query.filter_by(id=itemID).first()
    choices = [(category.categoryName, category.categoryName) for category in Category.query.all()]
    HandleItem.itemCategory.choices = choices
    form = HandleItem(itemName=item.itemName, itemQuantity=item.quantityAvailable, itemOut=item.quantityOut,
                      itemPrice=item.price, itemProcessingRequired=item.processing,
                      itemCategory=Category.query.filter_by(categoryName=item.category).first().categoryName)
    form.itemCategory.choices = choices
    # form.itemCategory.process_data(Category.query.filter_by(categoryName=item.category).first().id)
    if request.method == 'POST':
        print(form.validate())
        if form.validate():
            flash("successfully updated", "success")
            data = form.data
            item.itemName=data["itemName"]
            item.quantityAvailable=data['itemQuantity']
            item.quantityOut=data['itemOut']
            item.quantityInProcessing=0
            item.price=data['itemPrice']
            item.category=data['itemCategory']
            item.processing=data['itemProcessingRequired']
            # Inventory.query.filter_by(id=itemID).update().
            # TODO: FIX ME
            db.session.commit()
            return redirect(url_for('GCInv.mangeInventory'))
        else:
            flash("we were unable to update form due to: " + str(form.errors), "warning")
            return redirect(url_for('GCInv.mangeInventory'))
    elif request.method == 'GET':  # this route should only be called internally
        return render_template("modals/editItemPopUp.html", item=item, form=form)


@InvMangment.route("/addCatagory", methods=['GET', 'POST'])
def addCatagoty():
    pass


@InvMangment.route("/getInv")
def getInv():
    invList = Inventory.query.all()
    return jsonify(data=[i.serializeTable for i in invList])


@InvMangment.route("/getClientsMain")
def getClientsMain():
    ClientList = Client.query.all()
    return jsonify(data=[i.serializeTableClients for i in ClientList])


@InvMangment.route("/getClients")
def getClients():
    ClientList = Client.query.all()
    return jsonify(data=[i.serializeTable for i in ClientList])


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
        return jsonify(data=tableData)


@InvMangment.route("/getCheckout")
def getCheckout():
    checkoutList = checkedOut.query.all()
    return jsonify(data=[i.serializeTable(client=Client.query.filter_by(studentID=i.clientCheckoutID).first(), item=Inventory.query.filter_by(id=i.inventory).first()) for i in checkoutList])


@InvMangment.route("/getClientsCheckedOut")
def getClientsCheckedOut():
    clientList = Client.query.all()
    return jsonify(data=[i.serializeTable for i in clientList])


@InvMangment.route("/getItem/<int:itemID>", methods=['POST', 'GET'])
def getItem(itemID):
    item = Inventory.query.filter_by(id=itemID).first()
    numAvalible = item.quantityAvailable
    choices = [(n, n) for n in range(1, numAvalible + 1, 1)]
    form = Checkout()
    form.numberToCheckout.choices = choices
    if request.method == 'POST':
        if "backpack" in session:
            session["backpack"] += [
                {"itemName": item.itemName, "id": item.id, "numToCheckout": int(form.data['numberToCheckout'])}]
        else:
            session["backpack"] = [
                {"itemName": item.itemName, "id": item.id, "numToCheckout": int(form.data['numberToCheckout'])}]
        print(session["backpack"], len(session["backpack"]))
        return redirect(url_for('GCInv.checkoutGear'))
    elif request.method == 'GET':  # this route should only be called internally
        return render_template("modals/itemCheckoutPop.html", item=item, form=form)


@InvMangment.route("/getBackpackPopUp")
def getBackpackPopUp():
    return render_template("modals/BackpackPopUp.html")


@InvMangment.route("/makeClientPopUp", methods=['POST', 'GET'])
def getClientPopUp():
    form = CreateClient()
    if request.method == 'POST':
        if form.validate() == False:
            # TODO: Flash error message
            return redirect(url_for('GCInv.selectClient'))
        else:
            print(form.data)
            db.session.add(Client(form.data))
            db.session.commit()
            return redirect(url_for('GCInv.selectClient'))
    elif request.method == 'GET':  # this route should only be called internally
        return render_template("modals/createClientPopUp.html", form=form)

@InvMangment.route("/getClientsCheckedoutItems/<int:Clientid>")
def getClientsCheckedoutItems(Clientid):
    client = Client.query.filter_by(id=Clientid).first()
    itemsOut = checkedOut.query.filter_by(clientCheckoutID=client.studentID).all()
    itemsOutDictList = []
    for item in itemsOut:
        inventoryData =  Inventory.query.filter_by(id=item.inventory).first()
        d = {
            "itemName" : inventoryData.itemName,
            "numToCheckout" : item.numberOut
        }
        itemsOutDictList += [d]
    print(itemsOutDictList)
    print(itemsOut)
    return render_template("modals/CheckInModal.html", items=itemsOutDictList, name=client.name)




@InvMangment.route("/checkout/<int:Clientid>")
def checkout(Clientid):
    cart = session["backpack"]
    client = Client.query.filter_by(id=Clientid).first()
    for item in cart:
        Inventory.query.checkItemOut(client=client, Itemid=item["id"], ItemNum=item["numToCheckout"])
    session.pop("backpack", None)
    return redirect(url_for('GCInv.checkoutGear'))


@InvMangment.route("/selectClient/<int:Clientid>")
def selectClient(Clientid):
    client = Client.query.filter_by(id=Clientid).first()
    return render_template("/modals/CheckoutModal.html", client=client)
