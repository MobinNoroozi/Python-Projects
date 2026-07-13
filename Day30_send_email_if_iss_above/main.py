import requests
from datetime import datetime
import smtplib
import time

#👇Fill these out yourself
MY_LONGITUDE = -95.712891
MY_LATITUDE = 37.090240
MY_EMAIL = None
MY_PASSWORD = None


"""
Error codes:
1xx: Hold on 
2xx: Here you go
3xx: go away
4xx: you screwed up
5xx: I screwed up (server)
"""

def is_iss_overhead():
    #Make a request to this url and get the response
    response = requests.get(url="http://api.open-notify.org/iss-now.json")

    #This raise a specific exception based on the error code instead us manually checking every possible error. Been done for us.
    response.raise_for_status()

    data = response.json() #Holds the data and convert it to the json
    iss_longitude = float(data['iss_position']['longitude'])
    iss_latitude = float(data['iss_position']['latitude'])



    if MY_LATITUDE -5 <= iss_latitude <= MY_LATITUDE +5 and MY_LONGITUDE -5 <= iss_longitude <= MY_LONGITUDE +5:
        return True


def is_night():

    parameters = {
        "lat": MY_LATITUDE,
        "lng": MY_LONGITUDE,
        "formatted": 0,

    }   

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


#Every 1 min checks if iss is above, if yes, sends the email
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr = MY_EMAIL, 
                            to_addrs = MY_EMAIL, 
                            msg = "Subject: Look Up\n\nTHe ISS is above you in the sky. look up.", 
                            )