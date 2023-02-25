from flask import Flask, request, render_template
from flask_mysqldb import MySQL
import yaml
app = Flask(__name__)


# ================================================
'''    Pokemon Question   '''
# ================================================

# Configure db
db = yaml.safe_load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

# instantiate mysql
mysql = MySQL(app)


#Sign in page
@app.route('/')
def index():
    return render_template('signin.html')

# Successful user sign in page


@app.route('/login', methods=['GET', 'POST'])
def login():
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        creds = request.form
        name = creds['name']
        password = creds['password']
        cur.execute("select * from trainers where name='" +
                    name+"' and password='"+password+"' ")
        r = cur.fetchall()
        count = cur.rowcount

        if count == 1:
            return "SUCCESSFUL LOGIN.\n Here is the flag.\n FASTCTF{...}"
        else:
            return render_template('signin.html')

    return render_template('signin.html')


# ================================================
'''    Bruteforce Endpoints Question   '''
# ================================================


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/e1')
def e1():
    return render_template('empty.html')


@app.route('/e2')
def e2():
    return render_template('empty.html')


@app.route('/e3')
def e3():
    return render_template('empty.html')


@app.route('/e4')
def e4():
    return render_template('empty.html')


@app.route('/e5')
def e5():
    return render_template('empty.html')


@app.route('/found')
def found():
    return render_template('success.html')

# ====================================================


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
