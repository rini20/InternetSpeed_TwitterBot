This Twitterbot is a Python-based automation project that tests your internet speed and tweets your ISP if the speed falls below a specified threshold.

Features:

- Automated Internet Speed Testing: Uses Selenium to navigate to speedtest.net and perform an internet speed test.
- Automated Tweeting: Uses Tweepy to post a tweet tagging your ISP if the download or upload speed is below the promised threshold.
- Customizable Threshold: Set your own minimum download and upload speed to trigger a tweet.

Requirements:

- Python 3.12
- Selenium: For automating the speed test.
- Tweepy: For interacting with Twitter’s API.
- Google Chrome and ChromeDriver (Make sure they are compatible).

Installation

1. Clone this repository:
    git clone https://github.com/rini20/InternetSpeed_TwitterBot.git
    cd internet-speed-twitterbot

2. Install the required packages:

    pip install -r requirements.txt

3. Configure Twitter API credentials:

    a. Set up a Twitter Developer account and create an app to get API keys.
    b. Add your API keys to the .env file (which I've not included) in the project directory. The format is:
        API_KEY = your api_key""
        API_SECRET_KEY = "your api_secret_key"
        ACCESS_TOKEN = "your_access_token"
        ACCESS_TOKEN_SECRET = "your access_token_secret"
    c. Set your ISP's Twitter handle in the message and the promised download/upload speed in the script.

Run the script with:
 python main.py

The bot will:

Perform an internet speed test using Selenium.
Compare the results with your specified threshold.
If the speed is below the threshold, post a tweet tagging your ISP
