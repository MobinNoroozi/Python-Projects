
## Websites / services to use
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


Create an account at twilio.com. get your 
   - Account SID
   - Auth Token
   - A Twilio phone number (buy/request a trial number). On a trial account, recipient numbers must be verified.


Install dependencies (if you don't have them):
   - pip install --upgrade pip
   - pip install requests twilio


Set environment variables (example for macOS/Linux):

    export STOCK_API_KEY="YOUR OWN API KEY FROM ALPHAVANTAGE"
    export NEWS_API_KEY="YOUR OWN API KEY FROM NEWSAPI"
    export TWILIO_SID="YOUR TWILIO ACCOUNT SID"
    export TWILIO_AUTH_TOKEN="YOUR TWILIO AUTH TOKEN"
      - (optional) export https_proxy="http://proxy:port"  # if behind a proxy

   Recommended additional env vars you can add and use by editing the script:
   - TWILIO_ACCOUNT_SID
   - TWILIO_FROM_NUMBER
   - TWILIO_TO_NUMBER


Edit the script `main.py` and replace placeholders (or change it to read the values from env vars):
   - `account_sid = "YOUR ACCOUNT SID"` → set to your Twilio Account SID or change to read from `os.environ.get('TWILIO_ACCOUNT_SID')`
   - `from_="YOUR TWILIO VIRTUAL NUMB   ER"` → your Twilio phone number
   - `to="YOUR TWILIO VERIFIED REAL NUMBER"` → the destination phone number (must be verified on trial accounts)

