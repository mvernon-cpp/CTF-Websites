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
            return "SUCCESSFUL LOGIN.<br> Here is the flag for Team Rocket Strikes Back.</br><br>FASTCTF{Totodile}</br>"
        else:
            return render_template('signin.html')

    return render_template('signin.html')


# ================================================
'''    Bruteforce Endpoints Question   '''
# ================================================


@app.route('/home')
def home():
    return render_template('home.html')


# @app.route('/!@#redrose!@#')
# @app.route('/6whiterose')
# @app.route('/***rockyou***')
# @app.route('/1hat3passw0rds')
# @app.route('/thunderbolt')


@app.route('/01')
@app.route('/02')
@app.route('/03')
@app.route('/04')
@app.route('/05')
def e5():
    return render_template('empty.html')


@app.route('/101010')  # rockyou.txt
@app.route('/~djh101010')
# directory-list-lowercase-2.3-medium.txt, directory-list-2.3-medium.txt
@app.route('/1101010702')  # apache-user-enum-2.0.txt
def found():
    return render_template('success.html')

# ====================================================


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
