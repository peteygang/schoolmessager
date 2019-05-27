import urllib
from bs4 import BeautifulSoup
from urllib.request import urlopen
from flask import Flask, render_template, flash, redirect, url_for, request
import re
# from app import app
# app.secret_key = 'a random key'
print('hi')
# print('server name ', app.config["SERVER_NAME"])
app = Flask(__name__)

@app.route('/test')
def hello():
	return 'hello'

@app.route('/')
def index():
	quote_page = 'file:///Users/pecembalest/Desktop/compsci/compscipeople.html'
	data = []
	page = urlopen(quote_page, 'r')
	soup = BeautifulSoup(page, 'html.parser')
	counter = 0
	names = soup.find_all('span', attrs={'class': 'y4ihN'})
	for name in names:
		names[counter] = name.text.strip('<span class="y4ihN"></span>')
		db.session.add(name)
		db.session.commit()
		counter = counter +1
	print(names)
	thecounter = 0 
	realemails = []
	tags = []
	emails = soup.find_all('a')
	for email in emails:
		if email.get('href') != None:
			tags.append(email.get('href'))

	for tag in tags:
		if tag.count('https://mail.google.com/mail/?view') == 1:
			realemails.append(tag)
	
	print(realemails)
	return render_template('realclassmates.html', names = names, realemails = realemails)

@app.route('/classmates')
def classmates():
	return render_template('yourclassmates.html')

	
if __name__ == "__main__":
    app.run()


# , attrs={'href': re.compile('^https://mail.google.com/mail/?')}
# for email in emails:
# 	emails[counter] = email.strip('target="_blank"><div class="PDXc1b MbhUzd" jsname="ksKsZd"></div><content class="XuQwKc" jsslot=""><span class="GmuOkf"><svg class="" focusable="false" height="24" viewbox="0 0 24 24" width="24"><path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm-.8 2L12 10.8 4.8 6h14.4zM4 18V7.87l8 5.33 8-5.33V18H4z"></path></svg></span></content></a>')
# 	thecounter = thecounter +1
# re.compile("^https://mail.google.com/"
# <a aria-label="Email gbenedisgrab@packer.edu" class="IrxBzb TpQm9d" href="https://mail.google.com/mail/?view=cm&amp;fs=1&amp;to=gbenedisgrab%40packer.edu&amp;authuser=0" 


# Jack = soup.find(attrs={'data-current-student-id': '7018766'})

# price_box = soup.find('div', attrs={'class':'price'})
# price = price_box.text
# print(price)
# data.append((name, price))

# ########## Saved to csv ##########

# import csv 
# from datetime import datetime

# with open('index.csv', 'a') as csv_file:
# 	writer = csv.writer(csv_file)
# 	for name, price in data:
# 		writer.writerow([name, price, datetime.now()])
# 		writer.writerow('')

# @app.route('/index', methods=['GET', 'POST'])
# @login_required
# def index():
#     form = PostForm()
#     if form.validate_on_submit():
#         post = Post(body=form.post.data, author=current_user)
#         db.session.add(post)
#         db.session.commit()
#         flash('Your post is now live!')
#         return redirect(url_for('index'))
#     posts = current_user.followed_posts().all()
#     return render_template('index.html', title='Home', form=form,
#                            posts=posts)


# def login():
#     if current_user.is_authenticated:
#         return redirect(url_for('index'))
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(username=form.username.data).first()
#         if user is None or not user.check_password(form.password.data):
#             flash('Invalid username or password')
#             return redirect(url_for('login'))
#         login_user(user, remember=form.remember_me.data)
#         next_page = request.args.get('next')
#         if not next_page or url_parse(next_page).netloc != '':
#             next_page = url_for('index')
#         return redirect(next_page)
#     return render_template('login.html', title='Sign In', form=form)

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if current_user.is_authenticated:
#         return redirect(url_for('index'))
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         user = User(username=form.username.data, email=form.email.data)
#         user.set_password(form.password.data)
#         db.session.add(user)
#         db.session.commit()
#         flash('Congratulations, you are now a registered user!')
#         return redirect(url_for('login'))
#     return render_template('register.html', title='Register', form=form)

# @app.route('/feed')
# def feed():
# 	pass