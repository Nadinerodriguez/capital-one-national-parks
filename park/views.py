from django.shortcuts import render
from django.http import HttpResponse
from . import api_functions
from . import api_keys

# Render for index view
def index(request):
    return render(request, 'park/index.html')

# Render for results view
def results(request):
    if request.method == "GET":
        state_picked = request.GET.get('state-picked')

        #If user did not pick a state/Accessed url directly
        if state_picked is None:
            return HttpResponse("Error. Please pick a state from the homepage")

        else:
            context = api_functions.find_parks(state_picked) # list of locations for state
    return render(request, 'park/results.html', context)

# Render for results view (through search)
def search(request):
    if request.method == "GET":
        query = request.GET.get('search-query')

        if query is None:
            return HttpResponse("Error. Please search/pick a state from the home page.")
        else:
            context = api_functions.find_parks_with_search(query)
    return render(request, 'park/results.html', context)


# Render for detail view
def detail(request):
    if request.method == "POST":
        park_selected = request.POST.get('park-code')
        lat_long = request.POST.get('lat-long')
        full_name = request.POST.get('full-name')

        print("A park was selected!", park_selected)
        print("Lat long:", lat_long)
        print("Full name:", full_name)
        print(lat_long == "")

        # clean up lat_long string
        if lat_long != "":
            lat_long_arr = lat_long.split(", ")
            lat = lat_long_arr[0][4:]
            long = lat_long_arr[1][5:]
            print("Lat: ", lat)
            print("Long: ", long)
        else: # If no lat long from api for this location
            print("Empty lat and long")
            lat = ""
            long = ""
    else:
        return HttpResponse("Error accessing directly. Please pick a park from the results page.")

    access_token = api_keys.get_mapbox_access_token()
    overview_dictionary = api_functions.find_overview_details(park_selected)
    alerts_dictionary = api_functions.find_alerts(park_selected)
    articles_dictionary = api_functions.find_articles(park_selected)
    news_dictionary = api_functions.find_news(park_selected)
    events_dictionary = api_functions.find_events(park_selected)
    visitor_centers_dictionary = api_functions.find_visitor_centers(park_selected)
    campgrounds_dictionary = api_functions.find_campgrounds(park_selected)
    places_dictionary = api_functions.find_places(park_selected)
    lesson_plans_dictionary = api_functions.find_lesson_plans(park_selected)
    people_dictionary = api_functions.find_people(park_selected)

    return render(request, 'park/detail.html', {
        'lat': lat,
        'long': long,
        'full_name': full_name,
        'access_token': access_token,
        'overview': overview_dictionary['overview'],
        'alerts_total': alerts_dictionary['alerts_total'],
        'alerts': alerts_dictionary['alerts'],
        'articles_total': articles_dictionary['articles_total'],
        'articles': articles_dictionary['articles'],
        'news_total': news_dictionary['news_total'],
        'news_releases': news_dictionary['news_releases'],
        'events_total': events_dictionary['events_total'],
        'events': events_dictionary['events'],
        'visitor_centers_total': visitor_centers_dictionary['visitor_centers_total'],
        'visitor_centers': visitor_centers_dictionary['visitor_centers'],
        'campgrounds_total': campgrounds_dictionary['campgrounds_total'],
        'campgrounds': campgrounds_dictionary['campgrounds'],
        'places_total': places_dictionary['places_total'],
        'places': places_dictionary['places'],
        'lesson_plans_total': lesson_plans_dictionary['lesson_plans_total'],
        'lesson_plans': lesson_plans_dictionary['lesson_plans'],
        'people_total': people_dictionary['people_total'],
        'people': people_dictionary['people']
    })
