from flask import Flask
from flask import render_template

app = Flask(__name__)

print('app running')

@app.route('/')
def index():
    return render_template('index.html')
	
@app.route('/yo')
def yo():
    return 'yo'