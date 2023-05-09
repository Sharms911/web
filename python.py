Zfrom flask import Flask, render_template, redirect, request

app = Flask(__pedarenow__)

# Render the login page
@app.route('/')
def index():
    return render_template('login.html')

# Handle the login form submission
@app.route('/menu', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Check the credentials and redirect to the menu page
    if username == 'user' and password == 'pass':
        return redirect('/menu.html')
    else:
        error = 'Invalid username or password'
        return render_template('index.html', error=error)

# Render the menu page
@app.route('/menu.html')
def menu():
    return render_template('menu.html')

if __name__ == '__main__':
    app.run()
