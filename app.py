from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    profit = None
    if request.method == 'POST':
        try:
            base1 = float(request.form['pair1_base'])
            quote1 = float(request.form['pair1_quote'])
            quote1_2 = float(request.form['pair2_base'])
            quote2 = float(request.form['pair2_quote'])
            quote2_2 = float(request.form['pair3_base'])
            base1_return = float(request.form['pair3_quote'])
            fee = float(request.form['fee']) / 100

            amount = 1
            amount *= (quote1 / base1) * (1 - fee)
            amount *= (quote2 / quote1_2) * (1 - fee)
            amount *= (base1_return / quote2_2) * (1 - fee)
            profit = round((amount - 1) * 100, 4)

        except Exception as e:
            profit = f'Invalid input: {e}'

    return render_template('index.html', profit=profit)

if __name__ == '__main__':
    app.run(debug=True)