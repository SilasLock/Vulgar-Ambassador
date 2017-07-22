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
    if int(field.data) > 0:
        raise ValidationError('must checkout atleast 1 and no negatives')



class Checkout(FlaskForm):
    """
        Form to checkout a centrain number of items
    """
    numberToCheckout = SelectField("Number to check out", choices=[(0,0)])
    submit = SubmitField("Add to Pack")

class CreateClient(FlaskForm):
    clientName = StringField("Client Name", [validators.DataRequired("Please Provide the name of the item")])
    studentID = IntegerField("student ID", [validators.DataRequired("Please Enter student ID")])
    emailAddress = StringField("Client Email", [validators.DataRequired("Please enter email adress")])
    phoneNumber = IntegerField("Client Phone Number", [validators.DataRequired("Please provide a client phone number")])
    Employee = BooleanField("Are they an Employee")
    submit = SubmitField("Add Client")