import httpx

gitlab__baseurl = "https://gitlab.com/api/v4/projects/"

headers = {
    "PRIVATE-TOKEN": "glpat-UshTbdzU3Yq_ycENv0CicG86MQp1Oml4ZTRyCw.01.1200mi9iq"
    }
from datetime import datetime, timedelta, timezone


async def Merge_Merge_Request(iid, gitlab_url):
     async with httpx.AsyncClient() as client:
        try:
            
            response = await client.put(gitlab_url + f"/{iid}/merge", headers=headers)
            
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

async def Create_Merge_Request(target_branch ='push_from', project_id=None):
    Project_id =74904249
    gitlab_url = gitlab__baseurl + f"{Project_id}/merge_requests"
    async with httpx.AsyncClient() as client:
        MR_exsists = await client.get(gitlab_url+ f'?source_branch=testingbranch&target_branch={target_branch}&state=opened',headers=headers)
        if not MR_exsists.json():     
            try:
                body ={
                    "source_branch": "testingbranch",
                    "target_branch": target_branch,
                    "title": "Auto merge PR → B1",
                    "remove_source_branch": False,
                    "squash": False,
                    }
                
                response = await client.post(gitlab_url, json=body, headers=headers)
                mr = response.json()
                iid = mr["iid"]
            except httpx.HTTPError as e:
                print(f"An error occurred: {e}")
                return None
        else:
            mr = MR_exsists.json()
            iid = mr[0]["iid"]

        await Merge_Merge_Request(iid, gitlab_url)
        today_start_utc = (datetime.now(timezone.utc) - timedelta(minutes=2)).isoformat()

        piplineurl =gitlab__baseurl + f"{Project_id}/pipelines?ref={target_branch}&created_after={today_start_utc}"
        return await pipeline_status(piplineurl)
                
        
async def Retrigger_Pipeline():
    pass

async def pipeline_status(piplineurl):
    async with httpx.AsyncClient() as client:
            pipleine_response = await client.get(piplineurl, headers=headers)
            pipeline = pipleine_response.json()
            if not pipeline or pipeline[0]["status"] == "pending":
                pipeline_st = await pipeline_status(piplineurl)
                return pipeline_st
            return pipeline[0]["status"]
            
