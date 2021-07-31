import schedule
import subprocess
import time

def runBot():
    subprocess.run("python3 Scheduled_Bot.py")

schedule.every().day.at("09:00").do(runBot)

while True:
    schedule.run_pending()
    time.sleep(1)