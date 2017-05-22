import qrcode, PIL

def makeCode(itemName, itemQuanity=1):
    """
    :param itemName, itemQuanity: item name is the name for the item and item quanity
        is how many you wish to add to the inventory
    :return: Creates QR jpeg and adds line to csv file
    """
    qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H, #About 30% or less errors can be corrected ie. if the code
                                                       # is broken less than 30% it can still be used
    )
    qr.add_data(itemName)
    qr.make(fit=True)
    img = qr.make_image()


#  Workflow Outline
#  http://stackoverflow.com/questions/31849494/serve-image-stored-in-sqlalchemy-largebinary-column
#  Fetures we need:
#  Add to inv
#  Remove from inv
#  check in/out from inv
#  When we add to inv check to see if it is inv yet if yes figure out what id to generate
#  when we update inv provide 2 step check in for some items
#  need to create multiple pages use blue print stratagy for this
