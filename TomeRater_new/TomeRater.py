class User:
    def __init__(self, name, email):
        self.name=name
        self.email=email
        self.books={}


    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email=address
        print ("the email of user {} has changed".format(self.name))
        return self.email

    def __repr__(self):
        return  "User {}, email: {}, books read... ".format(self.name,self.email)
    def __eq__(self, other_user):
        if isinstance(other_user, self.__class__):
            return self.name == other_user.name and self.email == other_user.email
        return False  
    def read_book(self,book,rating=None):
        self.books[book]=rating
        #return self.books  
    def get_average_rating(self):
        sum=0
        for v in self.books.values():
            sum+=v
        return sum/float(len(self.books))


class Book:
    def __init__(self, title, isbn):
        self.title=title
        self.isbn=isbn
        self.ratings=[]
    def get_title(self):
        return self.title
    def get_isbn(self) :
        return self.isbn
    def set_isbn(self,new_isbn):
        self.isbn=new_isbn
        print ("the isbn of book {} has changed".format(self.isbn))   
        return self.isbn
    def add_rating(self,rating):
        if (rating>=0)and (rating<=4):           
            self.ratings.append(rating)
        else:
            print ("Invalid Rating")    
    def __eq__(self, other_book):
        if isinstance(other_book, self.__class__):
            return self.title == other_book.title and self.isbn == other_book.isbn
        return False
    def get_average_rating(self):
        sum=0
        for item in self.ratings:
            sum+=item
        return sum/float(len(self.ratings))
    def __hash__(self):
        return hash((self.title, self.isbn))   


class Fiction(Book):
    def __init__(self, title, author,isbn): 
        super().__init__(title, isbn)
        self.author=author
    def get_author(self):
        return self.author
    def __repr__(self):
        return  "{} by {} ".format(self.title,self.author) 

class Non_Fiction(Book):
    def __init__(self, title, subject,level,isbn):
        super().__init__(title, isbn)
        self.subject=subject
        self.level=level
    def get_subject(self):
        return self.subject
    def get_level(self):
        return self.level 
    def __repr__(self):
        return  "{},  a {} manual on {}".format(self.title,self.level,self.subject)

class TomeRater:
    def __init__(self):
        self.users={}
        self.books={}
        
    def create_book(self,title,isbn):
        a=Book(title,isbn)
        return a
    def create_novel(self,title,author,isbn):
        b=Fiction(title,author,isbn)
        return b
    def create_non_fiction(self,title,subject,level,isbn):
        c=Non_Fiction(title,subject,level,isbn)
        return c
    def add_book_to_user(self,book,email,rating=None):
        if email in self.users.keys():
            user=self.users[email]
            user.read_book(book,rating)
            book.add_rating(rating)
        else:
            print ("No user with email {} !".format(email))
        if book in self.books.keys():
            self.books[book]+=1
        else:
            self.books[book]=1
    def add_user(self,name,email,user_books=None):
        u=User(name,email)
        
        self.users[email]=u
        if user_books != None:
            for x in user_books:
                
                self.add_book_to_user(x,email)
    def print_katalog(self):
        for i in self.books.keys():
            print (i)
    def print_users(self):
        for value in self.users.values():
            print (value)
    def most_read_book(self):
        return max(zip(self.books.values(), self.books.keys()))
    def highest_rated_book(self):
        book_aver={}
        for book in self.books.keys():                      
            book_aver[book]=book.get_average_rating()
        return max(zip(book_aver.values(), book_aver.keys()))
    def most_positive_user(self):
        user_aver={}
        for user in sel.users.values():
            user_aver[user]=user.get_average_rating() 
        return max(zip(user_aver.values(), user_aver.keys()))



