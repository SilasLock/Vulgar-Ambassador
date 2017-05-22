from flask_sqlalchemy import BaseQuery
from GCDatabaseMangment import GCDBSchema as Schema

class inventoryMangment(BaseQuery):
    """
        This class will handel checking out and in an item by updating the db to:

    """
    def checkItemOut(self, client, Itemid):
        """
        add item to checked out table with client tied to it
        update inventory to reduce the number available and incress number out
        :param client: a client object
        :param Itemid: item id in the database
        :return: will check item out of inventory
        """
        clientID = client.studentID #pass a real cleint object
        checkedOutItem = Schema.checkedOut(clientID, Itemid)
        item = Schema.Inventory.query.filter_by(id=Itemid).first()#gets the item from db

        #move item out of inventory
        item.quantityOut += 1
        item.quantityAvailable += -1

        #TODO: Consider adding error handeling so that item quantitiyAvlible cannot be 0

        Schema.db.session.add(checkedOutItem)
        Schema.db.session.commit()

    def checkItemIn(self, client, Itemid):
        """
        will remove row form checkedOut table
        if gear requires processing it will move it into the processing table
        else it will update the inventory table to reflect returned gear
        :return:
        """
        pass

    def processItem(self, Itemid):
        """
        will remove item from processing table and update inventory to reflect
        item is now ready to go out
        :param Itemid:
        :return:
        """
        pass

    #TODO: change processing schema to include client ID so we can charge them if it is v broken