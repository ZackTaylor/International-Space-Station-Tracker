"""ISS tracker."""
import json
import urllib.request

ASTRONAUTS_URL = 'http://api.open-notify.org/astros.json'
POSITION_URL = 'http://api.open-notify.org/iss-now.json'


def get_api_data(url):
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


# TEST CODE
astros_data = get_api_data(ASTRONAUTS_URL)
number_astronauts = astros_data['number']
iss_passengers = [p['name'] for p in astros_data['people']]
print(iss_passengers)
