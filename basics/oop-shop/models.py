import permissions

class Category:
    def __init__(self, title):
        self.title = title


class Product:
    def __init__(self, title, price, description, quantity):
        self.title = title
        self.price = price
        self.desc = description
        self.quant = quantity

    def __str__(self):
        return f"{self.title} [{self.quant}] - ${self.price}\n({self.desc[:20]}"

class Comment:
    def __init__(self, user, product, body):
        permissions.login_required(user)
        from datetime import datetime
        self.user = user
        self.product = product
        self.body = body
        self.created_at = datetime.now()

    def __str__(self):
        return f'{self.user.email} [{self.created_at}] = {self.body}'

class User:
    def __init__(self, email, name, sex):
        self.email = email
        self.name = name
        self.sex = sex
        self.__password = None
        self.is_auth = False
        print(f"Succes создан юзер {self.email}")

    def register(self, password, password_confirm):
        if password != password_confirm:
            raise Exception("Пароль не совпадает")
        self.__password = password
        print(f"Succes reg {self.email}")

    def login(self, password):
        if self.__password != password:
            raise Exception("Пароль не верный")
        self.is_auth = True
        print(f"Success log {self.email}")

    def logout(self):
        permissions.login_required(self)
        self.is_auth = False
        print(f"Succes вышел {self.email}")

    def __str__(self):
        return self.email
