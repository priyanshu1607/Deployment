from fastapi import FastAPI
from scheduler import start_scheduler, Email_For_Approval,scheduler
import time
from datetime import datetime, timedelta
from database import SessionLocal
from models.deployment import Deployment

db = SessionLocal()
app = FastAPI()

# Not for production use - just to create tables
@app.on_event("startup")
def startup_event():
    start_scheduler()


if __name__ == "__main__":
    start_scheduler()
    
    # KEEP PROCESS ALIVE
    while True:
        time.sleep(1)
    

@app.post("/plan_deployment")
async def create_item(item:dict):
    try:
        scheduled_dt = datetime.fromisoformat(item["scheduled_time"])
        crm_record_id = item["crm_record_id"]
        approval_reminder_time = (scheduled_dt - timedelta(days=1)).replace(
            hour=15, minute=30, second=0, microsecond=0
        )
        # approval_reminder_time = (scheduled_dt - timedelta(minutes=2))
        deployment_obj = Deployment(
            crm_record_id=crm_record_id,
            scheduled_time=scheduled_dt,
            approval_reminder_time=approval_reminder_time,
            approval_status="pending",
            status="created"
        )
        
        db.add(deployment_obj)
        db.commit()
        db.refresh(deployment_obj)
        
        scheduler.add_job(
            Email_For_Approval,
            'date',
            run_date=approval_reminder_time,
            args=[
                deployment_obj.id,
                "Deployment Approval Reminder",
                f"This is a reminder to approve the deployment scheduled on {scheduled_dt}.",
                []
            ],
            id=f"approval_reminder_{deployment_obj.id}"
        )
        return {"item_received": deployment_obj}
    except Exception as e:
        print(e)
        return 

@app.get("/DbQuerys")
async def readDB():
    db.query(Deployment).delete()
    db.commit()
    return db.query(Deployment).all()

@app.get('/getJObs')
async def getjobs():
    jobs = scheduler.get_jobs()
    if not jobs:
        print("no jobs")
        return 0
    for index, job in enumerate(jobs):
        print(index, job)
    return 'exsist'