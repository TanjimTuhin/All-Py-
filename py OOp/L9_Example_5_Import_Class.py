
class Book:
    def __init__(self, title, author):
        self.name=title
        self.author=author
        self.price=0
    
    #getter setter method =======      
    def set_price(self,price):
        self.price=price
    def get_price(self):
        return self.price
    
    def details(self):
        print("Book Name",self.name,
              "\nAuthor:",self.author,
              "\nPrice:",self.price,"Taka")
# #creating object===========================
# book1=Book("Harry potter", "j k rowling")
# book1.set_price(200)
# book1.details()
# book1.get_price()
# print(book1.get_price())
    
    