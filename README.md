# Wow API

Wow API is a backend application that serves as the core component for an e-commerce platform that provides a seamless shopping experience for users. It comprises a set of RESTful API endpoints to manage user accounts, secure authentication, order management, product listings and user reviews.

## Features

- **Authentication**: Secure user authentication and authorization for accessing protected endpoints.
- **Orders**: Create, update, and manage orders for products.
- **Products**: Browse, search, and view product listings with detailed information.
- **Reviews**: Users can leave reviews and ratings for products.
- **Users**: Manage user accounts, profiles, and personal information.

## Technologies Used

- Python: the primary programming language used for the application
- FastAPI: a modern, fast (high-performance) web framework for building APIs with Python
- SQLAlchemy: an SQL toolkit and Object-Relational Mapping (ORM) library
- PostgreSQL: a powerful, open-source relational database
- Docker: a containerization platform used for easy deployment and scalability
- Docker Compose: a tool for defining and running multi-container Docker applications
- JWT: JSON Web Tokens for user authentication and authorization

## Getting Started

### Prerequisites

- Python (version >= 3.8)
- Docker (version >= 20.10)
- Docker Compose (version >= 1.29)

### Installation

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

### API Documentation

The API documentation can be accessed through the Swagger UI interface. Open your browser and visit the following URL:

  ```bash
  http://localhost:8000/docs
  ```

The Swagger UI provides an interactive interface to explore and test the available API endpoints.

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Please see the [Contributing Guidelines](CONTRIBUTING.md) for more details.
