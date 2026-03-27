from database import users, pcs, assignments

def userValidation(user_id):
    for i in users:
        if i["user_id"] == user_id: return True
    return False

def serialNumberValidation(serialNumber):
    for i in pcs:
        if i["serialNumber"] == serialNumber: return True
    return False

def assignmentValidation(is_active):
    for i in assignments:
        if i["is_active"] == 1: return True
    return False

