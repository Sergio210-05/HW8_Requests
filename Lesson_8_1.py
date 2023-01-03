import requests
from pprint import pprint


def all_hero_stats(url):
    """Function to get data from API"""
    resp = requests.get(url)
    # print(resp.status_code)
    # pprint(resp.json())
    return resp.json()


def find_heroes(all_char, *find):
    """Function to filter all_char. *find - list of comparing characters"""
    selected_hero = []
    for hero in all_char:
        if hero['name'] in find:
            selected_hero.append(hero)
    return selected_hero


def stats_list(characters, attribute):
    """Create dictionary - 'hero': attribute value"""
    hero_stats = {}
    for hero in characters:
        hero_stats[hero['name']] = hero['powerstats'][attribute]
    return hero_stats


def hero_comparison(characters, attribute):
    """Characters comparison"""
    hero_list = stats_list(characters, attribute)
    max_stat = max(list(hero_list.values()))
    for character in hero_list:
        if hero_list[character] == max_stat:
            print(f'The most {attribute} character is {character}')
            return character


url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
if __name__ == '__main__':
    all_characters = all_hero_stats(url)
    found_characters = find_heroes(all_characters, 'Hulk', 'Captain America', 'Thanos')
    hero_comparison(found_characters, 'intelligence')
