from flask import Flask, render_template  # Importing flask and render template(helper)


class Game:
    def __init__(self, name, category, console):
        self.name = name
        self.category = category
        self.console = console


app = Flask(__name__)  # Specify the module


@app.route('/start')  # Create a route
def hello():
    game1 = Game('Darksiders', 'Action', 'Mult-platform')
    game2 = Game('Phamosphobia', 'Horror', 'Computer')
    game3 = Game('Skyrim', 'RPG', 'Mult-platform')
    lib = [game1, game2, game3]
    return render_template('list.html', title='Games', games=lib)  # The variable title in render template push the stored information in HTML code "<h1>{{title}}</h1>"


@app.route('/new')
def new():
    return render_template('new.html', title = 'New Game')


app.run()  # running the application
