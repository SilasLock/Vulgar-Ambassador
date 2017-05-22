import csv,os
import pandas as pd
from GCDatabaseMangment.GCDBSchema import Inventory, db

def loadInventory(filePath):
    """
    :param filePath: path to csv file
    :return: Will load db with inventory from file
    """
    testData = {"data": {}}
    count = 0
    data = pd.read_csv(filePath)
    for row in data.iterrows():
        temp = {'itemPrice': row[1]["Price"], 'itemQuantity': row[1]["Num Avalible"],
                'itemCategory': row[1]["Category"], 'itemName': row[1]["Name"],
                'submit': True, 'itemProcessingRequired': True}
        testData["data"][count] = temp
        count += 1
    return testData


# data = loadInventory(os.curdir+'/inventoryGC.csv')
import json
# with open(os.curdir+ 'inventoryGC.json', 'w') as outfile:
#     json.dump(data, outfile)

with open(os.curdir+ 'inventoryGC.json') as data_file:
    data = json.load(data_file)
for item in data['data'].values():
    print(item)