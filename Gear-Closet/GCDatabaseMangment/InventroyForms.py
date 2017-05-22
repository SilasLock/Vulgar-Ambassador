from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, validators, SelectField, BooleanField


class AddGeartoInv(FlaskForm):
    itemName = StringField("Item Name", [validators.DataRequired("Please Provide the name of the item")])
    itemQuantity = IntegerField("Item Quantity", [validators.DataRequired("Please Enter how many you wish to add")])
    itemPrice = IntegerField("Item Price", [validators.DataRequired("Please Enter how much this costs")])
    itemCategory = SelectField(label="Catagory", choices=[], validators=[validators.DataRequired("Please Select a catagory")])
    itemProcessingRequired = BooleanField("Requires Additional Checking Processing")
    submit = SubmitField("Add Item")

