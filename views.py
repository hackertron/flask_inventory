from app import app
from app import mysql
from functools import wraps
from forms import RegisterForm, SkillForm, RecommendForm, user_info
from flask import  render_template, request, flash, redirect, url_for, session, logging
from flask import escape
from passlib.hash import sha256_crypt
import sys
#home
@app.route('/')
def index():
		return render_template('home.html')

# About
@app.route('/about')
def about():
	return render_template('about.html')

# Users
@app.route('/users')
def users():
    #create cursor
    cur = mysql.connection.cursor()

    # Get users
    result = cur.execute("SELECT * FROM users")

    users = cur.fetchall()
    if result > 0:
        return render_template('users.html', users=users)
    else:
        msg = 'No users Found'
        return render_template('users.html', msg=msg)

    # Close connection
    cur.close()



# to do : get user profile page by both id and username ;)
# single users
@app.route('/profile/<int:id>/')
@app.route('/profile/<string:username>/')
def profile(id=None, username=None):
    # Create cursor
    cur = mysql.connection.cursor()

    #Get user
    if username != None:
        result = cur.execute("SELECT * FROM users WHERE username = %s", [username])

    elif id != None:
        result = cur.execute("SELECT * FROM users WHERE id = %s", [id])

    else :
        return render_template('404.html')

    users = cur.fetchone()
    print(users['id'],file=sys.stderr)
    result = cur.execute("SELECT * FROM skills WHERE has_skill =%s", [users['id']])
    skills = cur.fetchall()

    result = cur.execute("SELECT * FROM recommendation WHERE profile = %s", [users['id']])
    recommendation = cur.fetchall()

    return render_template('user.html', users=users, skills=skills, recommendation=recommendation)



# User Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        # Create cursor
        cur = mysql.connection.cursor()

        # Execute query
        cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)", (name, email, username, password))

        # Commit to DB
        mysql.connection.commit()
        # fetch id of the newly addeded user
        result = cur.execute("SELECT id FROM users WHERE email = %s", [email])
        if result > 0:
            id = cur.fetchone()
            print(id['id'],file=sys.stderr)

        # Close connection
        cur.close()

        flash('Add additional info to complete your registration', 'danger')

        return redirect(url_for('add_info', id=id['id']))
    return render_template('register.html', form=form)


