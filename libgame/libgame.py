from flask import Flask, render_template, request, \
    redirect, session,flash  # Importing flask, render template(helper), request(take information's from formulary), redirect(helper, redirect the HTML to next page), session(Sessions in Flask allow you to retain information across multiple requests), flash(The flash function is a helper in Flask that saves messages temporarily and returns them to be displayed to the user."




class Game:
    def __init__(self, name, category, console):
        self.name = name
        self.category = category
        self.console = console


game1 = Game('Darksiders', 'Action', 'Mult-platform')
game2 = Game('Phamosphobia', 'Horror', 'Computer')
game3 = Game('Skyrim', 'RPG', 'Mult-platform')
lib = [game1, game2, game3]

app = Flask(__name__)  # Specify the module
app.secret_key = 'luka'


@app.route('/')  # Create a route
def index():
    return render_template('list.html', title='Games',
                           games=lib)  # The variable title in render template push the stored information in HTML code "<h1>{{title}}</h1>"


@app.route('/new')
def new():
    return render_template('new.html', title='New Game')


@app.route('/create',
           methods=['POST', ])  # However, if you want the route to accept both POST requests, you can specify.
def create():
    name = request.form["name"]
    category = request.form["category"]
    console = request.form["console"]
    game = Game(name, category, console)
    lib.append(game)  # In Python, if you want to add something to a list, you can use methods like append()
    return redirect('/')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/authentication', methods=['POST', ])
def authentication():
    if 'Gengar' == request.form['password']:
        session['user_login'] = request.form['username']
        flash( session['user_login'] + 'Successful Login')
        return redirect('/')
    else:
        flash('Wrong Password or Username ')
        return redirect('/login')


app.run(debug=True)  # running the application
