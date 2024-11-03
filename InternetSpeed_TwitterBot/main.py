from test_internet_speed import TestSpeed
import internet_speed_twitter_bot as bot


promised_speed = 100


# get speed values

test_speed = TestSpeed()
test_speed.test_internet_speed()
download_speed = test_speed.download
upload_speed = test_speed.upload

# If the calculated speed is below promised speed, send the tweet to ISP

if download_speed < promised_speed or upload_speed < promised_speed:
    bot.post_tweet(download_speed, upload_speed, promised_speed)



