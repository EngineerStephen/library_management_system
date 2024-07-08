

# Library Management System

This Python program simulates a Library Management System where users can perform various operations related to books, users, and authors. It provides an interactive command-line interface (CLI) for easy navigation and operation.

## Features

- **Book Operations:**
  - Add new books to the library.
  - Borrow books from the library.
  - Return borrowed books.
  - Search for books in the library.

- **User Operations:**
  - Add new users to the system.
  - View details of a specific user.
  - Display all users in the system.

- **Author Operations:**
  - Add new authors to the system.
  - View details of a specific author.
  - Display all authors in the system.

## Modules and Classes

The program is structured using multiple modules and classes:

- **user_interaction.py:** Contains the `UserInteraction` class and functions for displaying menus (`display_menu`, `display_book_operations`, `display_user_operations`, `display_author_operations`).

- **book.py:** Defines the `Book_Operations` class and functions for book-related operations (`add_new_book`, `borrowing_book`, `return_book`, `search_book`).

- **user.py:** Implements the `User_Operations` class and functions for user-related operations (`add_new_user`, `view_user_details`, `all_users`).

- **author.py:** Includes the `Author_Operations` class and functions for author-related operations (`add_new_author`, `view_author_details`, `all_authors`).

## Getting Started

To run the program, ensure you have Python installed on your machine. Clone the repository and navigate to the directory where the program files are located. Execute the following command to start the program:

python library_management.py

Follow the on-screen prompts to navigate through different menu options and perform operations related to books, users, and authors.

## Dependencies

This program requires Python 3.x and does not have any additional dependencies beyond the standard library.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.
