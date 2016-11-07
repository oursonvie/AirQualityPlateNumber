import schedule
import time
import bearychat
import moment

def job():
    print("I'm working...")
    bearychat.bearySend(moment.now().timezone("Asia/Shanghai").format("YYYY-M-D h:m:s A"))

## time is based on UTC time, there means -8:00
## 6:00 local time is 22:00 UTC time

schedule.every().day.at("22:00").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)
