import requests
from datetime import datetime

#Get ISS pass times for Berlin
params = {"lat":52.520008,"lon": 13.404954,"n" : 30}
response = requests.get("http://api.open-notify.org/iss-pass.json",params=params)
data = response.json()

#Extract times (local time zone) from response and print to console
print("\n The next {} times the ISS will pass Lat: {}, Lon: {}:\n".format(params["n"],params["lat"],params["lon"]))

cursor_day = datetime.fromtimestamp(data["response"][0]["risetime"]).day #cursor for day-check
for passed in data["response"]:
    pass_time = datetime.fromtimestamp(passed["risetime"])
    pass_time_day = pass_time.day

    #Check whether day changed and print seperating dashes
    if(pass_time_day != cursor_day):
        dash_length=len(pass_time.strftime("%Y-%m-%d %H:%M:%S"))
        print("-" * dash_length)
        cursor_day=pass_time_day

    print(datetime.fromtimestamp(passed["risetime"]))
