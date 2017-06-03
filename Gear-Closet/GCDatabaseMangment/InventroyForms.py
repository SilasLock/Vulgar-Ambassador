from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, validators, SelectField, BooleanField, ValidationError


class AddGeartoInv(FlaskForm):
    itemName = StringField("Item Name", [validators.DataRequired("Please Provide the name of the item")])
    itemQuantity = IntegerField("Item Quantity", [validators.DataRequired("Please Enter how many you wish to add")])
    itemPrice = IntegerField("Item Price", [validators.DataRequired("Please Enter how much this costs")])
    itemCategory = SelectField(label="Catagory", choices=[], validators=[validators.DataRequired("Please Select a catagory")])
    itemProcessingRequired = BooleanField("Requires Additional Checking Processing")
    submit = SubmitField("Add Item")

#Custom Validators
def check_positive(form, field):
    if field.data > 0:
        raise ValidationError('must checkout atleast 1 and no negatives')



class Checkout(FlaskForm):
    """
        Form to checkout a centrain number of items
    """

    numberToCheckOut = IntegerField("",[validators.DataRequired("Please Provide how many you wish to checkout"),check_positive])
    submit = SubmitField("Add to Pack")