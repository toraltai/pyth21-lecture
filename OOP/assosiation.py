"=================Ассоциация================="
# Ассоциая - принцип ООП, в котором ва класса друг с другом связаны
# ассоциация делится на 2 принциппа:
# 1 - агрегация (более слабая связь)
# 2 - композиция (более сильная связь)

class Battery:
    power = 100

    def charge(self):
        if self.power < 100:
            self.power = 100

class Iphone:
    def __init__(self, color:str):
        self.color = color
        # когда мы создаем oбьект от другого класса прям внутри другого - тесная связь(композиция)
        self.battery = Battery()

class Nokia:
    def __init__(self, color:str, battery:Battery):
        self.color = color
        self.battery = battery
        #когда мы принимаем уже созданный вне класса обьект - агрегация

        