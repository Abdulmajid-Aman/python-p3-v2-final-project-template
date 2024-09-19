from models.__init__ import CONN, CURSOR

class User:

    all = {}

    def __init__(self, name, id = None):
        self.id = id
        self.name = name

    def __repr__(self):
        print(f"< Name: ({self.name}) >")

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if type(name) is str and len(name):
            self._name = name

        else:
            raise ValueError("Invalid name")
        
    @classmethod
    def create(cls, name):
        user = cls(name)
        user.insert_table_data()
        return user
        
    @classmethod
    def create_table(cls):
        sql = """ CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT) """

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """ DROP TABLE IF EXISTS users """

        CURSOR.execute(sql)
        CONN.commit()


    def insert_table_data(self):
        sql = """ INSERT INTO users(name) VALUES(?) """

        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self


    def updating_table_data(self):
        sql = """ UPDATE users SET name = ? WHERE id = ? """

        CURSOR.execute(sql, (self.name, self.id))

    def delete_data(self):
        sql  = """ DELETE FROM users WHERE id = ? """

        CURSOR.execute(sql)
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        user = cls.all.get(row[0])

        if user:
            user.name = row[1]
        else:
            user = cls(row[1])
            user.id = row[0]
            cls.all[user.id] = user
        return user
    
    @classmethod
    def get_all(cls):
        sql = """ SELECT * FROM users """

        users = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(user) for user in users] if users else None

    @classmethod
    def find_by_id(cls, id):
        sql = """ SELECT * FROM users WHERE id = ? """


        user = CURSOR.execute(sql, (id,)).fetchone()
        return user
    
