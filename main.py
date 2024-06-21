from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def landing_page():
    return render_template('landingpage.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/current+projects')
def currentprojects():
    return render_template('current_projects.html')

if __name__ == '__main__':
    app.run()
