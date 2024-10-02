import time
from fmconsult.database.connection import DatabaseConnector
from src.database.models.work_schedule import WorkSchedule

db = DatabaseConnector()

def normalize():
    try:
        # Inicia a contagem do tempo
        start_time = time.time()
        
        db.connect()

        # Carrega todos os WorkSchedules
        print('Step 1: Fetching all WorkSchedules...')
        work_schedules = WorkSchedule.objects(deleted=False, embeddeds__exists=False)
        
        print('Step 2: Total WorkSchedules found:', len(work_schedules))
        
        updates = []
        index = 0

        for ws in work_schedules:
            index += 1
            print(f'Processing WorkSchedule {index}/{len(work_schedules)}')
            print('WorkSchedule ID:', ws.id)
       
            embeddeds = {
                'enterprise': {
                    'id': ws.enterprise.id,
                    'name': ws.enterprise.name,
                } if 'enterprise' in ws else None,
                'vehicle': {
                    'id': ws.vehicle.id,
                    'description': ws.vehicle.description,
                    'plate': ws.vehicle.plate,
                    'description': ws.vehicle.description,
                    'is_online': ws.vehicle.is_online,
                    'icon': ws.vehicle.icon,
                } if 'vehicle' in ws else None,
                'route': {
                    'id': ws.route.id,
                    'hexcode': ws.route.hexcode,
                    'description': ws.route.description,
                    'acronym': ws.route.acronym if hasattr(ws.route, 'acronym') else None,
                    'subenterprise': {
                        'id': ws.route.subenterprise.id,
                        'name': ws.route.subenterprise.name,
                    },
                    'color': ws.route.color,
                    'direction': ws.route.direction,
                    'schedule_grid': ws.route.schedule_grid,
                } if 'route' in ws else None,
                'driver': {
                    'id': ws.driver.id,
                    'name': ws.driver.name,
                } if 'driver' in ws else None,
                'subenterprise': {
                    'id': ws.route.subenterprise.id,
                    'name': ws.route.subenterprise.name,
                    'hexcode': ws.route.subenterprise.hexcode,
                    'active': ws.route.subenterprise.active,
                } if 'subenterprise' in ws else None,
                'start_point': {
                    'id': ws.start_point.id,
                    'description': ws.start_point.description,
                    'location': {
                        'latitude': ws.start_point.location['coordinates'][0] if ws.start_point.wrong_location else ws.start_point.location['coordinates'][1],
                        'longitude': ws.start_point.location['coordinates'][1] if ws.start_point.wrong_location else ws.start_point.location['coordinates'][0]
                    },
                    'wrong_location': ws.start_point.wrong_location
                },
                'end_point': {
                    'id': ws.end_point.id,
                    'description': ws.end_point.description,
                    'location': {
                        'latitude': ws.end_point.location['coordinates'][0] if ws.end_point.wrong_location else ws.end_point.location['coordinates'][1],
                        'longitude': ws.end_point.location['coordinates'][1] if ws.end_point.wrong_location else ws.end_point.location['coordinates'][0]
                    }
                },
                'waypoints': []
            }

            if hasattr(ws, 'waypoints') and len(ws.waypoints) > 0:
                waypoints_embedded = []
                for wp in ws.waypoints:
                    wr_embedded = {
                        'point': {
                            'id': wp.point.id,
                            'description': wp.point.description,
                            'location': {
                                'latitude': wp.point.location['coordinates'][0] if wp.point.wrong_location else wp.point.location['coordinates'][1],
                                'longitude': wp.point.location['coordinates'][1] if wp.point.wrong_location else wp.point.location['coordinates'][0]
                            },
                        },
                        'incoming_time': wp.incoming_time,
                        'outcoming_time': wp.outcoming_time,
                        'passengers': []
                    }
                    
                    if len(wp.passengers) > 0:
                        for p in wp.passengers:
                            passenger_dict = {
                                'passenger': p['passenger'],
                                'status': p['status']
                            }
                            wr_embedded['passengers'].append(passenger_dict)
                    waypoints_embedded.append(wr_embedded)
                embeddeds['waypoints'] = waypoints_embedded
       
            updates.append({
                "id": ws.id,
                'embeddeds': embeddeds
            })

        # Realiza atualizações em massa (bulk update) para otimizar o processo
        print('Step 3: Preparing updates...')
        if updates:
            for update in updates:
                print('Updating WorkSchedule ID:', update["id"])
                WorkSchedule.objects(id=update["id"]).update_one(set__embeddeds=update["embeddeds"])

        # Calcula o tempo total e imprime o resultado
        end_time = time.time()
        total_time = (end_time - start_time) / 60  # Converte para minutos
        
        print('============ Done ============')
        print(f'Total processing time: {total_time:.2f} minutes')

    except Exception as e:
        print(f'Error occurred: {e}')

normalize()