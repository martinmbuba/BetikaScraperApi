import os
import unittest

from flask_script import Manager

from app import blueprint
from app.main import create_app
from app.main.service.game_scraper import collect_games_details

app = create_app(os.getenv('FLASK_ENV') or 'development')
app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)


@manager.command
def run():
    app.run()


@manager.command
def new_games():
    if os.path.exists('match_details.json'):
        os.remove('match_details.json')
    collect_games_details()


@manager.command
def test():
    """Run the tests"""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
