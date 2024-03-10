namePass = []
def changeUser(newUsername):
    if newUsername == "":
        return 0

    elif newUsername in namePass:
        return 0

