# Rest-API
A Rest API with Dynamic Parameter Handling and Basic CRUD Operations. Implemented in Python and SQL-lite.


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



Quick setup Overview:
How to setup:
1. pip install -r requirements.txt
2. flask run
3. Test your endpoints



* /api
* /api/<user_id>
* /api/form

Endpoints:

- A POST requests to http://192.168.0.6:5000/api or http://127.0.0.1:5000/api add information to the endpoint. The endpoint /api receives data from  http://192.168.0.6:5000/api/form
- A GET requests to http://192.168.0.6:5000/api/<user_id> Return a json object containing the details of thr user.
- A DELETE request to http://192.168.0.6:5000/api/<user_id> Returns a msg "Delete Successful"
- A PATCH or PUT request to http://192.168.0.6:5000/api/<user_id> Returns a json object containing the details of the user when modified and Updated.


