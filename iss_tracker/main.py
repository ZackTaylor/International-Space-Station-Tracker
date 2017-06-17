"""ISS tracker."""
import json
import urllib.request
import turtle

ASTRONAUTS_URL = 'http://api.open-notify.org/astros.json'
LOCATION_URL = 'http://api.open-notify.org/iss-now.json'


def api_data(url):
    """Get the JSON data from the specified NASA API."""
    url = url
    response = urllib.request.urlopen(url)
    # data came as bytes so convert into string to be parsed
    string_response = response.read().decode("utf-8")
    result = json.loads(string_response)

    if result['message']:
        return result
    else:
        return "Something went wrong."


def display_craft_passengers():
    """Show number of astronauts and name of astronauts."""
    astros_data = api_data(ASTRONAUTS_URL)
    number_astronauts = astros_data['number']
    message = "There are " + str(number_astronauts) + " astronauts in space: \n"
    # Save all astronauts plus a new line in a list
    iss_passengers = [astronaut['name'] + "\n" for astronaut in astros_data['people']]

    for person in iss_passengers:
        message += person

    return(message)


def craft_location():
    """Pull craft location sats from NASA API. Return latitude and longitude."""
    craft_data = api_data(LOCATION_URL)
    location = craft_data['iss_position']
    lat = location['latitude']
    lon = location['longitude']

    return [lat, lon]


def draw_map():
    """Draw map gif in new window."""
    screen = turtle.Screen()
    screen.setup(720, 360)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.bgpic('images/map.gif')


# TEST CODE
draw_map()
turtle.done()
