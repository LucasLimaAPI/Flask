from flask import Flask, render_template, request, \
  redirect, session, \
  flash, \
  url_for  # Importing flask, render template(helper), request(take information's from formulary), redirect(helper, redirect the HTML to next page), session(Sessions in Flask allow you to retain information across multiple requests), flash(The flash function is a helper in Flask that saves messages temporarily and returns them to be displayed to the user."


class Game:
  def __init__(self, name, category, console):
    self.name = name
    self.category = category
    self.console = console


game1 = Game('Darksiders', 'Action', 'Mult-platform')
game2 = Game('Phamosphobia', 'Horror', 'Computer')
game3 = Game('Skyrim', 'RPG', 'Mult-platform')
lib = [game1, game2, game3]


class Users:
  def __init__(self, name, nickname, password):
    self.name = name
    self.nickname = nickname
    self.password = password


# Create user instances
user1 = Users('Lucas Lima', 'LC', 'Gengar')
user2 = Users('Kaline Fernanda', 'KF', 'Kalinda')
user3 = Users('Luka', 'LK', 'Luka')
user4 = Users('Daniel', 'YA', 'Celta')

# Store user instances in the dictionary
users = {
  user1.nickname: user1,
  user2.nickname: user2,
  user3.nickname: user3,
  user4.nickname: user4
}

app = Flask(__name__)  # Specify the module
app.secret_key = 'luka'


@app.route('/')  # Create a route
def index():
  return render_template('list.html', title='Games',
                         games=lib)  # The variable title in render template push the stored information in HTML code "<h1>{{title}}</h1>"


@app.route('/new')
def new():
  if 'user_login' not in session or session['user_login'] is None:
    return redirect(url_for('login', next=url_for('new')))
  return render_template('new.html', title='New Game')


@app.route('/create',
           methods=['POST', ])  # However, if you want the route to accept both POST requests, you can specify.
def create():
  name = request.form["name"]
  category = request.form["category"]
  console = request.form["console"]
  game = Game(name, category, console)
  lib.append(game)  # In Python, if you want to add something to a list, you can use methods like append()
  return redirect(url_for('index'))


@app.route('/login')
def login():
  next = request.args.get('next')
  return render_template('login.html', next=next)


@app.route('/authentication', methods=['POST'])
def authentication():
    username = request.form.get('user')
    password = request.form.get('password')
    next_page = request.form.get('next')

    if username and password:
        user = users.get(username)
        if user and user.password == password:
            session['user_login'] = user.nickname
            flash(user.nickname + " " + 'Successful Login')
            return redirect(next_page) if next_page else redirect(url_for('index'))

    flash('Wrong Password or Username')
    return redirect(url_for('login', next=next_page))



@app.route('/logout')
def logout():
  session['user_login'] = None
  flash("You logged out")
  return redirect(url_for('index'))


if __name__ == '__main__':
  app.run(debug=True)  # running the application