# User info
# need to fix request origin
@app.route('/add_info',methods=['GET', 'POST'])
def add_info():
	form = user_info(request.form)
	id =  request.args
	print(id['id'],file=sys.stderr)
	if request.method == 'POST' and form.validate():
		org_name = escape(form.org_name.data)
		contact_person = escape(form.contact_person.data)
		contact_email = escape(form.contact_email.data)
		contact_no = escape(form.contact_no.data)
		address = escape(form.address.data)
		state = escape(form.state.data)
		pin_code = escape(form.pin_code.data)
		city = escape(form.city.data)
		country = escape(form.country.data)
		GSTIN_number = escape(form.GSTIN_number.data)
		serial_key_2 = escape(form.serial_key_2.data)
		package = escape(form.package.data)
		tally = "tally" in request.form
		busy = "busy" in request.form
		openoffice = "openoffice" in request.form
		username1 = escape(form.username1.data)
		username2 = escape(form.username2.data)
		username3 = escape(form.username3.data)
		user_id = form.user_id.data

		# Create cursor
		cur = mysql.connection.cursor()

		# Execute query
		cur.execute(""" INSERT INTO user_info(user_id, org_name, contact_person, contact_email,
		contact_no, address, state, pin_code, city, country, GSTIN_number, serial_key_2,
		package, tally, busy, openoffice, username1, username2, username3) VALUES(%s, %s, %s, %s,
		%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",(user_id, org_name, contact_person,
		contact_email, contact_no, address, state, pin_code, city, country, GSTIN_number, serial_key_2,
		package, tally, busy, openoffice, username1, username2, username3))

		# Commit to DB
		mysql.connection.commit()

		# add to package table
		cur.execute("UPDATE packages SET users_count = users_count + 1 WHERE name = %s", [package])

		# commit to DB
		mysql.connection.commit()

		# close connection
		cur.close()

		flash('You are now registered and can log in', 'success')
		return redirect(url_for('login'))
	return render_template('add_info.html',form=form, id=id)


# User login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get Form Fields
        username = request.form['username']
        password_candidate = request.form['password']

        # Create cursor
        cur = mysql.connection.cursor()

        # Get user by username
        result = cur.execute("SELECT * FROM users WHERE username = %s", [username])

        if result > 0:
            # Get stored hash
            data = cur.fetchone()
            password = data['password']

            # Compare Passwords
            if sha256_crypt.verify(password_candidate, password):
                # Passed
                session['logged_in'] = True
                session['username'] = username

                flash('You are now logged in', 'success')
                return redirect(url_for('dashboard'))
            else:
                error = 'Invalid login'
                return render_template('login.html', error=error)
            # Close connection
            cur.close()
        else:
            error = 'Username not found'
            return render_template('login.html', error=error)

    return render_template('login.html')

# Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))
    return wrap


# Logout
@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))



# Dashboard
@app.route('/dashboard')
@is_logged_in
def dashboard():
    # dashboard

	#create Cursor
	cur = mysql.connection.cursor()

	# get user type (admin)
	cur.execute("SELECT type FROM users WHERE username = %s", [session['username']])
	type = cur.fetchone()
	return render_template('dashboard.html', type=type)



# Add Skill
@app.route('/add_skill', methods=['GET', 'POST'])
@is_logged_in
def add_skill():
    form = SkillForm(request.form)
    if request.method == 'POST' and form.validate():
        skill_name = form.skill_name.data

        skills = skill_name.split(',')
        #print(skills,file=sys.stderr)
        # Create Cursor
        cur = mysql.connection.cursor()

        # Get user id
        result = cur.execute("SELECT id FROM users WHERE username = %s" , [session['username']])
        user_id = cur.fetchone()
        print(user_id['id'],file=sys.stderr)

        # Execute
        size = len(skills)
        for i in range(0,size):
            cur.execute("INSERT INTO skills (skill_name, has_skill) VALUES(%r, %s)",[skills[i], user_id['id']])

        # Commit to DB
        mysql.connection.commit()

        #Close connection
        cur.close()

        flash('Skill Added', 'success')

        return redirect(url_for('dashboard'))

    return render_template('add_skill.html', form=form)


# Delete skill
@app.route('/delete_skill/<string:id>', methods=['POST'])
@is_logged_in
def delete_skill(id):
    # Create cursor
    cur = mysql.connection.cursor()

    # get user id
    result = cur.execute("SELECT id FROM users WHERE username = %s" , [session['username']])
    user_id = cur.fetchone()
    print(user_id['id'],file=sys.stderr)

    # Execute
    cur.execute("DELETE FROM skills WHERE has_skill = %s AND id = %s", [user_id['id'], id])

    # Commit to DB
    mysql.connection.commit()

    #Close connection
    cur.close()

    flash('Skill Deleted', 'success')

    return redirect(url_for('dashboard'))

# add endorsement
@app.route('/endorsement/<string:id>', methods=['POST'])
@is_logged_in
def endorsement(id):
    #Create cursor
    cur = mysql.connection.cursor()

    #get users id
    result = cur.execute("SELECT id FROM users WHERE username = %s", [session['username']])
    endorsed_by_id = cur.fetchone()
    result = cur.execute("SELECT * FROM skills WHERE id =%s",[id])
    endorsed_to_id = cur.fetchone()

    print("endorsed by %s",endorsed_by_id['id'],file=sys.stderr)
    print("endorsed to %s",endorsed_to_id['has_skill'],file=sys.stderr)

    # insert in endorsement table
    cur.execute("INSERT INTO endorsement (endorsed_by, endorsed_to, skill) VALUES(%s, %s, %s)",[endorsed_by_id['id'], endorsed_to_id['has_skill'], endorsed_to_id['id']])

    #Commit to DB
    mysql.connection.commit()

    #Close Connection
    cur.close()

    flash('Endorsement added', 'success')

    #Redirect
    redirect_to = "/profile/{}".format(endorsed_to_id['has_skill'])
    print(redirect_to,file=sys.stderr)
    return redirect(redirect_to)



# Add Serial Keys
@app.route('/serial_key', methods=['GET','POST'])
@is_logged_in
def serial_key():
	if request.method == 'POST':
		key1 = escape(request.form['key1'])
		key2 = escape(request.form['key2'])
		package = escape(request.form['package'])
		print(key1,file=sys.stderr)
		print(key2,file=sys.stderr)
		print(package,file=sys.stderr)

		# create cursor
		cur = mysql.connection.cursor()

		# execute query
		cur.execute("INSERT INTO serial_keys (key1, key2, package) VALUES(%s, %s, %s)",(key1, key2, package))

		# commit to DB
		mysql.connection.commit()

		# close Connection
		cur.close()

		flash('Keys added successfully', 'success')
		return redirect('/dashboard')
	else:
		return render_template('serial_key.html')


# add distributors
@app.route('/distributors', methods=['GET', 'POST'])
@is_logged_in
def distributors():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))
        type = 'Distributor'

        # Create cursor
        cur = mysql.connection.cursor()

        # Execute query
        cur.execute("INSERT INTO users(name, email, username, password, type) VALUES(%s, %s, %s, %s, %s)", (name, email, username, password, type))

        # Commit to DB
        mysql.connection.commit()
        # fetch id of the newly addeded user
        result = cur.execute("SELECT id FROM users WHERE email = %s", [email])
        if result > 0:
            id = cur.fetchone()
            print(id['id'],file=sys.stderr)

        # Close connection
        cur.close()

        flash('Add additional info to complete your registration', 'danger')

        return redirect(url_for('add_info', id=id['id']))
    return render_template('dist.html', form=form)



# add Dealer
@app.route('/dealer', methods=['GET', 'POST'])
@is_logged_in
def dealer():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))
        type = 'Dealer'

        # Create cursor
        cur = mysql.connection.cursor()

        # Execute query
        cur.execute("INSERT INTO users(name, email, username, password, type) VALUES(%s, %s, %s, %s, %s)", (name, email, username, password, type))

        # Commit to DB
        mysql.connection.commit()
        # fetch id of the newly addeded user
        result = cur.execute("SELECT id FROM users WHERE email = %s", [email])
        if result > 0:
            id = cur.fetchone()
            print(id['id'],file=sys.stderr)

        # Close connection
        cur.close()

        flash('Add additional info to complete your registration', 'danger')

        return redirect(url_for('add_info', id=id['id']))
    return render_template('deal.html', form=form)




# Add Recommendation
@app.route('/add_recommendation/<string:id>', methods=['GET', 'POST'])
@is_logged_in
def add_recommendation(id):
    form = RecommendForm(request.form)
    if request.method == 'POST' and form.validate():
        title = form.title.data
        body = form.body.data

        # Create Cursor
        cur = mysql.connection.cursor()

        # Execute
        cur.execute("INSERT INTO recommendation(profile, author, body) VALUES(%s, %s, %s)",(id, session['username'], body))

        # Commit to DB
        mysql.connection.commit()

        #Close connection
        cur.close()

        flash('Recommendation added', 'success')
        redirect_to = "profile/" + id
        print("kya hai ye %s",redirect_to,file=sys.stderr)
        return redirect(redirect_to)

    return render_template('add_recommendation.html', form=form)
