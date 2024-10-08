## Formatted Structure

- ..
- │   ├── .git
- │   ├── .gitignore
- │   ├── LICENSE
- │   ├── README.md
- │   ├── base
- │   │   ├── constants
- │   │   │   ├── api_info.json
- │   │   ├── custom
- │   │   │   ├── pagination.py
- │   │   ├── docs
- │   │   │   ├── ERD.drawio
- │   │   ├── migrations
- │   │   ├── models.py
- │   │   ├── tests.py
- │   │   ├── utils
- │   │   │   ├── read_write_file.py
- │   │   ├── views.py
- │   ├── core
- │   │   ├── asgi.py
- │   │   ├── permissions.py
- │   │   ├── settings.py
- │   │   ├── urls.py
- │   │   ├── wsgi.py
- │   ├── manage.py
- │   ├── requirements.txt
- │   ├── ride
- │   │   ├── filterset.py
- │   │   ├── migrations
- │   │   ├── models.py
- │   │   ├── serializers
- │   │   │   ├── ride.py
- │   │   │   ├── ride_event.py
- │   │   ├── tests.py
- │   │   ├── urls
- │   │   │   ├── ride.py
- │   │   │   ├── ride_event.py
- │   │   ├── views
- │   │   │   ├── ride.py
- │   │   │   ├── ride_event.py
- │   ├── user
- │   │   ├── helpers
- │   │   ├── managers.py
- │   │   ├── migrations
- │   │   ├── mixins.py
- │   │   ├── models.py
- │   │   ├── serializers
- │   │   │   ├── token.py
- │   │   │   ├── user.py
- │   │   ├── tests.py
- │   │   ├── urls.py
- │   │   ├── views.py