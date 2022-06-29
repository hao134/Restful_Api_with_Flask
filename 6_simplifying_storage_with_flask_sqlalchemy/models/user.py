import sqlite3

class UserModel:
    def __init__(self, _id, username, password):
        self.id =_id
        self.username = username
        self.password = password

    # haven't use the user, use the class itself, hence, we choose @classmethod
    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,))
        # get the first row
        row = result.fetchone()
        if row:
            user = cls(*row) #or cls(row[0], row[1], row[2])
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,))
        # get the first row
        row = result.fetchone()
        if row:
            user = cls(*row)  # or cls(row[0], row[1], row[2])
        else:
            user = None

        connection.close()
        return user