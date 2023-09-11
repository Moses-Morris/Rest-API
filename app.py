from flask import Flask, render_template, request
from database import connect
app = Flask(__name__)

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

        cursor = connect.cursor()
        #insert a new user
        cursor.execute('INSERT INTO users VALUES (?)', (name,))
        #commit the changes
        connect.commit()
        #close the connection
        connect.close()
        return 'success'
    

#create a route to view all users
@app.route('/api/<user_id>', methods=['GET'])
def get_user(user_id):
    #create a cursor to execute SQL commands
    cursor = connect.cursor()
    #select all users
    cursor.execute('SELECT * FROM users WHERE name = ?', (user_id,))
    #fetch all the users
    users = cursor.fetchall()
    #close the connection
    connect.close()
    return users



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)