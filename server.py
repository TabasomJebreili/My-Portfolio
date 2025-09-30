from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/starter')
def starter():
    return render_template("starter-page.html")


@app.route('/portfolio')
def portfolio():
    return render_template("portfolio-details.html")


if __name__ == "__main__":
    app.run(debug=True)