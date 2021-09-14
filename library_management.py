class Library:
    def __init__(self, list_of_books, name_of_library): #created a constructor that will take arg as list of books and name of library
        self.list_of_books = list_of_books
        self.name_of_library = name_of_library
        self.issued_book=[]

    def display_book(self):# method to display all the books available in library
        for items in self.list_of_books:
             print(items)
        return "This are the books we have"
    def add_book(self, new_book):#method if user wants to add some books to current library books stock
         self.list_of_books.append(new_book.capitalize())#in case if user enter lowercase letter it must be capitalize
    def issue_book(self, book):#method if user want to issue book from library 
        if book in self.list_of_books:#in case if book that user wants to be issued is available in library
            self.issued_book.append(book)#append that book(which user wants)in issued book list
            self.list_of_books.remove(book)#and remove that book(which user wants)from current library books stock
            print("Book has been issued to you...")
        elif book in self.issued_book:#if in case book(that user wants)is available in issue book list that means that book is already being issued by someone else
            print("Sorry the book is already been issued\n"
                  "Currently we only have these:- ")
            for items in self.list_of_books:#displays all the reamining books that is available in library
                print(items)
        else:#if in case book(which user wants) not available in library books stock 
            print("Book's name entered is not available or name is wrong "
                  "and the available books are:- ")
            for items in self.list_of_books:
                print(items)


def system():
    try:
        value = True
        CityLibrary = Library(["Brief History of Time", "Game of thrones", "Twilight", "MiddleMarch"], "CityLibrary")

        while value == True:#infinite while loop asking for user name
            user_name = input("Enter your name:- ")

            user_input = eval(input(f"Welcome {user_name} to {CityLibrary.name_of_library} \n"
                                    f"Enter (1) To display books we have\n"
                                    f"Enter (2) To donate a book \n"
                                    f"Enter (3) To issue a book\n"
                                    f"Enter (4) To return a book\n"
                                    f"Enter (5) For exit"
                                    f":- "))

            if user_input == 1:
                print(CityLibrary.display_book())

            elif user_input == 2:
                new_book = input("Enter name of book you want to donate:- ")
                CityLibrary.add_book(new_book.capitalize())
                print( "Book has been added thank you for your donation")


            elif user_input == 3:
                book = input("Enter the name of book you want to issue:- ")
                CityLibrary.issue_book(book.capitalize())


            elif user_input == 4:
                new_book = input("Enter the name of book you want to return:- ")
                CityLibrary.add_book(new_book.capitalize())
                print("Thank you for returning book hope to se you soon")
            elif user_input == 5:
                value = False
            else:
                print("Wrong input has been entered:- ")
    except:
        print("Error!!!")
        system()
system()
