from GCDatabaseMangment.InventroyForms import AddGeartoInv
from flask import  request, redirect, url_for, \
     render_template, flash,Blueprint, jsonify
from GCDatabaseMangment.GCDBSchema import db, Inventory, Processing, Client, Category, checkedOut
GCInv = Blueprint('GCInv', __name__, template_folder='templates')


# # Page contains check in and checkout functionality
# @GCInv.route('/', methods=['GET', 'POST'])
# def Main():
#     form = AddGeartoInv()
#     form.itemCategory.choices=[("a","a"),("b","b")]
#     form.itemCategory.choices.insert(0, ("", "Some default value...")) #TODO: Write custom query class for Category to return names in this format
#
#     if request.method == 'POST':
#         # print(form.data)  # returns a dictonary with keys that are the feilds in the table
#         if form.validate() == False:
#             flash('All fields are required.')
#             return render_template('GCmain.html', form=form)
#         else:
#             # print(form.data)
#             itemModel = Inventory(form=form.data)
#             db.session.add(itemModel)
#             db.session.commit()
#             # model = TripModel(form.data)
#             # model.addModel()  # add trip to db
#             # db.session.commit()
#             flash('New entry was successfully posted')
#             return redirect(url_for('GCInv.Main'))  # Im going to be honest this naming schema is terible
#     elif request.method == 'GET':
#         return render_template('GCmain.html', form=form)
#
# # Page contains inventory and ability to edit it
# @GCInv.route('/inventory', methods=['GET','POST'])
# def Inventory():
#     #TODO: add a cool inventory table using javasricpt so that we can edit items in the table
#     return "Cool stuff coming"
#
# @GCInv.route('/checkedOut', methods=['GET', 'POST'])
# def checkedOut():
#     #TODO add a feture to see who has checked out gear
#     return "Cool stuff coming soon"




# http://flask.pocoo.org/docs/0.12/patterns/jquery/
@GCInv.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

@GCInv.route('/')
def index():
    return render_template('testAJAX.html')

@GCInv.route("/table")
def table():
    return render_template('testTable.html')