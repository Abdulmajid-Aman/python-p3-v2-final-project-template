from models.__init__ import CONN, CURSOR
from models.user import User
 

class Todo:

    all = {}

    def __init__(self, todo, user_id, id = None, status = 'Not Done !!!'):
        self.id = id
        self.todo = todo
        self.user_id = user_id
        self.status = status

    def __repr__(self):
        return f"< Todo: ({self.todo}) User_id: ({self.user_id}) Status: ({self.status}) >"

    @property
    def todo(self):
        return self._todo
    
    @todo.setter
    def todo(self, todo):
        if type(todo) is str and len(todo):
            self._todo = todo
        else:
            raise TypeError("Todo must be a string and not empty")
        
    @property
    def user_id(self):
        return self._user_id
    
    @user_id.setter
    def user_id(self, id):
        if type(id) is int and User.find_by_id(id):
            self._user_id = id
        else:
            raise TypeError('User_id must be an integer and be in users table')

    @classmethod
    def create_table(cls):
        sql = """ CREATE TABLE IF NOT EXISTS todos(id INTEGER PRIMARY KEY, todo TEXT, status TEXT, user_id INTEGER, FOREIGN KEY(user_id) REFERENCES users(id))"""

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """ DROP TABLE IF EXISTS todos """

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create(cls, todo, user_id):
        todo = cls(todo, user_id)
        todo.save()
        return todo

    def save(self):
        sql = """ INSERT INTO todos (todo, user_id, status) VALUES (?, ?, ?) """

        CURSOR.execute(sql, (self.todo, self.user_id, self.status))
        CONN.commit()
        
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """ UPDATE todos SET todo = ?, user_id = ?  WHERE id = ? """

        CURSOR.execute(sql, (self.todo, self.user_id, self.id))
        CONN.commit()

    def delete(self):
        sql = """ DELETE FROM todos WHERE id = ? """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        todo = cls.all.get(row[0])

        if todo:
            todo.todo = row[1]
            todo.user_id = row[2]
            todo.status = row[3]
        else:
            todo = cls(row[1], row[3], row[2])
            todo.id = row[0]
            cls.all[row[0]] = todo
        return todo
    
    @classmethod
    def get_all_todo(cls):
        sql = """ SELECT * FROM todos """

        todos = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(todo) for todo in todos]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """ SELECT * FROM todos WHERE id = ? """

        todo = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(todo)

    @classmethod
    def completed_todo(cls, id):
        sql = """ UPDATE todos SET status = 'Done!!!' WHERE id = ? """

        CURSOR.execute(sql, (id,)).fetchone()
        CONN.commit()
        todo = Todo.find_by_id(id)
        todo.status = 'Done!!!'
        return todo
    
    @classmethod
    def find_by_user_id(cls, user_id):
        sql = """ SELECT * FROM todos WHERE user_id = ? AND user_id = ? """
        CURSOR.execute(sql, (user_id, user_id))
        todos = CURSOR.fetchall()
        return [cls.instance_from_db(todo) for todo in todos]