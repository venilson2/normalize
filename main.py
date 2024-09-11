from fmconsult.database.connection import DatabaseConnector

from src.database.models.route import Route
from src.database.models.work_schedule import WorkSchedule

db = DatabaseConnector()

def normalize():
    
    db.connect()
    
    work_schedules = WorkSchedule.objects()
    
    print(f'WorkSchedules: {len(work_schedules)}')
    
    for ws in work_schedules:
        
        if str(ws.id) == "5edb0d8b30fc252fb924b4ab":
            print('WorkSchdule:', ws.id)
            subenterprise = Route.objects(id=ws.route.id)
            print('subenterprise:', str(subenterprise[0].subenterprise))
            WorkSchedule.objects(id=ws.id).update_one(set__subenterprise=subenterprise)

normalize()	
