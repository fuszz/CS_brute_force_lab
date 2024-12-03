from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import secrets
import string

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Klucz do sesji

# Przykładowe dane użytkowników (w prawdziwej aplikacji użyjesz bazy danych)
users_db = {
    "Administrator": {
        "password": generate_password_hash("265"), 
        "nickname": "Administrator"
    }
}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Sprawdzenie, czy użytkownik istnieje i czy hasło jest poprawne
    if username in users_db and check_password_hash(users_db[username]['password'], password):
        session['username'] = username
        return redirect(url_for('dashboard'))
    
    # W przypadku błędnych danych logowania
    flash("Invalid credentials, please try again.")
    return redirect(url_for('home'))

@app.route('/dashboard')
def dashboard():
    # Jeśli użytkownik nie jest zalogowany, przekierowujemy go do strony logowania
    if 'username' not in session:
        return redirect(url_for('home'))

    # Pobieranie danych użytkownika (nickname)
    username = session['username']
    nickname = users_db[username]['nickname']
    return render_template('dashboard.html', nickname=nickname)

@app.route('/logout')
def logout():
    # Usuwanie użytkownika z sesji
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
