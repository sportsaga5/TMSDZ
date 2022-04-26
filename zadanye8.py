class Parent:
    """Родитель в прямом смысле слова"""
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def say_hello(self):
        return f'Привет, меня зовут {self.name} и я родитель!' # метод родителя

    def say_bye(self):
        return f'Пока!' # метод родителя

    def __str__(self):
        return f'Это родитель с именем: {self.name} и возрастом: {self.age}!' # переопределение __str__

parent1 = Parent("Billy", 40)

print(parent1.say_hello())

# создание класса наследника
class FirstTwin(Parent):
    """Первый из детей близнецов с игрушкой"""
    def __init__(self, lovely_toy: str, **kwargs):
        self.lovely_toy = lovely_toy
        super().__init__(**kwargs)

    def say_hello(self):
        return f'Привет, меня зовут {self.name} и я ребёнок!'  # переопределение метода родителя
    
    def my_lovely_toy(self):
        return f'Моя любимая игрушка это - {self.lovely_toy}!' # его собственный метод

    def __str__(self):
        return f'Это ребёнок с именем: {self.name} и возрастом: {self.age} и любимой игрушкой: {self.lovely_toy}!' # переопределение __str__

class SecondTwin(Parent):
    """Второй из детей близнецов с хобби"""
    def __init__(self, hobby: str, **kwargs):
        self.hobby = hobby
        super().__init__(**kwargs)

    def say_hello(self):
        return f'Привет, меня зовут {self.name} и я ребёнок!'  # переопределение метода родителя

    def my_hobby(self):
        return f'Моё хобби это - {self.hobby}!' # его собственный метод

    def __str__(self):
        return f'Это ребёнок с именем: {self.name} и возрастом: {self.age} и хобби: {self.hobby}!' # переопределение __str__

# близнец 1
twin1=FirstTwin(
    name = "Helly",
    age = 10,
    lovely_toy = "машина"
)

# близнец 2
twin2=SecondTwin(
    name = "Selly",
    age = 10,
    hobby = "футбол"
)

# проверка
print(twin1.say_hello())
print(twin1.my_lovely_toy())
print(twin2.say_hello())
print(twin2.my_hobby())

class Little_kid(FirstTwin, SecondTwin):
    """Младший ребёнок с наследованием от 2 близнецов"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

# младший брат   
little_brother=Little_kid(
    name = "Ben",
    age = 5,
    lovely_toy = "вертолёт",
    hobby = "баскетбол"
)

# проверка
print(little_brother.say_hello())
print(little_brother.my_lovely_toy())
print(little_brother.my_hobby())