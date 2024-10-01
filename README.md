# wingz-rider

### Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/delletran/wingz-rider.git
    cd wingz-rider
    ```

2.  **Create and activate a virtual environment**:

    ```bash
    python -m venv venv
    ```

    ### On Windows
    ```bash
    venv\Scripts\activate
    ```

    ### On macOS/Linux
    ```bash
    source venv/bin/activate
    ```


3. **Install the required packages**:

    `pip install -r requirements.txt`

4. **Configure the database**:

    Update settings.py with your database configurations.

5. **Run migrations:**:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Create a superuser**:

    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server**:

    ```bash
    python manage.py runserver

    ```

8. **Access the application**:
    
    Open your web browser and go to http://127.0.0.1:8000/