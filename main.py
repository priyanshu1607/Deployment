from fastapi import FastAPI
from scheduler import start_scheduler,load_new_deploymwnt_jobs,scheduler
import time
from datetime import datetime, timedelta
from database import SessionLocal
from models.deployment import Deployment
from sqlalchemy.orm import Session
from fastapi import Depends
from database import get_db


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
async def create_item(item:dict, db: Session = Depends(get_db)):
    try:
        scheduled_dt = datetime.fromisoformat(item["scheduled_time"])
        crm_record_id = item["crm_record_id"]
        # approval_reminder_time = (scheduled_dt - timedelta(days=1)).replace(
        #     hour=15, minute=30, second=0, microsecond=0
        # )
        approval_reminder_time = (scheduled_dt - timedelta(minutes=1))
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
        
        load_new_deploymwnt_jobs(approval_reminder_time,deployment_obj.id)
        return {"item_received": deployment_obj}
    except Exception as e:
        print(e)
        return 

@app.get("/DbQuerys")
async def readDB(db: Session = Depends(get_db)):
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
        print(index+1, job)
    return 'exsist'




'''
Todo list

1. failure/cancaltion detection in pipline
2. in email add deployment doc URL 
3. follow up email needs to be sent on same email threat   
4. approval acepted 
5. sometime PR is created but not perged without having conflicts
'''

'''pending, created, canceling, canceled'''