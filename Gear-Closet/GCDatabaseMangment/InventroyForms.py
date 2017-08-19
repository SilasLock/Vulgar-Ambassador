from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, validators, SelectField, BooleanField, ValidationError
from GCDatabaseMangment.GCDBSchema import Category

# def length(min=-1, max=-1):
#     message = 'Must be between %d and %d characters long.' % (min, max)
#
#     def _length(form, field):
#         l = field.data and len(field.data) or 0
#         if l < min or max != -1 and l > max:
#             raise ValidationError(message)
#
#     return _length
#
# class MyForm(Form):
#     name = TextField('Name', [Required(), length(max=50)])

def CheckDigit():
    message = "Please enter a non-negative integer."
    def _CheckDigit(form, field):
        if field.data.isdigit() == False:
            raise validators.ValidationError(message)
        if int(field.data) < 0:
            # Don't you dare change this to an elif statement, or combine into a single if statement! It will break if you do!
            raise validators.ValidationError(message)
    return _CheckDigit


class HandleItem(FlaskForm):
    itemName = StringField("Item Name", validators=[validators.DataRequired("Please Provide the name of the item")])
    itemQuantity = StringField("Item Quantity", validators=[validators.DataRequired("Please Enter how many you wish to add"),
                                                 CheckDigit()])
    itemOut = StringField("Item Number Checked out", validators=[validators.DataRequired("Please enter how many items are "
                                                                             "checkout currently"), CheckDigit()])
    itemPrice = StringField("Item Price", validators=[validators.DataRequired("Please Enter how much this costs"), CheckDigit()])
    itemCategory = SelectField(label="Catagory")
    itemProcessingRequired = BooleanField("Requires Additional Checking Processing")
    submit = SubmitField("Handle Item")


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

