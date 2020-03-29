from controller import *

def test_insert_data():
    assert insert_data(1,1) == False
    assert insert_data("testInput", 1) == False
    assert insert_data(1, ("datetime", 1020)) == False

    insert_data("testKey", ("datetime", 1020))
    assert retrieve_stored_data().get("testKey") == [("datetime", 1020)]
    

def test_remove_all_data():
    insert_data("testKey", ("datetime", 1020))
    insert_data("testKey2", ("datetime", 1021))
    insert_data("testKey3", ("datetime", 1022))

    delete_all_stored_data()
    assert retrieve_stored_data() == {}

def test_delete_single_key():
    insert_data("testKey", ("datetime", 1020))
    insert_data("testKey2", ("datetime", 1021))
    insert_data("testKey3", ("datetime", 1022))

    delete_key_stored_data("testKey2")
    assert retrieve_stored_data() == {'testKey': [('datetime', 1020)], 'testKey3': [('datetime', 1022)]}
