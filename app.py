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


#create a route to add new users
@app.route('/api', methods=['GET', 'POST'])
def add_user():
    #create a cursor to execute SQL commands
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        if name == "" or email == "" or password == "":
            return 'Cannot add user with empty fields'
        if len(password) < 8:
            return 'Password must be at least 8 characters'
        if type(name) != str or type(email) != str:
            return 'Invalid data type Values must be strings'

        #cursor = connect.cursor()
        #insert a new user
        try:
            execute = cursor.execute('INSERT INTO apiusersinfo (name, email, password) VALUES (?, ?, ?)', (name, email, password))
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
    elif request.method == 'GET':
        #create a cursor to execute SQL commands
        #cursor = connect.cursor()
        #select all users
        cursor.execute('SELECT * FROM apiusersinfo')
        #fetch all the users
        users = cursor.fetchall()
        if users:
            return jsonify(users)
        else:
            return 'No users found'
    else:
        return 'Invalid request method'

#create a route to view a user and their information
@app.route('/api/<user_id>', methods=['GET'])
def get_user(user_id):
    #create a cursor to execute SQL commands
    #cursor = connect.cursor()
    #select all users
    cursor.execute('SELECT * FROM apiusersinfo WHERE name = ?   OR  id = ? OR email = ?', (user_id, user_id, user_id))
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
    




#Do not close the connection!!!
#connect.close()
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)