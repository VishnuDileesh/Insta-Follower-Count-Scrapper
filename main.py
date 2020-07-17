from requests_html import HTMLSession
from pynotifier import Notification
import time

session = HTMLSession()

while True:

    r = session.get('https://www.instagram.com/peoplewhocode/')

    r.html.render()

    profileInfo = r.html.find('.g47SY')

    followersInfo = profileInfo[1]

    count = followersInfo.attrs['title']

    #print(count)

    Notification(
        title='InstaFollowerScraper',
        description='Follower Count: {}'.format(count),
        duration=2,  # Duration in seconds
        urgency=Notification.URGENCY_CRITICAL).send()

    time.sleep(10)
