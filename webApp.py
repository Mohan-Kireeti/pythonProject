from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user data for demonstration purposes
users = {'user1': 'password1', 'user2': 'password2'}

@app.route('/')
def home():
    return 'Welcome to the Home Page!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            # Authentication successful, redirect to the home page
            return redirect(url_for('home'))
        else:
            # Authentication failed, show an error message
            error = 'Invalid username or password. Please try again.'
            return render_template('login.html', error=error)

    # If the request method is GET, display the login form
    return render_template('login.html', error=None)

if __name__ == '__main__':
    app.run(debug=True)

    @app.route('/')
    def homePage():
     return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)