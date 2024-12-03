class Book:
    def __init__(self, title: str, author: str, genre: str, time_of_publication: int):
        self.current_year: int = 2024
        self.title: str = title
        self.author: str = author
        self.genre: str = genre
        self.time_of_publication: int = int(time_of_publication)
        self.book_age = self.age()

    def age(self):
        return self.current_year - self.time_of_publication

    def __str__(self):
        return f"{self.title} by {self.author} is now {self.book_age} years old."

book_list = input().split(", ")
book = Book(*book_list)
print(book)