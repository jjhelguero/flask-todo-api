# Flask Todo API

This repository contains a simple Flask API for managing todo tasks. The API is designed to be simple and easy to use.

## Design Approach

The API is designed using the Flask framework, a lightweight and flexible web application framework. The API follows the RESTful design principles, with each resource being represented as a URL and the HTTP methods being used to perform operations on the resources.

The API uses a simple in-memory data store for storing the tasks. This makes the API easy to set up and use for testing and development.

## Tests

The API is thoroughly tested using the pytest framework. The tests cover all the API endpoints and ensure that the API behaves as expected.

The tests are located in the `tests` directory. To run the tests, simply run `pytest` in the root directory of the repository.

## Getting Started

Install poetry
```
pipx install poetry
```

To run tests
```
poetry run pytest
```

To run Flask API
```
flask run
```