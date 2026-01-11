from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio
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

scheduler =  AsyncIOScheduler()
msg = MIMEMultipart()
msg['From'] = constants.SMTP_USER


def start_scheduler():

    scheduler.start()    
    # load_existing_jobs()

def Email_For_Approval(subject="Deployment Approval Reminder", message="This is a reminder to approve the scheduled deployment.", cc:list = []):
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

        # server.send_message(msg)

        server.quit()
        print("Email sent successfully!")
        # scheduling deployment 
        
        # db = SessionLocal()
        # try:
        #     deployment = db.query(Deployment).filter(Deployment.id == deployment_id).first()
        #     if deployment:
        #         load_new_deploymwnt_jobs(deployment.scheduled_time ,deployment_id)
        # finally:
        #     db.close()
    except Exception as e:
        print("Failed to send email:", e)
        
def load_existing_jobs():
    db = SessionLocal()
    try:
        remaining_Deployments = db.query(Deployment).filter(Deployment.approval_reminder_time >datetime.now())
        
        for remaining_Deployment in remaining_Deployments:
                scheduler.add_job(Email_For_Approval,
                                'date',run_date = remaining_Deployment.approval_reminder_time, args=[remaining_Deployment.id] )
    finally:
        db.close()

def load_new_deploymwnt_jobs(approval_date,deployment_id):
    
        # db = SessionLocal()
        # deployment = db.query(Deployment).filter(Deployment.id == deployment_id).first()
        # deployment_time  = deployment.scheduled_time

        deployment_time  = approval_date + timedelta(minutes=1)
        
        # schedule deployment
        scheduler.add_job(
            deployment_Job,
            'date',
            run_date = deployment_time,
            args=[deployment_id, 74904249]
            ),      
        # schedule approval
        scheduler.add_job(
            Email_For_Approval,
            'date',
            run_date = approval_date,
            args=[
                "Deployment Approval Reminder",
                f"This is a reminder to approve the deployment scheduled on {deployment_time}.",
                []],
            id=f'approval_reminder_{deployment_id}'
            ),      
    
TargetBranches = ['push_from', 'Pipleine3', 'Pipleine2']
# TargetBranches = ['prodwebserver', 'prodsocketserver', 'CSworkder']

async def deployment_Job(deployment_id,Project_id):
    tasks = []

    for target_branch in TargetBranches:
        task = asyncio.create_task(
            Create_Merge_Request(
                project_id = Project_id,
                target_branch=target_branch,
            )
        )
        tasks.append(task)

    statuses = await asyncio.gather(*tasks)
    print(statuses)
    pipline_status = "succeeded"  
    for status in statuses:
        if status != 'passed':
            pipline_status = status    
    
    print(pipline_status)
    return pipline_status
 
    
    # Email_For_Approval(deployment_id=None, subject="Deployment Completed", message=f"The scheduled deployment has been {status_for_email}.",)
