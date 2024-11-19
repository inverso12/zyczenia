from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

def validate_password(password):
    """Sprawdź, czy hasło odpowiada dacie 15.11.2024 w różnych formatach."""
    valid_passwords = [
        '15.11.2024',
        '15/11/2024',
        '15-11-2024',
        '15112024',
        '15 listopada 2024',
        '15 November 2024'
    ]
    return password in valid_passwords

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        password = request.form.get('hasło')
        if validate_password(password):
            return redirect(url_for('show_code'))
        else:
            return render_template('index.html', error="Błędne hasło. Podpowiedź: dzień, którego rocznicę co roku będziecie wspólnie świętować")
    return render_template('index.html')

@app.route('/show_code')
def show_code():
    # Odczytaj zawartość wszystkich plików do wyświetlenia
    files_content = {}
    files = ['main.py', 'templates/index.html', 'templates/show_code.html', 'static/style.css']
    for file in files:
        with open(file, 'r') as f:
            files_content[file] = f.read()
    return render_template('show_code.html', files_content=files_content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get("PORT", 5000))
