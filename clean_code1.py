
class Book:
    def __init__(self, title, author, price, isbn, stock):
        self.title = title
        self.author = author
        self.price = price
        self.isbn = isbn
        self.stock = stock

    def check_availability(self):
        return self.stock > 0

    def update_stock(self, quantity):
        if quantity >= 0:
            self.stock = quantity
        else:
            raise ValueError("Stock quantity cannot be negative.")


if __name__ == "__main__":

    book1 = Book("1984", "George Orwell", 9.99, "9780451524935", 10)
    
    print(f"Availability: {book1.check_availability()}")
    book1.update_stock(5)
    print(f"New Stock: {book1.stock}")


