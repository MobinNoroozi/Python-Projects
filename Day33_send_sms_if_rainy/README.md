# Send SMS If Rainy

A small Python script that checks the next few forecast entries from OpenWeatherMap and sends an SMS via Twilio if precipitation (rain/snow/etc.) is predicted.

## What this does
- Calls OpenWeatherMap 5-day / 3-hour forecast API for a given latitude/longitude.
- Inspects a few forecast entries; if any weather condition code indicates precipitation, it sends an SMS using Twilio.

## Websites / services to use
- OpenWeatherMap — https://openweathermap.org (get the weather API key)
- Twilio — https://www.twilio.com (get Account SID, Auth Token, and a Twilio phone number)

## How to get the API keys
1. OpenWeatherMap
   - Create an account on openweathermap.org.
   - Go to your profile → API keys and create/copy an API key.

2. Twilio
   - Create an account at twilio.com.
   - In the Twilio Console you will find:
     - Account SID
     - Auth Token
     - A Twilio phone number (buy/request a trial number). On a trial account, recipient numbers must be verified.

## Setup (quick)
1. Optional: create and activate a virtual environment (recommended)
   - python -m venv venv
   - On macOS/Linux: source venv/bin/activate
   - On Windows (PowerShell): .\venv\Scripts\Activate.ps1

2. Install dependencies (if you don't have them):
   - pip install --upgrade pip
   - pip install requests twilio


3. Set environment variables (example for macOS/Linux):
   - export OWM_API_KEY="your_openweather_api_key"
   - export AUTH_TOKEN="your_twilio_auth_token"
   - (optional) export https_proxy="http://proxy:port"  # if behind a proxy

   Recommended additional env vars you can add and use by editing the script:
   - TWILIO_ACCOUNT_SID
   - TWILIO_FROM_NUMBER
   - TWILIO_TO_NUMBER

4. Edit the script `main.py` and replace placeholders (or change it to read the values from env vars):
   - `account_sid = "YOUR ACCOUNT SID"` → set to your Twilio Account SID or change to read from `os.environ.get('TWILIO_ACCOUNT_SID')`
   - `from_="YOUR TWILIO VIRTUAL NUMBER"` → your Twilio phone number
   - `to="YOUR TWILIO VERIFIED REAL NUMBER"` → the destination phone number (must be verified on trial accounts)

5. Run the script:
   - python Day33_send_sms_if_rainy/main.py

## Notes & tips
- The OpenWeatherMap endpoint returns forecast steps every 3 hours. The script inspects a small number of upcoming entries (`cnt` in the script) — increase or decrease as needed.
- The script uses a simple heuristic: OpenWeatherMap condition codes < 700 indicate precipitation (rain/snow/etc.). This covers most precipitation cases.
- If you're not behind a proxy, you can simplify Twilio initialization by removing the TwilioHttpClient/proxy code.
- Keep API keys and auth tokens out of source control — use environment variables or a secrets manager.

