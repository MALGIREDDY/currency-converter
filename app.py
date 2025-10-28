from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    from_currency = request.form['from']
    to_currency = request.form['to']
    amount = float(request.form['amount'])

    # External API for conversion
    url = f'https://api.exchangerate-api.com/v4/latest/{from_currency}'
    response = requests.get(url)
    data = response.json()

    if 'rates' not in data or to_currency not in data['rates']:
        return render_template('index.html', result="Invalid currency code entered.")

    rate = data['rates'][to_currency]
    converted_amount = amount * rate

    return render_template(
        'index.html',
        result=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}"
    )

if __name__ == '__main__':
    app.run(debug=True)

