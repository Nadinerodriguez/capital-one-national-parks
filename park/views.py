from django.shortcuts import render
from django.http import HttpResponse
from . import api_functions

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
            context = api_functions.find_parks(state_picked) # list of locations for state
    return render(request, 'park/results.html', context)

# def detail(request):
#     if request.method == "GET":
#         park_selected = request.GET.get('park-selected')
#
#         #If user did not pick a park/Accessed url directly
#         if park_selected is None:
#             return HttpResponse("Error. Please pick a park from the results page")
#
#         else:
#             print("A park was selected:", park_selected)
#             pass
#     return render(request, 'park/detail.html')

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

    # TODO: build context
    access_token = api_keys.get_mapbox_access_token()

    return render(request, 'park/detail.html', {
        'lat': lat,
        'long': long,
        'full_name': full_name,
        'access_token': access_token,
    })
