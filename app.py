from flask import Flask, render_template, request, jsonify
from database import connect
import sqlite3
app = Flask(__name__)
cursor = connect.cursor()
#Create a route to display Hello World
@app.route('/')
def hello_world():
    return 'Hello, World!'

#Create a form to add new users
@app.route('/api/form', methods=['GET', 'POST'])
def form():
    return render_template('form.html')


def validate_data(data):
    # Validate that fields are only strings
    if not all(isinstance(data[field], str) for field in ['name', 'address', 'email']):
        return False
    # Additional validation can be added here
    return True

#create a route to add new users
@app.route('/api', methods=['GET','POST'])
def add_user():
    if request.method == 'GET':
        return " "# jsonify({'message': 'This is a GET request'})

    elif request.method == 'POST':
        data = request.get_json()
        # Validate that the request contains JSON
        if 'name' not in data:
            return jsonify({'message': 'Name is required'}), 400

        name = data.get('name')
        #password = data.get('password', None)

        if name == "" :   
            return 'Cannot add user with empty fields'

        #cursor = connect.cursor()
        #insert a new user
        try:
            execute = cursor.execute('INSERT INTO apiusersinfo (name) VALUES (?)', (name,))
            # Commit the transaction if needed
            # connection.commit()
            if execute:
                connect.commit()
                #close the connection
                #connect.close()
                return 'Success : User added successfully'
            else:
                return 'User add failed'
        except Exception as e:
            return ("Error:", e)
    else:
        return 'Invalid request method'
    
#create a route to view a user and their information
@app.route('/api/<user_id>', methods=['GET'])
def get_user(user_id):
    #create a cursor to execute SQL commands
    #cursor = connect.cursor()
    #select all users
    cursor.execute('SELECT * FROM apiusersinfo WHERE name = ?   OR  id = ? ', (user_id, user_id))
    #fetch all the users
    user = cursor.fetchall()
    if user:
        return jsonify(user)
    else:
        return 'User not found'
    

#create a route to |Update a user and their information
@app.route('/api/<user_id>', methods=['PATCH','PUT'])
def update_user(user_id):
    name= "Piece of Crap"
    State=cursor.execute('UPDATE apiusersinfo SET name = ? WHERE name = ? OR id =?', (name, user_id, user_id))
    if State:
        connect.commit()  
        return 'Update success'
    else:
        return 'Update failed'
    


#create a route to delete a user and their information
@app.route('/api/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    #create a cursor to execute SQL commands
    #cursor = connect.cursor()#
    State=cursor.execute('DELETE  FROM apiusersinfo WHERE name = ? OR id = ?', (user_id,user_id))
    if State:
        connect.commit()
        return 'Delete success'
    else:
        return 'Delete failed'
    

#view all users
@app.route('/api/users', methods=['GET'])
def all_users():
    
    #select all users
    cursor.execute('SELECT * FROM apiusersinfo')
    #fetch all the users
    users = cursor.fetchall()
    #connect.close()
    return jsonify(users)


#Do not close the connection!!!
#connect.close()
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)