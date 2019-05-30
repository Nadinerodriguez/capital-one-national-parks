""" This file holds all of the functions that interact with our API """
import requests
from . import api_keys


def find_parks(state_picked):
    """ Find parks from state code """
    API_KEY = api_keys.get_nps_api_key()
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
