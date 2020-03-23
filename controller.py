from model import *

def retrieve_stored_data():
    return dataStorage

def insert_data(key, input):
    # Data should be in a (Key as a string, tuple(datetime, value)) format
    if(isinstance(key, str) == False or isinstance(input, tuple) == False):
        errorMessage = "insertData failed input type verification. Data should be in a (Key as a string, List(datetime, value)) format"
        print(errorMessage)
        return False
    if key in dataStorage:
        data = dataStorage[key]
        data.append(input)
        dataStorage.update({key: data})
    else:
        dataStorage.update({key: [input]})
    return True

def delete_all_stored_data():
    dataStorage.clear()

def delete_key_stored_data(key):
    if key in dataStorage:
        del dataStorage[key]


