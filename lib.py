class Book:
    def __init__(self, title, author, is_issued=False):
        self.title = title
        self.author = author
        self.is_issued = is_issued

    def __str__(self):
        status = "Issued" if self.is_issued else "Available"
        return f"Title: {self.title} | Author: {self.author} | Status: {status}"


class Library:
    def __init__(self):
        self.books = []
        self.load_books()

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author name: ")

        book = Book(title, author)
        self.books.append(book)

        print(" Book added successfully!")

    def view_books(self):
        if not self.books:
            print(" No books available.")
            return

        print("\n--- Library Books ---")
        for i, book in enumerate(self.books, start=1):
            print(f"{i}. {book}")

    def search_book(self):
        title = input("Enter book title to search: ")

        for book in self.books:
            if book.title.lower() == title.lower():
                print("\nBook Found:")
                print(book)
                return

        print("Book not found.")

    def issue_book(self):
        title = input("Enter book title to issue: ")

        for book in self.books:
            if book.title.lower() == title.lower():

                if not book.is_issued:
                    book.is_issued = True
                    print(" Book issued successfully.")
                else:
                    print(" Book is already issued.")

                return

        print(" Book not found.")

    def return_book(self):
        title = input("Enter book title to return: ")

        for book in self.books:
            if book.title.lower() == title.lower():

                if book.is_issued:
                    book.is_issued = False
                    print(" Book returned successfully.")
                else:
                    print(" This book was not issued.")

                return

        print(" Book not found.")

    def save_books(self):
        with open("library.txt", "w") as file:
            for book in self.books:
                file.write(
                    f"{book.title},{book.author},{book.is_issued}\n"
                )

    def load_books(self):
        try:
            with open("library.txt", "r") as file:
                for line in file:
                    title, author, status = line.strip().split(",")

                    book = Book(
                        title,
                        author,
                        status == "True"
                    )

                    self.books.append(book)

        except FileNotFoundError:
            pass


def main():
    library = Library()

    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            library.add_book()

        elif choice == "2":
            library.view_books()

        elif choice == "3":
            library.search_book()

        elif choice == "4":
            library.issue_book()

        elif choice == "5":
            library.return_book()

        elif choice == "6":
            library.save_books()
            print(" Data saved successfully.")
            print(" Goodbye!")
            break

        else:
            print(" Invalid choice. Try again.")


if __name__ == "__main__":
    main()