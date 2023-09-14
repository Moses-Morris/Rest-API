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
@app.route('/api', methods=['POST'])
def add_user():
        data = request.get_json()
        # Validate that the request contains JSON
        if not data:
            return jsonify({'message': 'No JSON data provided'}), 400

        if 'name' not in data:
            return jsonify({'message': 'Name is required'}), 400

        name = data.get('name')
        #password = data.get('password', None)

        if name == "" :   
            return jsonify({'message': 'Name cannot be empty'}), 400
        
        if type(name) != str:
            return jsonify({'message':'Cannot add user with non-string fields'}), 400
        
        #check if user exist in Database
        cursor.execute('SELECT * FROM apiusersinfo WHERE name = ?', (name,))
        user = cursor.fetchone()
        if user:
            return jsonify({'message': 'User already exists'}), 400

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
                #get_user = cursor.execute('SELECT * FROM apiusersinfo WHERE name = ?', (name,))
                #return jsonify(get_user), 201
                cursor.execute('SELECT * FROM apiusersinfo WHERE name = ?', (name,))
                user = cursor.fetchone()
                #return jsonify({'message': 'User added successfully'}), 201
                return jsonify({'Person': {'id': user[0], 'name': user[1]}}), 201
            else:
                return jsonify({'message': 'User already exists'}), 400
        except Exception as e:
            return ("Error:", e)
    
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
        return jsonify({'message': 'User not found!'}), 404
    

#create a route to |Update a user and their information
@app.route('/api/<user_id>', methods=['PUT'])
def update_user(user_id):
    #name= "Piece of Crap"
    data = request.get_json()
    name = data['name']


    if 'name' not in data:
        return jsonify({'message': 'Name is required'}), 400
    
    if isinstance(data['name'], str) == False:
        return jsonify({'message':'Cannot add user with non-string fields'}), 400

    #check if user exist
    CheckUser=cursor.execute('SELECT * FROM apiusersinfo  WHERE name = ? OR id =?', (user_id, user_id))

    if CheckUser:
        State=cursor.execute('UPDATE apiusersinfo SET name = ? WHERE name = ? OR id =?', (name, user_id, user_id))
        if State:
            connect.commit()  
            cursor.execute('SELECT * FROM apiusersinfo WHERE name = ?', (name,))
            user = cursor.fetchone()
            #return jsonify({'message': 'User added successfully'}), 201
            return jsonify({'Person': {'id': user[0], 'name': user[1]}}), 202
        else:
            return jsonify({'message': 'Update failed!'}), 400
    else:
        return jsonify({'message': 'User not found!'}), 404
    


#create a route to delete a user and their information
@app.route('/api/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    #create a cursor to execute SQL commands
    #cursor = connect.cursor()#
    State=cursor.execute('DELETE  FROM apiusersinfo WHERE name = ? OR id = ?', (user_id,user_id))
    if State:
        connect.commit()
        return jsonify('Delete success'), 204    #Dont Send a response to the user just return a status code
        #return jsonify('Delete success'), 200   //Send a response to the user
    else:
        return jsonify({'message': 'Delete failed!!'}), 400
    

#view all users
@app.route('/api/users', methods=['GET'])
def all_users():
    
    #select all users
    cursor.execute('SELECT * FROM apiusersinfo')
    #fetch all the users
    users = cursor.fetchall()
    #connect.close()
    return jsonify(users), 200


#Do not close the connection!!!
#connect.close()
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)