# wingz-rider

## Installation

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

-----

## Usage


1. **Login and Get the Access Token**:

    Go to swagger: http://127.0.0.1:8000/swagger/
    
    Look for `token`, `/api/token/` 

    Click `Try it out`

    Add your user credentials and then Submit:
    ```json
    {
        "email": "your_email",
        "password": "your_password"
    }
    ```

2. **Authorization**:

    Look for the "Authorize" button in the top-right corner of the Swagger UI.

    Click the "Authorize" button, and a popup will appear asking for a token.

    In the popup, enter the token in the following format:
    `Bearer your_access_token_here`
    

3. **Booking Ride**:
    Go to `ride`, `/api/ride/create`

    sample data:
    ```json
    {
        "id_rider": 2,
        "id_driver": null,
        "status": "en-route",
        "pickup_latitude": 40.7128,
        "pickup_longitude": -74.0060,
        "dropoff_latitude": 40.730610,
        "dropoff_longitude": -73.935242
    }
    ```

    make sure `id_rider` users already exist.

    
4. **Pickup a Booking/Ride | Creating RideEvent**:
    Go to `ride_event`, `/api/ride_event/pickup`

    sample data:
    ```json
    {
        "id_ride": 1,
        "ride_data": {
            "id_driver": 3
        }
    }
    ```

    make sure `id_driver` users already exist.

4. **Dropoff a Booking/Ride | Update RideEvent**:
    Go to `ride_event`, `/api/ride_event/dropoff`

    `id_ride_event`: <picked_up-ride_event_id>,


## API documentation

    Go to redoc: http://127.0.0.1:8000/redoc/

