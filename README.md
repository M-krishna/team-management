# Team Management

## Getting Started
Steps:
1. Clone/Pull/Download this repository
2. Create a ```virtualenv venv``` and install dependencies with ```pip install -r requirements.txt```
3. Configure your ```.env``` variables
4. Migrate the DB Schema using
    ```
    * python manage.py makemigrations
    * python manage.py migrate
   ```
5. Start the server using ```python manage.py runserver```

This Project includes:
   * REST API for managing team members.

For testing use this ```cURL commands```
   * GET Method: 
   ```
   curl -H "Content-Type:application/json" http://localhost:8000/v1/api/user
```
   * POST Method:  
   ```
    curl --location --request POST 'http://localhost:8000/v1/api/user' --header 'Content-Type: application/json' \
    --data-raw '{
        "first_name": "John",
        "last_name": "doe",
        "email": "john.doe@gmail.com",
        "phone_number": "8345109284",
        "role": "admin"
    }'
   ```
  * PATCH Method:
  ```
    curl --location --request PATCH 'http://localhost:8000/v1/api/user/1' --header 'Content-Type: application/json' \
    --data-raw '{
        "first_name": "New",
        "last_name": "",
        "email": "new.user@gmail.com",
        "phone_number": "8345109284",
        "role": "admin"
    }'
  ```
  * DELETE Method:
  ```
    curl --location --request DELETE 'http://localhost:8000/v1/api/user/12' --header 'Content-Type: application/json' \
    --data-raw '{
        "first_name": "New",
        "last_name": "",
        "email": "new.user@gmail.com",
        "phone_number": "8345109284",
        "role": "admin"
    }'
  ```
  