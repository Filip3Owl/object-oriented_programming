class Book:
    created_books = 0  # atributo da classe

    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def create_book(cls, title, author):
        new_book = cls(title, author)  # cria nova instância
        cls.created_books += 1  # incrementa contador da CLASSE
        print(f"Created book: {new_book.title} by {new_book.author}")
        return new_book

    @classmethod
    def book_number(cls):
        print(f"Total de livros criados: {cls.created_books}")

Book.create_book("1984", "George Orwell")