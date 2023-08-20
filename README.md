# Flask Blog Management Application

This is a Flask application that allows users to manage blog posts. The application uses custom-created data structures like LinkedList, Queue, Stack, HashTable, and a Binary Search Tree to organize and manipulate data. Users can create, retrieve, update, and delete both users and blog posts through various routes provided by the application.

## Features

- Create users with their name, email, address, and phone number.
- Retrieve a list of all users in descending and ascending order of their IDs.
- Retrieve information about a specific user by their ID.
- Delete a user by their ID.
- Create blog posts associated with a user.
- Retrieve information about a specific blog post by its ID.
- Convert the bodies of blog posts into numeric values.
- Delete the last 10 blog posts.

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/Ihor-Pryyma/flask_blog_management_app.git
    cd flask_blog_management_app
    ```

2. Create and activate a virtual environment:

    ```
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

4. Initialize the database:

   After setting up the virtual environment, you need to initialize the database. Open a Python shell or a script and run the following commands:

   ```python
   from server import db
   db.create_all()

Run the Flask application:

    python server.py

   The application will start running on `http://127.0.0.1:5000/`.

## Routes

- **POST /user**: Create a new user.
- **GET /user/descending_id**: Retrieve a list of all users in descending order of their IDs.
- **GET /user/ascending_id**: Retrieve a list of all users in ascending order of their IDs.
- **GET /user/<user_id>**: Retrieve information about a specific user by their ID.
- **DELETE /user/<user_id>**: Delete a user by their ID.
- **POST /blog_post/<user_id>**: Create a new blog post associated with a user.
- **GET /blog_post/<blog_post_id>**: Retrieve information about a specific blog post by its ID.
- **GET /blog_post/numeric_body**: Convert the bodies of blog posts into numeric values.
- **DELETE /blog_post/delete_last_10**: Delete the last 10 blog posts.

## Data Structures

- `linked_list.py`: Implementation of a singly linked list.
- `hash_table.py`: Implementation of a hash table.
- `binary_search_tree.py`: Implementation of a binary search tree.
- `custom_queue.py`: Implementation of a custom queue.
- `custom_stack.py`: Implementation of a custom stack.

## Technologies Used

- Flask: Web framework used for building the application.
- SQLAlchemy: Used for database interaction.
- SQLite: Used as the database backend.
- Python: Programming language used for the application logic.

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Create a pull request to the main repository.

## License

This project is licensed under the [MIT License](LICENSE).
