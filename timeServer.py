from flask import Flask
import schedule
import moment

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/time")
def timeNow():
    return moment.now().timezone("Asia/Shanghai").format("YYYY-M-D h:m:s A")

def job():
    print("I'm working...")

schedule.every(1).seconds.do(job)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
