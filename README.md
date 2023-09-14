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
Links: https://rest-api-aeyz.onrender.com/api


- A POST requests to https://rest-api-aeyz.onrender.com/api or https://rest-api-aeyz.onrender.com/api add information to the endpoint. The endpoint /api receives data from  https://rest-api-aeyz.onrender.com/api as a POST request. The format is in raw format
- A GET requests to https://rest-api-aeyz.onrender.com/api/<user_id> Return a json object containing the details of thr user.
- A DELETE request to https://rest-api-aeyz.onrender.com/api/<user_id> Returns a msg "Delete Successful"
- A PATCH or PUT request to https://rest-api-aeyz.onrender.com/api/<user_id> Returns a json object containing the details of the user when modified and Updated.



* UML and ER Diagrams.
- https://lucid.app/lucidchart/b91e23a5-402d-42b2-a14f-a02f3bb02588/edit?viewport_loc=-303%2C-2475%2C3840%2C1827%2C0_0&invitationId=inv_cf08654d-cd65-4852-9b16-df2646f34d0b

* UML and ER Diagrams.
- https://lucid.app/lucidchart/b91e23a5-402d-42b2-a14f-a02f3bb02588/edit?viewport_loc=-303%2C-2475%2C3840%2C1827%2C0_0&invitationId=inv_cf08654d-cd65-4852-9b16-df2646f34d0b


Testing:
Done with postman software tool.
https://www.postman.com/ 
