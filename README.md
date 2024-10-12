### Table of Contents
- [Installations](#installations)
- [Assignment](/assignment.md)

## Installations

1. **Create a Virtual Environment**

    Use one of the following commands to create a virtual environment:

    ```sh
    python -m venv env
    ```

    **OR**

    ```sh
    python3 -m venv env
    ```

2. **Activate the Virtual Environment**

    - On **Linux/MacOS**:
    ```sh
    source env/bin/activate
    ```

    - On **Windows**:
    ```sh
    env\Scripts\activate
    ```

3. **Install the Requirements**

    Install the required dependencies using the `requirements.txt` file:

    ```sh
    pip install -r requirements.txt
    ```

4. **Set Up MongoDB**

    - Create a MongoDB database either using [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) or a local MongoDB instance.
    - Get the MongoDB connection URL.

5. **Create a `.env` File**

    Create a `.env` file in the root directory and add the following variables:

    ```env
    MONGODB_URL='<connection-url>'
    PORT='8000'
    ```

    Replace `<connection-url>` with your actual MongoDB connection URL.

6. **Start the Application**

    Start the FastAPI application using:

    ```sh
    python app/main.py
    ```

    This will start the application on the default port `8000` (or the one specified in `.env`).

7. **API Documentation**

    The API documentation (Swagger UI) will be available at the following URL:

    [API Docs](https://vodex-assignment.onrender.com/docs)



