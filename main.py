from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('index.html', title='home')

@app.route('/about/')
def about():
    return render_template('about.html', title='about')

@app.route('/handy/')
def handy():
    return render_template('handy.html', title='handy')

if __name__ == '__main__':
    app.run()