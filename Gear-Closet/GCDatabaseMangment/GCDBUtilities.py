#This file contatins methods useful for minipulating db transactions that dont have to do with
#actual changes to db or to SQLalchmey objects

def backpackToCart(backpack):
    """
    :param backpack: a list of dictionaries of form
     [{"itemName":item.itemName, "id":item.id, "numToCheckout":int(form.data['numberToCheckout'])}]
    :return:
    """

