# Wow API

Wow API is a backend application that serves as the core component for an e-commerce platform that provides a seamless shopping experience for users. It comprises a set of RESTful API endpoints to manage user accounts, secure authentication, order management, product listings and user reviews.

## Features

- User registration and authentication
- User management (create, update, delete)
- Product listing management (create, update, delete)
- Order management (create, update, delete)
- User reviews management (create, update)
- User authentication using JSON Web Tokens (JWT)
- Password hashing for secure storage

## Technologies Used

- Python: the primary programming language used for the application
- FastAPI: a modern, fast (high-performance) web framework for building APIs with Python
- SQLAlchemy: an SQL toolkit and Object-Relational Mapping (ORM) library
- PostgreSQL: a powerful, open-source relational database
- Docker: a containerization platform used for easy deployment and scalability
- JWT: JSON Web Tokens for user authentication and authorization
<!-- - Pytest: a testing framework for running unit tests -->

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/evans-nyang/wow.git
    ```

2. Navigate to the project directory:

   ```bash
   cd wow
   ```

3. Build and run the Docker containers:

   ```bash
   docker compose up --build
   ```

4. The application will be running on `http://localhost:8000`

## API Documentation

The API documentation can be accessed through the Swagger UI interface. Open your browser and visit the following URL:

  ```bash
  http://localhost:8000/docs
  ```

The Swagger UI provides an interactive interface to explore and test the available API endpoints.

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## Contact

For any inquiries or questions, please contact the project maintainers:

- Johnevans Nyawanga (<nyangjohnevans@outlook.com>)

Feel free to reach out if you need any assistance or have any feedback.
