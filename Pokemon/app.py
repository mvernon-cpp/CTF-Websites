from flask import Flask, request, render_template
from flask_mysqldb import MySQL
import yaml
app = Flask(__name__)

# COnfigure db
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
	return render_template('index.html')

#Successful user sign in page
@app.route('/login', methods=['GET', 'POST'])
def login():
	cur = mysql.connection.cursor()
	if request.method=='POST':
		creds=request.form
		name=creds['name']
		password=creds['password']
		cur.execute("select * from trainers where name='"+name+"' and password='"+password+"' ")
		r=cur.fetchall()
		count=cur.rowcount

		if count==1:
			return "SUCCESSFUL LOGIN.\n Here is the flag.\n FASTCTF{...}"
		else:
			return render_template('index.html')

	
	return render_template('index.html')


# @app.route('/users')
# def users():
# 	cur = mysql.connection.cursor()
# 	resultValue = cur.execute("SELECT * FROM trainers")
# 	if resultValue > 0:
# 		userDetails = cur.fetchall()
# 		return render_template('users.html', userDetails=userDetails)
# 	#  return render_template('index.html')


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0',port=8000)
