from flask import Flask, request
from app.tasks import send_email_task, log_time_task
 
app = Flask(__name__)
 
@app.route("/action")
def action():
    email = request.args.get("sendmail")
    talk = request.args.get("talktome")
    if email:
        send_email_task.delay(email)
        return f"Email task sent for {email}!"
    if talk is not None:
        log_time_task()
        return "Current time logged!"
 
    return "No valid query provided."