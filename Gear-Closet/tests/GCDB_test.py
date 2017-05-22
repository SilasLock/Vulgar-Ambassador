import unittest, os, datetime, json
from copy import deepcopy
from flask_testing import TestCase
from GCDatabaseMangment.InventroyForms import AddGeartoInv
from GCDatabaseMangment.GCDBSchema import db,Inventory,Category,Client,Processing,checkedOut
from App import app

Inputs = {
    'addIteminput': {'itemPrice': 250, 'itemQuantity': 3, 'itemCategory': 'Clothes', 'itemName': 'Arcteryx  Hoddie', 'submit': True, 'itemProcessingRequired': True},
    # The above referse to a input that comes from the add the inv from InventoryForms.AddGeartoInv
    'Client' : {'name':'Alasdair Johnson', 'phoneNumber': 9192339401, 'studentID': 100000000, 'email': 'alasdair@alasdair.com'}
}
Expected = {
'addItemExpected': {'itemName': 'Arcteryx  Hoddie', 'quantityAvailable': 3, 'category': 'Clothes', 'price': 250,
                    'processing': True, 'quantityOut':0}
}


class Database_Use_Tests(TestCase):


    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.getcwd() + '/DataBase_Test_Scripts/testing.db'
    TESTING = True

    def create_app(self):
        return app

    def setUp(self):
        db.create_all()
        #loads inventory and adds it to db
        with open(os.curdir + 'inventoryGC.json') as data_file:
            data = json.load(data_file)
        for item in data['data'].values():
            temp = Inventory(item)
            db.session.add(temp)


    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_additemToinv(self):
        """
        Basic test of db relationship will use a posible input form the
        WTF-form and initalize and add a Inventory object add it to the db
        and make sure it is present
        """
        item = Inventory(Inputs["addIteminput"])
        db.session.add(item)

        #query db for item
        itemInInv = deepcopy(Inventory.query.filter_by(itemName="Arcteryx  Hoddie")[0].__dict__)
        itemInInv.pop('_sa_instance_state', None)
        itemInInv.pop('id', None)
        self.assertDictEqual(itemInInv, Expected['addItemExpected'])

    def test_checkoutItemFromInventory(self):
        """
        Will test to make sure that we can remove item from inventory and all feilds are created correctly
        and shit
        """
        checoutItemName = "Water Jug (7 gal) Green"
        checkOutItem = Inventory.query.filter_by(itemName=checoutItemName).first()

        # before Checkout Query info
        beforeNumAvalible = checkOutItem.quantityAvailable
        beforeNumOut = checkOutItem.quantityOut

        #Info for checkout query construction
        checkedoutItemID = checkOutItem.id
        personCheckingOut = Client(Inputs['Client'])

        #simulate Client in table
        db.session.add(personCheckingOut)

        print("checked out item id: ", checkedoutItemID)
        print("person checking out id: ", personCheckingOut.studentID)

        # check Item out of inventory this should update the quanity avalible -1 and incress
        # quanity out by +1 as well as create a row in checked out with client id in it and the inventory id
        Inventory.query.checkItemOut(client=personCheckingOut, Itemid=checkedoutItemID)

        # post checkout Querys
        postCheckoutItemInInv = Inventory.query.filter_by(itemName=checoutItemName).first()
        checkedOutTableData = checkedOut.query.filter_by(inventory=checkedoutItemID).first()

        # post checkout Query results
        AfterNumAvalible = postCheckoutItemInInv.quantityAvailable
        AfterNumOut = postCheckoutItemInInv.quantityOut

        print("post checked out item quality: ", AfterNumAvalible)
        print("post checkout quanity out: ", AfterNumOut)

        # Inventory checks
        self.assertEqual(beforeNumAvalible, AfterNumAvalible+1)# +1 indicates that before has decreased by 1
        self.assertEqual(beforeNumOut, AfterNumOut-1) # -1 indicates before has increased by 1

        # checkOut checks
        print("client checkedout ID: ", checkedOutTableData.clientCheckoutID)
        print("person checking out id: ",  personCheckingOut.studentID)
        print("inventory id: ", checkedOutTableData.inventory)
        print("checked out table item id: ", checkedoutItemID)

        self.assertEqual(checkedOutTableData.clientCheckoutID, personCheckingOut.studentID)
        self.assertEqual(checkedOutTableData.inventory, checkedoutItemID)

    def test_checkInItemFromInventoryNonProcessing(self):
        """

        :return:
        """
        pass
    def test_checkInItemFromInventoryProcessing(self):
        """

        :return:
        """
        pass





if __name__ == '__main__':
    unittest.main()
