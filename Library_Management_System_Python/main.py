# Define a Library class
class Library:

    def __init__(self, books):
        self.books = books

    # Display available books in the library
    def show_avail_books(self):
        print('Our Library Can Offer You The Following Books:')
        print('================================================')
        for book, borrower in self.books.items():
            if borrower == 'Free':
                print(book)

    def lend_book(self, requested_book, name):
        # Check if the requested book exists in the library
        if requested_book in self.books:
            if self.books[requested_book] == 'Free':
                print(f'{requested_book} has been marked as \'Borrowed\' by: {name}')
                self.books[requested_book] = name
                return True
            else:
                print(f'Sorry, {requested_book} is currently on loan to: {self.books[requested_book]}')
                return False
        else:
            print(f'Sorry, {requested_book} is not available in the library.')
            return False

    # Return a book to the library
    def return_book(self, returned_book):
        self.books[returned_book] = 'Free'
        print(f'Thanks for returning {returned_book}')


# Define a Student class
class Student:

    def __init__(self, name, library):
        self.name = name
        self.books = []
        self.library = library

    # View books borrowed by the student
    def view_borrowed(self):
        if not self.books:
            print('You haven\'t borrowed any books')
        else:
            for book in self.books:
                print(book)

    # Request to borrow a book from the library
    def request_book(self):
        book = input('Enter the name of the book you\'d like to borrow >> ')
        if self.library.lend_book(book, self.name):
            self.books.append(book)

    # Return a borrowed book to the library
    def return_book(self):
        book = input('Enter the name of the book you\'d like to return >> ')
        if book in self.books:
            self.library.return_book(book)
        else:
            print('You haven\'t borrowed that book. Please try another...')


# Function to create a library and interact with a student
def create_lib():
    books = {
        'The Last Battle': 'Free',
        'The Hunger Games': 'Free',
        'Cracking the Coding Interview': 'Free'
    }
    library = Library(books)
    student_example = Student('Your Name', library)

    while True:
        print('''
           ==========LIBRARY MENU===========
           1. Display Available Books
           2. Borrow a Book
           3. Return a Book
           4. View Your Books
           5. Exit'''
              )

        # Get user choice
        choice = int(input('Enter Choice: '))

        # Process user choice
        if choice == 1:
            print()
            library.show_avail_books()
        elif choice == 2:
            print()
            student_example.request_book()
        elif choice == 3:
            print()
            student_example.return_book()
        elif choice == 4:
            print()
            student_example.view_borrowed()
        elif choice == 5:
            print('Goodbye')
            exit()


if __name__ == '__main__':
    create_lib()
