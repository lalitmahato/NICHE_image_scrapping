from db_configuration import db
# Check if the data is into the database or not
def look_in_db(collection_objet, name_ins):
    status = [i for i in collection_objet.find({'Institute_Name': name_ins})]
    # print(status)
    # print('length:', len(status))
    if len(status) >= 1 :
        # print(True)
        return False # return False if the data is already exist into the database
    else:
        # print(False)
        return True # return True if the data is not exist into the database


def check_availability(name_ins, collection):
    collection_record = db[collection]
    status = look_in_db(collection_record, name_ins)
    return status

## To check
# look_in_db(db["College_Details"], "Aaniiih Nakoda College")
# check_availability("Aaniiih Nakoda College","College_Details")


    
    