import os
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def splash():
    return render_template('privacy.html')


@app.route('/privacy')
def privacy():
    return render_template('privacy.html')


if __name__ == '__main__':
    app.run(port=os.getenv('PORT', 8000))