import time
from fmconsult.database.connection import DatabaseConnector
from src.database.models.route import Route
from src.database.models.work_schedule import WorkSchedule

db = DatabaseConnector()

def normalize():
	try:
		# Inicia a contagem do tempo
		start_time = time.time()
		
		db.connect()

		# Carrega todos os WorkSchedules
		print('Step 1: Fetching all WorkSchedules...')
		work_schedules = WorkSchedule.objects()
		
		print('Step 2: Total WorkSchedules found:', len(work_schedules))
		
		updates = []
		index = 0

		# Coleta todos os IDs das rotas associadas
		print('Step 3: Collecting all associated Route IDs...')
		route_ids = [ws.route.id for ws in work_schedules if ws.route]
		print('Step 4: Total Route IDs collected:', len(route_ids))
		
		# Carrega todas as rotas de uma vez
		print('Step 5: Fetching all Routes associated with WorkSchedules...')
		routes = Route.objects(id__in=route_ids)
		print('Step 6: Total Routes fetched:', len(routes))

		# Mapeia as rotas por ID para fácil acesso
		print('Step 7: Creating Route map...')
		route_map = {route.id: route for route in routes}

		for ws in work_schedules:
			index += 1
			print('Processing WorkSchedule', index, '/', len(work_schedules))
			print('WorkSchedule ID:', ws.id)

			route = route_map.get(ws.route.id)  # Busca a rota a partir do mapa
			if route:
				print('Route found for WorkSchedule:', ws.id)
				print('Subenterprise ID:', str(route.subenterprise.id))
				updates.append({
					"id": ws.id,
					"subenterprise": route.subenterprise.id
				})
			else:
				print('No Route found for WorkSchedule:', ws.id)
		
		# Realiza atualizações em massa (bulk update) para otimizar o processo
		print('Step 8: Preparing updates...')
		for update in updates:
			print('Updating WorkSchedule ID:', update["id"], 'with Subenterprise ID:', update["subenterprise"])
			WorkSchedule.objects(id=update["id"]).update_one(set__subenterprise=update["subenterprise"])

		# Calcula o tempo total e imprime o resultado
		end_time = time.time()
		total_time = (end_time - start_time) / 60  # Converte para minutos
		
		print('============ Done ============')
		print(f'Total processing time: {total_time:.2f} minutes')
	except Exception as e:
		print(e)

normalize()
