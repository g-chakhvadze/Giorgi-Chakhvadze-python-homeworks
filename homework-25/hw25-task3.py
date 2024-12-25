from datetime import datetime

class TimestampMixin:
    def __init__(self):
        self.creation_time = datetime.now()
        self.modification_time = datetime.now()

    def get_creation_time(self):
        return self.creation_time

    def get_modification_time(self):
        return self.modification_time

    def update_modification_time(self):
        self.modification_time = datetime.now()

class File(TimestampMixin):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def rename(self, new_filename):
        self.filename = new_filename
        self.update_modification_time()

class User(TimestampMixin):
    def __init__(self, username):
        super().__init__()
        self.username = username

    def change_username(self, new_username):
        self.username = new_username
        self.update_modification_time()

file = File("example.txt")
user = User("john_doe")

print("File Creation Time:", file.get_creation_time())
print("User Creation Time:", user.get_creation_time())

file.rename("example2.txt")
user.change_username("john_smith")

print("File Modification Time after rename:", file.get_modification_time())
print("User Modification Time after username change:", user.get_modification_time())
