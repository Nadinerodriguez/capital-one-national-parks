""" This file holds all of the functions that interact with our API """
import requests
from . import api_keys

API_KEY = api_keys.get_nps_api_key()

def find_parks(state_picked):
    """ Find parks from state code """
    global API_KEY
    # Parsing Parameters

    state_picked = state_picked.upper()
    fields = "&fields=images"
    url = "https://developer.nps.gov/api/v1/parks?stateCode=" + state_picked + "&api_key=" + API_KEY + fields

    # API Call
    response = requests.get(url)
    json_object = response.json()
    locations = json_object['data'] #Array of dictionaries

    # Convert abbreviation
    state_name = convert_abbreviation_to_full(state_picked)

    return {
        'state_name': state_name,
        'locations':locations
    }

def convert_abbreviation_to_full(state_abbrev):
    """ Helper function for formatting """
    states_dictionary = {
        "AL": "Alabama",
        "AK": "Alaska",
        "AZ": "Arizona",
        "AR": "Arkansas",
        "CA": "California",
        "CO": "Colorado",
        "CT": "Connecticut",
        "DE": "Delaware",
        "FL": "Florida",
        "GA": "Georgia",
        "HI": "Hawaii",
        "ID": "Idaho",
        "IL": "Illinois",
        "IN": "Indiana",
        "IA": "Iowa",
        "KS": "Kansas",
        "KY": "Kentucky",
        "LA": "Louisiana",
        "ME": "Maine",
        "MD": "Maryland",
        "MA": "Massachusetts",
        "MI": "Michigan",
        "MN": "Minnesota",
        "MS": "Mississippi",
        "MO": "Missouri",
        "MT": "Montana",
        "NE": "Nebraska",
        "NV": "Nevada",
        "NH": "New Hampshire",
        "NJ": "New Jersey",
        "NM": "New Mexico",
        "NY": "New York",
        "NC": "North Carolina",
        "ND": "North Dakota",
        "OH": "Ohio",
        "OK": "Oklahoma",
        "OR": "Oregon",
        "PA": "Pennsylvania",
        "RI": "Rhode Island",
        "SC": "South Carolina",
        "SD": "South Dakota",
        "TN": "Tennessee",
        "TX": "Texas",
        "UT": "Utah",
        "VT": "Vermont",
        "VA": "Virginia",
        "WA": "Washington",
        "WV": "West Virginia",
        "WI": "Wisconsin",
        "WY": "Wyoming"
    }
    return states_dictionary[state_abbrev]

def find_alerts(park_code):
    global api_key
    url = "https://developer.nps.gov/api/v1/alerts?parkCode=" + park_code + "&api_key=" + API_KEY

    response = requests.get(url)
    json_object = response.json()

    alerts_total = json_object['total']
    alerts = json_object['data']

    return {
        'alerts_total': alerts_total,
        'alerts': alerts
     }

def find_articles(park_code):
    global api_key
    url = "https://developer.nps.gov/api/v1/articles?parkCode=" + park_code + "&api_key=" + API_KEY

    response = requests.get(url)
    json_object = response.json()

    articles_total = json_object['total']
    articles = json_object['data']

    return {
        'articles_total': articles_total,
        'articles': articles
     }

def find_news(park_code):
    global api_key
    url = "https://developer.nps.gov/api/v1/newsreleases?parkCode=" + park_code + "&api_key=" + API_KEY

    response = requests.get(url)
    json_object = response.json()

    news_total = json_object['total']
    news_releases = json_object['data']

    return {
        'news_total': news_total,
        'news_releases': news_releases
     }

def find_events(park_code):
    global api_key
    url = "https://developer.nps.gov/api/v1/events?parkCode=" + park_code + "&api_key=" + API_KEY

    response = requests.get(url)
    json_object = response.json()

    events_total = json_object['total']
    events = json_object['data']

    return {
        'events_total': events_total,
        'events': events
     }
