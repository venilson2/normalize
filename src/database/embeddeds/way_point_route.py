from src.database.embeddeds.way_point_passenger import WaypointPassenger
from mongoengine.fields import (
	BooleanField, 
 	DateTimeField, 
  	FloatField, 
   	IntField, 
    StringField,
    EmbeddedDocument,
    ObjectIdField,
    EmbeddedDocumentListField
)

WAYPOINT_STATUS = ('pending', 'partial', 'total', 'skipped')

class WaypointRoute(EmbeddedDocument):
    
	point 							= ObjectIdField()
	incoming_time 					= StringField()
	incoming_distance 				= FloatField()
	incoming_duration 				= FloatField()
	outcoming_time 					= StringField()
	outcoming_distance 				= FloatField()
	outcoming_duration 				= FloatField()
	passengers 						= EmbeddedDocumentListField(WaypointPassenger)
	status 							= StringField(choices=WAYPOINT_STATUS, default='pending')
	comments 						= StringField()
	scheduled_at					= DateTimeField()
	executed_at 					= DateTimeField()
	vehicle_tracker_passed			= BooleanField(default=False)
	vehicle_tracker_passed_time 	= IntField()
	vehicle_tracker_passed_distance = IntField()
 
	def to_json(waypoint):
		return {
			"point": str(waypoint.point),
			"incoming_time": waypoint.incoming_time,
			"incoming_distance": waypoint.incoming_distance,
			"incoming_duration": waypoint.incoming_duration,
			"outcoming_time": waypoint.outcoming_time,
			"outcoming_distance": waypoint.outcoming_distance,
			"outcoming_duration": waypoint.outcoming_duration,
			"passengers": [
				{
					"passenger": str(passenger.passenger),
					"status": passenger.status,
					"comments": passenger.comments,
					"updated_at": passenger.updated_at.isoformat() if passenger.updated_at else None
				}
				for passenger in waypoint.passengers
			],
			"status": waypoint.status,
			"comments": waypoint.comments,
			"scheduled_at": waypoint.scheduled_at.isoformat() if waypoint.scheduled_at else None,
			"executed_at": waypoint.executed_at.isoformat() if waypoint.executed_at else None,
			"vehicle_tracker_passed": waypoint.vehicle_tracker_passed,
			"vehicle_tracker_passed_time": waypoint.vehicle_tracker_passed_time,
			"vehicle_tracker_passed_distance": waypoint.vehicle_tracker_passed_distance
		}