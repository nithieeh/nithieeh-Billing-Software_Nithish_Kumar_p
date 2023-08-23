from flask import Flask, render_template


app = Flask(__name__)
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_HOST']="localhost"



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/purchase')
def purchase():
    return render_template('purchase.html')

@app.route('/sales')
def sales():
    return render_template('sales.html')

if __name__ == '__main__':
    app.run(debug=True)
