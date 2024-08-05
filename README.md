# School Project

## Setup

1. **Clone the repository**

    ```bash
    git clone <repository-url>
    cd <project-directory>
    ```

2. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run migrations**

    ```bash
    python manage.py migrate
    ```

4. **Run the server**

    ```bash
    python manage.py runserver
    ```

5. **Access the application**

    Open your web browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Docker Setup

1. **Build the Docker image**

    ```bash
    docker build -t school_project .
    ```

2. **Run the Docker container**

    ```bash
    docker run -p 8000:8000 school_project
    ```

3. **Access the application**

    Open your web browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
