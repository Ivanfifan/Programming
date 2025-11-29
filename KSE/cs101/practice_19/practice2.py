import json

class PasswordManager:
    def __init__(self,file_name):
        self.file_name = file_name
        try:
            with open(self.file_name, "r") as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = {}

    def save(self):
        with open(self.file_name, 'w') as f:
            json.dump(self.data, f)

    def get(self, src):
        try:
            return f'Login:{self.data[src]['login']}, Password:{self.data[src]['password']}'
        except KeyError:
            return {}

    def set_val(self, src, login, password):
        if src in self.data:
            print("Key already exists")
            return

        self.data[src] = {"login": login, "password": password}
        self.save()
        print("Success")

    def update(self, src, login, password):
        if src not in self.data:
            print("Key does not exist")
            return

        self.data[src] = {"login": login, "password": password}
        self.save()
        print("Success")

    def delete(self, src):
        try:
            del self.data[src]
            self.save()
        except KeyError:
            pass

def get_input():
    src = input("Enter source: ")
    login = input("Enter login: ")
    password = input("Enter password: ")
    return src, login, password

manager = PasswordManager('db.json')

while True:
    command = input("Enter command (get, set, update, delete, exit) >>> ")

    if command == "get":
        src = input("Enter source: ")
        print(manager.get(src))

    elif command == "set":
        src, login, password = get_input()
        manager.set_val(src, login, password)

    elif command == "update":
        src, login, password = get_input()
        manager.update(src, login, password)

    elif command == "delete":
        src = input("Enter source to delete: ")
        manager.delete(src)

    elif command == "exit":
        break
    else:
        print("Invalid command")
