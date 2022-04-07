from dataclasses import dataclass
# задание 1 (создание класса данных)
@dataclass
class BookForTask1():
    name: str
    author: str
    year: int

# задание 2 (staticmethod)     
class BookForTask2():
    def __init__(self, name: str, author: str, year: int):
        self.name = name
        self.author = author
        self.year = year
    
    @staticmethod
    def compare(first_book, second_book):
        if first_book.year > second_book.year:
            return f'{second_book.name} вышла раньше, чем {first_book.name}!'
        else:
            return f'{first_book.name} вышла раньше, чем {second_book.name}!'

# задание 3 (classmethod)
class BookForTask3():
    count = 0
    
    def __init__(self):
         BookForTask3.count += 1
    
    @classmethod
    def reset_progress(cls):
        cls.count = 0

# проверка dataclass
book1 = BookForTask1("book_name1", "author_of_book1", 1888)
book2 = BookForTask1("book_name2", "author_of_book2", 1900)
print(book1)
print(book2)

# проверка staticmethod
book3 = BookForTask2("book_name3", "author_of_book3", 1768)
book4 = BookForTask2("book_name4", "author_of_book4", 1546)
print(BookForTask2.compare(book3, book4)) 

# проверка classmethod
a = BookForTask3()
a = BookForTask3()
a = BookForTask3()
a = BookForTask3()
print(a.count)

BookForTask3.reset_progress(0)
print(BookForTask3.count)