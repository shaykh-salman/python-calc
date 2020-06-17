allUsers = []


def isUserPresent(user):
    print(allUsers);
    print(user)
    if user in allUsers:
        return True;
    return False;


def addUser(user):
    allUsers.append(user);
    return True;


def removeUser(user):
    allUsers.remove(user);
