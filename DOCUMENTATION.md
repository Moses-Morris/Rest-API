API Documentation
This document provides detailed information on how to use the User API, which allows you to perform CRUD operations on a "user" resource.

Table of Contents
Endpoints
- Create a New Person
- Retrieve Person Details
- Update Person Details
- Delete a Person


NB: The ID of the user is Automatically generated and incremented by the database.

1. Create a New user
- Endpoint: POST /api


+ Response 
json
{
    1,
    "Mark Essien",
    "branch@gmail.com123",
    "qwertyuiop"
}


2. Retrieve User Details
- Endpoint: GET /api/<user_id>

Response:
json
{
    6,
    "Mark Essien",
    "branch@gmail.com123",
    "qwertyuiop"
}


3.  Update User Details
- Endpoint: PUT /api/<user_id>

+ Request:
json
{
    6,
    "Update value Field",
    "branch@gmail.com123",
    "qwertyuiop"
}


4. Delete a User
- Endpoint: DELETE /api/<user_id>

+ Response:
json

{
  "message": "Person with ID <user_id> has been deleted successfully."
}

<br>

5. Create a New User

- Request:
    http
+ POST /api
    Content-Type: application/json

{
    //Id Generation is automatic
    "Mark Essien",
    "branch@gmail.com123",
    "qwertyuiop"
}



6. Retrieve user Details

- Request:
- GET /api/2

+ Response:
json
{
    6,
    "Mark Essien",
    "branch@gmail.com123",
    "qwertyuiop"
}





Known Limitations
The API currently does not support pagination for large datasets.

Setup Instructions

1. Clone the repository from GitHub: git clone https://github.com/Moses-Morris/Rest-API.git
2. Navigate to the project directory: cd Rest-API
3. Create a virtual environment: python -m venv venv
4. Activate the virtual environment:
5. On macOS and Linux: source venv/bin/activate
6. On Windows: venv\Scripts\activate
7. Install the required packages: pip install -r requirements.txt
8. Start the Flask application: python app.py or flask run
9. Deployment  - You can deploy the Flask application to a server of your choice.