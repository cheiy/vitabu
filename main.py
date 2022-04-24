from flask import Flask, redirect, url_for, render_template, request, json
from flaskext.mysql import MySQL
from flask import session


app = Flask(__name__)

app.secret_key = 'eb52f64c381878a2666ec778eae9ae34f2eb0accf563f79c6f7e176063581f584b103448fb96dcccefb5e62f96212ac0aadd15394e66285ffd71580d182f228d'

mysql = MySQL()

#Mysql configurations
app.config['MYSQL_DATABASE_USER'] = 'vitabu_admin'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Admin_2021#'
app.config['MYSQL_DATABASE_DB'] = 'vitabu'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)





@app.route("/")
def main():
    return render_template("index.html")

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/signUp', methods=['POST'])
def signUp():

    # Read the posted values from the UI
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
    _gender = request.form['gender']
    _phonenumber = request.form['phoneNumber']

    # Validate the received values
    if _name and _email and _password:
        
        conn = mysql.connect()

        cursor = conn.cursor()

        cursor.callproc('sp_createUser',(_email,_name,_phonenumber,_gender,_password))

        data = cursor.fetchall()
        if len(data) is 0:
            conn.commit()
            return json.dumps({'message':'User created successfully !'})
        else:
            return json.dumps({'error':str(data[0])})
        conn.close()
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})


@app.route('/showSignin')
def showSignin():
    return render_template('signin.html')


@app.route('/validateLogin', methods=['POST'])
def validateLogin():
    try:
        _username = request.form['inputEmail']
        _password = request.form['inputPassword']

    #Connect to MySQL
        con = mysql.connect()
        cursor = con.cursor()
        cursor.callproc('sp_validateLogin',(_username,))
        data = cursor.fetchall()

        #session = {}
        if len(data) > 0:
            #Check if user logging in is an admin and if so redirect them to the admin dashboard
            if data[0][8] == 1 and data[0][2] == _password:
                session['user'] = data[0][0]
                session['isadmin'] = data[0][8]
                return redirect('/admindashboard')
            #If user logging in successfully is not an admin, redirect them to the users page
            elif data[0][2] == _password:
                session['user'] = data[0][0]
                return redirect('/userHome')
            else:
                return render_template('error.html',error = 'Wrong Email Address or Password.')
        else:
            return render_template('error.html',error = 'Wrong Email Address or Password.')

    except Exception as e:
        return render_template('error.html',error = str(e))
    finally:
        con.close()

@app.route('/userHome')
def userHome():
    if session.get('user'):
        return render_template('userHome.html')
    else:
        return render_template('error.html',error = 'Unauthorized Access')

@app.route('/logout')
def logout():
    session.pop('user',None)
    session.pop('isadmin',None)
    return redirect('/')

#ADD Books Page
@app.route('/showAddBook')
def showAddBook():
    if session.get('user'):
        return render_template('addBook.html')

#ADD Books Method
@app.route('/addBook', methods=['POST'])
def addBook():
    try:
        if session.get('user'):
            _user_id = session.get('user')
            _book_title = request.form['inputTitle']
            _grade_name = request.form['inputGrade']
            _publisher_name = request.form['inputPublisher']
            _options = request.form['sellExchangeBoth']
            _price = request.form['txtPrice']
            _condition = request.form['bookCondition']
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_addListing',(_user_id,_book_title,_publisher_name,_options,_price,_grade_name,_condition))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return redirect('/userHome')
            else:
                return render_template('error_html',error='An error occurred HERE')

        else:
            return render_template('error.html',error='Unauthorized Access')
    except Exception as e:
        return render_template('error.html',error = str(e))
    finally:
        #return render_template('error.html',error='An error occurred THERE')
        cursor.close()
        conn.close()
        

#Admin Page
@app.route('/admindashboard')
def admin_dashboard():
   if session.get('user') and session.get('isadmin'):
       return render_template('admin_dashboard.html', title="Dashboard")
   elif session.get('user'):
       return render_template('userHome.html')
   else:
       return render_template('index.html')


#ADD Publishers Page
@app.route('/showAddPublisher')
def showAddPub():
    if session.get('user') and session.get('isadmin'):
       return render_template('addPublisher.html')
    elif session.get('user'):
       return render_template('userHome.html')
    else:
       return render_template('index.html')

#Add Publishers Method
@app.route('/addPublisher', methods=['POST'])
def addPublisher():
    try:
        if session.get('user') and session.get('isadmin'):
            _user_id = session.get('user')
            _shortname = request.form['pubShortName']
            _longname = request.form['pubLongName']
            _ISBN = request.form['pubISBN']
            
        
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_addPublisher',(_shortname,_longname,_ISBN,_user_id))
            data = cursor.fetchall()
     
            if len(data) is 0:
                conn.commit()
                return redirect('/admindashboard')
            else:
                return render_template('error_html',error='An error occurred 1')

        else:
            return render_template('error.html',error='Unauthorized Access')
    except Exception as e:
        return render_template('error.html',error = str(e))
    finally:
        #return render_template('error.html',error='An error occurred 2')
        cursor.close()
        conn.close()
#List books
#@app.route('/showListedBooks')
#def listedBooks():

if __name__ == "__main__":
	app.run(host='0.0.0.0')
