from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta
from database import SessionLocal
from models.deployment import Deployment
from  gitmanagement.gitlab import Create_Merge_Request

# smpt for emailing
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import constants as constants

from database import SessionLocal
db = SessionLocal()

scheduler =  AsyncIOScheduler()
msg = MIMEMultipart()
msg['From'] = constants.SMTP_USER


def start_scheduler():

    scheduler.start()    
    load_existing_jobs()

def Email_For_Approval(deployment_id, subject="Deployment Approval Reminder", message="This is a reminder to approve the scheduled deployment.", cc:list = []):
    try:
        msg['From'] = constants.SMTP_USER
        msg['To'] = "priyamathur168@gmail.com"
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        if cc:
            msg['Cc'] = ", ".join(cc)

        server = smtplib.SMTP(constants.SMTP_HOST, constants.SMTP_PORT)
        server.starttls()
        server.login(constants.SMTP_USER, constants.SMTP_PASS)

        server.send_message(msg)   # <-- THE CORRECT WAY

        server.quit()
        print("Email sent successfully!")
        # scheduling deployment 
        
        deployment = db.query(Deployment).filter(Deployment.id == deployment_id).first()   
        load_new_deploymwnt_jobs(deployment.scheduled_time ,deployment_id)
    except Exception as e:
        print("Failed to send email:", e)
        
def load_existing_jobs():
    remaining_Deployments = db.query(Deployment).filter(Deployment.approval_reminder_time >datetime.now())
    
    for remaining_Deployment in remaining_Deployments:
            scheduler.add_job(Email_For_Approval,
                            'date',run_date = remaining_Deployment.approval_reminder_time, args=[remaining_Deployment.id] )

def load_new_deploymwnt_jobs(run_date,deployment_id):
        scheduler.add_job(
            deployment_Job,
            'date',
            run_date = run_date,
            args=[deployment_id]
            ),      
    
TargetrRanches = ['push_from', 'Pipleine3', 'Pipleine2']
stat = []
async def deployment_Job(deployment_id, Project_id =74904249):
    Project_id =74904249
    for target_branch in TargetBranches:
        status = await Create_Merge_Request(target_branch =target_branch, project_id=Project_id)
        stat.append(status)
    if "failed" in stat:
        status_for_email = "failed"
    else:
        status_for_email = "succeeded"
     
    
    Email_For_Approval(deployment_id=None, subject="Deployment Completed", message=f"The scheduled deployment has been {status_for_email}.",)
