import pymysql
import pymysql.cursors
import query_maker
from tabulate import tabulate
import click

db_conn = pymysql.connect(host='localhost',
                          user='kunwar',
                          password='',
                          db='dota',
                          cursorclass=pymysql.cursors.DictCursor)

db_curr = db_conn.cursor()


def print_query(query):
    try:
        db_curr.execute(query)
        output = db_curr.fetchall()
    except:
        db_curr.rollback()

    if not output:
        return

    headers = [name.replace('_', ' ').title()
               for name in list(output[0].keys())]

    output = [list(row.values()) for row in output]

    click.secho(tabulate(output, headers, tablefmt='fancy_grid'), fg='yellow')


def team_matches(team):
    '''Get all matches played by a team'''
    query = query_maker.all_match_team(team)
    print_query(query)


def player_matches(player):
    '''Get all matches played by a player'''
    query = query_maker.all_match_player(player)
    print_query(query)


def match_against(team1, team2):
    '''Get all matches played between 2 given teams'''
    query = query_maker.all_match_two_teams(team1, team2)
    print_query(query)


def winrate_greater_player(player, x):
    '''Get all Heroes with win-rate >= x, for a certain player'''
    query = query_maker.hero_win_rate(player, x)
    print_query(query)

def winrate_greater(x):
    '''Get all Heroes with win-rate >= x'''
    query = query_maker.hero_win_rate_all(x)
    print_query(query)

def wins_by_pattr(player, primary_att):
    '''Total wins by a player for all heroes of a given primary attribute'''
    query = query_maker.player_attr_wins(player, primary_att)
    print_query(query)

def total_time(player):
    '''Total time by a player in all matches'''
    query = query_maker.total_time_player(player)
    print_query(query)

def total_wins(player):
    '''Total wins by player in all the matches'''
    query = query_maker.total_win_player(player)
    print_query(query)

def find_hero(hero):
    '''Get info about a hero'''
    query = query_maker.partial_search_hero(hero)
    print_query(query)

def find_player(player):
    '''Get info about a player'''
    query = query_maker.partial_search_player(player)
    print_query(query)