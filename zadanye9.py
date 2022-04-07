from dataclasses import dataclass
# задание 1 (создание класса данных)
@dataclass
class Book_for_task1():
    name: str
    author: str
    year: int

# задание 2 (staticmethod)     
class Book_for_task2():
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
class Book_for_task3():
    count = 0
    
    def __init__(self):
         Book_for_task3.count += 1
    
    @classmethod
    def reset_progress(cls, value):
        cls.count = value

# проверка dataclass
book1 = Book_for_task1("book_name1", "author_of_book1", 1888)
book2 = Book_for_task1("book_name2", "author_of_book2", 1900)
print(book1)
print(book2)

# проверка staticmethod
book3 = Book_for_task2("book_name3", "author_of_book3", 1768)
book4 = Book_for_task2("book_name4", "author_of_book4", 1546)
print(Book_for_task2.compare(book3, book4)) 

# проверка classmethod
a = Book_for_task3()
a = Book_for_task3()
a = Book_for_task3()
a = Book_for_task3()
print(a.count)

Book_for_task3.reset_progress(0)
print(Book_for_task3.count)