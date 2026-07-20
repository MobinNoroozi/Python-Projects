# Day33_send_sms_if_rainy - main.py
# This script checks the 3-hour weather forecast from OpenWeatherMap for the next
# few time slots and sends an SMS via Twilio if rain (or snow/other precipitation)
# is predicted.
#
# Usage:
#  - Set the environment variable OWM_API_KEY to your OpenWeatherMap API key.
#  - Set the environment variable AUTH_TOKEN to your Twilio Auth Token.
#  - Replace the account_sid, from_ and to values below with your Twilio values
#    (or load them from environment variables if preferred).
#  - Optionally set https_proxy environment variable if you're behind a proxy.

import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

# OpenWeatherMap 5 day / 3 hour forecast endpoint
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

# Read OpenWeatherMap API key from environment variable
api_key = os.environ.get("OWM_API_KEY")

# Twilio account SID. Replace the placeholder with your real account SID,
# or load it from an environment variable (recommended for security):
# account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
account_sid = "YOUR ACCOUNT SID"

# Twilio auth token read from environment variable for safety
auth_token = os.environ.get("AUTH_TOKEN")

# Parameters sent to the OpenWeatherMap API.
# - lat/lon specify the location to check (currently set to coordinates for Bern, Switzerland)
# - appid is the API key
# - cnt is the number of forecast entries to return (each entry is a 3-hour step)
weather_params = {
    "lat": 46.947975,
    "lon": 7.447447,
    "appid": api_key,
    "cnt": 4,
}

# Request the forecast JSON from OpenWeatherMap
response = requests.get(OWM_Endpoint, params=weather_params)
# Raise an exception if the HTTP request failed (non-2xx status code)
response.raise_for_status()
weather_data = response.json()
# Example: weather_data["list"][0]["weather"][0]["id"] is the weather condition code

# OWM condition codes < 700 indicate rain, snow, or other precipitation
will_rain = False
for hour_data in weather_data["list"]:
    # Each forecast entry contains a list under the "weather" key. We take the first
    # element and inspect its "id" field which is an integer code describing the condition.
    condition_code = hour_data["weather"][0]["id"]
    # If the condition code is less than 700, it's precipitation (rain/snow/etc.)
    if int(condition_code) < 700:
        will_rain = True

# If precipitation is expected in any of the checked forecast entries, send an SMS
if will_rain:
    # If you're behind a corporate proxy, Twilio's library needs a http client with
    # proxy settings. This example reads HTTPS proxy from the https_proxy environment
    # variable and configures TwilioHttpClient to use it. If not behind a proxy, you
    # can omit the proxy_client/http_client pieces and call Client(account_sid, auth_token).
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    # Initialize Twilio client with account SID and auth token
    client = Client(account_sid, auth_token, http_client=proxy_client)

    # Create and send the message. Replace the from_ number with your Twilio phone
    # number (virtual number) and the to number with the recipient (must be verified
    # for trial accounts).
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="YOUR TWILIO VIRTUAL NUMBER",
        to="YOUR TWILIO VERIFIED REAL NUMBER"
    )
    print(message.status)
