# Dummy-api

This project is a Python 3.10 application designed for experimenting and testing hypotheses using the open REST API provided by [DummyJSON](https://dummyjson.com). The project structure is organized as follows:

```
project-name
├── main.py
├── poetry.lock
├── pyproject.toml
├── README.md
└── src
├── api_client.py
├── categories.py
├── DTOs.py
├── models.py
├── products.py
├── schemas.py
└── settings.py
```

## Description

This project leverages the open REST API from DummyJSON to explore and test various functionalities and behaviors. It includes modularized code for interacting with the API, defining data transfer objects (DTOs), data models, and schemas.

## Installation

To set up and run the project, follow these steps:

1. Make sure you have Python 3.10 installed on your system.
2. Install Poetry package manager using the instructions from [Poetry's official documentation](https://python-poetry.org/docs/).
3. Clone the project repository from GitHub.
4. Navigate to the project directory in your terminal or command prompt.
5. Run the following command to install project dependencies using Poetry:
    ```bash
    poetry install
    poetry shell
    ```

## Usage
After installing the project dependencies, you can run the main.py script to start experimenting with the DummyJSON API and testing your hypotheses.

```bash
python main.py
```

## Project Structure
- main.py: The main script to be executed for running the project.
- poetry.lock: File containing exact versions of dependencies managed by Poetry.
- pyproject.toml: Configuration file for Poetry, specifying project metadata and dependencies.
- README.md: This file providing an overview of the project and its usage.
- src/: Directory containing the source code of the project.
    - api_client.py: Module for interacting with the DummyJSON API using an ApiClient class.
    - categories.py: Module for handling product categories.
    - DTOs.py: Module containing data transfer objects for interacting with the API.
    - models.py: Module defining data models used in the project.
    - products.py: Module for managing product-related functionalities.
    - schemas.py: Module containing data validation schemas.
    - settings.py: Module for storing project settings and configurations.

Feel free to modify the source code and expand the project based on your experimentation needs.

## License
This project is licensed under the MIT License - see the LICENSE file for details.