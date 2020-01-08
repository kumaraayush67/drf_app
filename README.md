# Simple DRF Application

This is a rest application created using django rest framework as a backend assignment.

### Installation

- Install all libraries mention in requirements.txt file in root repo using following command.
 
    ```
    pip install -r requirements.txt
    ```

- Application is created on Python version 3.6.9.

### General Application Setup

- To get a simple and easy access to database, it is advised to created a super user. Fill in super user details (username, email id and password ) after using following command.
  
    ```
    python manage.py createsuperuser
    ```

### Start Server and Login to admin pannel

- To start django server:

    ```
    python manage.py runserver
    ```
 
- Once the server is started, to can log on to user local super user admin pannel browse following url and use previously generated creadentials to sign in.
  
    ```
    http://localhost:8000/admin
    ```

### Database

The application uses sqlite database, having one table "User" with following attribute
- ID
- First Name
- Last Name
- Company Name
- Age
- City
- State
- Zip
- Email
- Web

### Rest API End Points

Use following end points with base url: http://localhost:8000

- /api/users - GET - To list the users 

- /api/users - POST - To create a new user

- /api/users/{id} - GET - To get the details of a user

- /api/users/{id} - PUT - To update the details of a user

- /api/users/{id} - DELETE - To delete the user

### Testing

All testcases are created in tests.py file in userapp directory. To run test cases :

- to test user listing api
```
python manage.py test userapp.tests.UserTestCase.list_request_test
```

- to test retreive user api
```
python manage.py test userapp.tests.UserTestCase.get_request_test
python manage.py test userapp.tests.UserTestCase.get_invalid_request_test
```

- to test create user api
```
python manage.py test userapp.tests.UserTestCase.post_request_test
python manage.py test userapp.tests.UserTestCase.post_invalid_request_test
```

- to test update user api
```
python manage.py test userapp.tests.UserTestCase.put_request_test
```

- to test delete user api
```
python manage.py test userapp.tests.UserTestCase.delete_request_test
```
