from apscheduler.schedulers.blocking import BlockingScheduler
from twitter_tunes.scripts import twitter_bot
import logging

logging.basicConfig()
sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=60)
def timed_job():
    twitter_bot.main()

sched.start()
