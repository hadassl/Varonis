class User:
    def __init__(self, uid, username, password):
        self.uid = uid
        self.username = username
        self.password = password

    def get_uid(self):
        return "User(id={'{}')".format(self.uid)

    def get_auth_details(self):
        return {"uid":self.uid, "username": self.username, "password": self.password}


users = []
users.append(User(1,"hadas","test"))

# Get Auth details (username & uid) for all users
usernames = {user.username: user for user in users}
uids = {uid.uid: uid for uid in users}


