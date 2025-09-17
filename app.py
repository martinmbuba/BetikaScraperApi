from flask import Flask
from flask_cors import CORS
from app.main.service.game_service import get_all_games

app = Flask(__name__)
CORS(app)

@app.route('/api/games', methods=['GET'])
def games():
    games = get_all_games()
    return {'games': games}

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
