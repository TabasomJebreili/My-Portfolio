from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)


@app.route('/')
def welcome():
    return render_template('base.html')


if __name__ == "__main__":
    app.run(debug=True)