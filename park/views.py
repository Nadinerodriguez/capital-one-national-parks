from django.shortcuts import render
import requests
from django.http import HttpResponse

def test(request):
    return render(request,'park/test.html')

def index(request):
    return render(request, 'park/index.html')

def results(request):
    if request.method == "GET":
        state_picked = request.GET.get('state-picked')

        #If user did not pick a state/Accessed url directly
        if state_picked is None:
            return HttpResponse("Error. Please pick a state from the homepage")

        else:
            context = find_parks_using_API(state_picked) # list of locations for state
    return render(request, 'park/results.html', context)

#Helper function that calls the API
def find_parks_using_API(state_picked):
    """ Helper function that calls the API """
    # Parsing Parameters
    state_picked = state_picked.upper()
    API_KEY = "BfjJkQ8FsI9gI33vN95G8f2tunWF5qZFYBZFOwb0"
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

    # Context to pass into template
    # designation = json_object['designation']
    # title = json_object['fullName']
    # states = json_objects['states']
    # description = json_object['description']
    # images_array = json_object['images'] #Array of 5 images
    # images_url_array = []
    # for image_dict in images_array:
    #     image_url = image_dict['url']
    #     image_url_array.append(image_url)
    #
    # output = {
    #     'designation': designation,
    #     'title': title,
    #     'states': states,
    #     'description': description,
    #     'images': images_url_array,
    # }
    #
    # return output

def convert_abbreviation_to_full(state_abbrev):
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
