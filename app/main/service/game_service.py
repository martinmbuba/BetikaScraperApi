import json

import requests


def get_all_games():
    loaded_data = load_data('match_details')
    games = []
    for data in loaded_data:
        game = {
            'game_id': data['game_id'],
            'country': data['country'],
            'sport': data['sport_name'],
            'league': data['league_name'],
            'away_team': data['away_team'],
            'home_team': data['home_team'],
            'starting_time': data['starting_time']
        }
        games.append(game)
    return games


def get_a_game(game_id):
    loaded_data = load_data('match_details')
    for data in loaded_data:
        if data['game_id'] == game_id:
            game = {
                'game_id': data['game_id'],
                'country': data['country'],
                'sport': data['sport_name'],
                'league': data['league_name'],
                'away_team': data['away_team'],
                'home_team': data['home_team'],
                'starting_time': data['starting_time'],
                'odds_url': data['odds_url']
            }
            return game
    return None


def get_games_by_country(country):
    loaded_data = load_data('match_details')
    games = []
    for data in loaded_data:
        if data['country'] == country:
            game = {
                'game_id': data['game_id'],
                'country': data['country'],
                'sport': data['sport_name'],
                'league': data['league_name'],
                'away_team': data['away_team'],
                'home_team': data['home_team'],
                'starting_time': data['starting_time']
            }
            games.append(game)
    return games


def get_games_by_sport(sport):
    loaded_data = load_data('match_details')
    games = []
    for data in loaded_data:
        if data['sport_name'] == sport:
            game = {
                'game_id': data['game_id'],
                'country': data['country'],
                'sport': data['sport_name'],
                'league': data['league_name'],
                'away_team': data['away_team'],
                'home_team': data['home_team'],
                'starting_time': data['starting_time']
            }
            games.append(game)
    return games


def get_games_by_league(country, league):
    loaded_data = load_data('match_details')
    games = []
    for data in loaded_data:
        if data['country'] == country and data['league_name'] == league:
            game = {
                'game_id': data['game_id'],
                'country': data['country'],
                'sport': data['sport_name'],
                'league': data['league_name'],
                'away_team': data['away_team'],
                'home_team': data['home_team'],
                'starting_time': data['starting_time']
            }
            games.append(game)
    return games


def load_data(file_name):
    with open(file_name + '.json') as f:
        collected_data = json.load(f)
    return collected_data


def extract_time(param):
    date, time = param.split(" ")
    year, month, day = date.split("-")
    hours, minutes, seconds = time.split(":")
    return datetime(
        year=int(year),
        month=int(month),
        day=int(day),
        hour=int(hours),
        minute=int(minutes),
        second=int(seconds)
    )


def extract_game_odds(odds_url):
    response = requests.get(url=odds_url)
    response_data = response.json().get('data')

    return_data = []
    for data in response_data:
        odd_data = {}
        odd_data['name'] = data['name']
        odds = data['odds']
        odd_info = []
        for odd in odds:
            odds_dict = {}
            odds_dict['display'] = odd['display']
            odds_dict['key'] = odd['odd_key']
            odds_dict['value'] = odd['odd_value']
            odd_info.append(odds_dict)
        odd_data['odds'] = odd_info
        return_data.append(odd_data)

    return return_data
