class Book:
    def __init__(self,title, author, price,stock_status):
        self.title = title
        self.author = author
        self.price = price
        self.stock_status = stock_status

    def __str__(self):
        return f"{self.title} by {self.author}"
    

    def check_availability(self):
        if self.stock_status > 0:
            return True
        else: 
            return False
        

    def borrow_book(self):
        if self.stock_status > 0:
            self.stock_status -= 1
            print(f"{self.title} has been borrowed.")
        else:
            print(f"Sorry {self.title} is out of stock")

    def return_book(self):
        self.stock_status += 1
        print(f"{self.title} returned")

        
        