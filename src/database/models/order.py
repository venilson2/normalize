from src.database.models.enterprise import Enterprise
from src.database.models.route import Route
from src.database.embeddeds.attachment import Attachment
from src.database.models.user import User
from src.database.models.vehicle import Vehicle
from src.database.embeddeds.trip_performed import TripPerformed
from src.database.embeddeds.time_slot import TimeSlot
from src.database.embeddeds.way_point_route import WaypointRoute
from bson import ObjectId
from fmconsult.database.models.base import CustomBaseDocument
from mongoengine.fields import (
	BooleanField, 
 	DateTimeField, 
    EmbeddedDocumentListField,
    EmbeddedDocumentField,
   	IntField, 
    ListField,
    ObjectIdField,
    ObjectIdField,
    PointField,
    StringField,
    ReferenceField
)

DIRECTION_OPTIONS = ('incoming', 'outcoming', 'both', 'circular')

class Order(CustomBaseDocument):
	meta = {'collection': 'order'}

	enterprise 							= ReferenceField(Enterprise)
	work_schedule 						= ObjectIdField()
	work_calendar 						= ObjectIdField()
	vehicle 							= ReferenceField(Vehicle)
	driver 								= ReferenceField(User)
	line 								= ObjectIdField()
	route 								= ReferenceField(Route)
	waypoints 							= EmbeddedDocumentListField(WaypointRoute)
	direction 							= StringField(choices=DIRECTION_OPTIONS)
	scheduled_at 						= DateTimeField()
	
	# Order Confirmation Data
	confirmed 							= BooleanField(default=False)
	confirmed_at 						= DateTimeField()
	confirmed_by 						= ReferenceField('User')
	confirm_annotations 				= StringField()

	# Order Accept Data
	accepted 							= BooleanField(default=False)
	accepted_at 						= DateTimeField()
	accept_location 					= PointField()
	
	# Order Departure Place Data (Outcoming Orders)
	arrived_departure_place 			= BooleanField()
	arrived_departure_place_at 			= DateTimeField()
	departure_place_location 			= PointField()

	# Order Start Improdutive Time Data
	start_time 							= StringField()
	start_at 							= DateTimeField()
	start_point 						= ObjectIdField()
	started_improdutive_time 			= BooleanField(default=False)
	started_improdutive_time_at 		= DateTimeField()
	started_odometer_value 				= IntField()
	start_location 						= PointField()
	start_vehicle_location 				= PointField()
	
	# Order Start Travel Data
	start_travel_scheduled_at 			= DateTimeField()
	started_travel 						= BooleanField(default=False)
	started_travel_at 					= DateTimeField()
	start_travel_location 				= PointField()
	
	# Order Completed Travel Data
	completed 							= BooleanField(default=False)
	completed_at 						= DateTimeField()
	completed_odometer_value 			= IntField()
	complete_location 					= PointField()
	completed_vehicle_location 			= PointField()
	complete_scheduled_at 				= DateTimeField()
	
	# Order Delivery Data
	end_time 							= StringField()
	end_at 								= DateTimeField()
	end_point 							= ObjectIdField()
	delivered 							= BooleanField(default=False)
	delivered_at 						= DateTimeField()
	delivered_odometer_value 			= IntField()
	delivery_location 					= PointField()
	delivered_after_time 				= BooleanField(default=False)
	justification_text 					= StringField()
	finished_automatically 				= BooleanField(default=False)
 
	attachments 						= EmbeddedDocumentListField(Attachment)
	
	checklist_initial 					= ObjectIdField()
	checklist_sanitary 					= ObjectIdField()

	customized 							= BooleanField(default=False)
	customized_by 						= ObjectIdField()

	# Support Vehicle
	support_vehicle 					= ObjectIdField()
	support_driver 						= ObjectIdField()
	support_start_point 				= ObjectIdField()
	
	# Order Late Finish
	delivered_after_time_unfounded 		= BooleanField(default=False)
	delivered_after_time_verified 		= BooleanField(default=False)
	delivered_after_time_verified_at 	= DateTimeField()
	delivered_after_time_user_update 	= ObjectIdField()
	is_valid 							= BooleanField(default=False)
 
	time_slot 							= EmbeddedDocumentField(TimeSlot)
	trips_performed						= EmbeddedDocumentListField(TripPerformed)
	
	# Order Delay
	is_delayed_vehicle 					= BooleanField(default=False) 
	delayed_at 							= DateTimeField()
	delayed_vehicle_time 				= IntField() # Seconds
	delayed_vehicle_distance			= IntField() # Meters
	chat_room_id						= ObjectIdField()
	count_requests                      = IntField(default=0)
	edited_history                      = ListField()
 
	wrong_location 						= BooleanField()
 
	active								= BooleanField()
 
	def to_json(order):
     
		def serialize_waypoint(waypoint):
			return WaypointRoute.to_json(waypoint)
     
		data =  {
			"id": str(order.id),
			"enterprise": {
				"id": str(order.enterprise.id),
				"name": str(order.enterprise.name)
         	} if order.enterprise else None,
			"work_schedule": str(order.work_schedule),
			"work_calendar": str(order.work_calendar),
			"vehicle": {
				"id": str(order.vehicle.id),
				"getrak_id": order.vehicle.getrak_id,
				"plate": order.vehicle.plate,
				"description": order.vehicle.description,
				"seats_layout": {
					"id": str(order.vehicle.seats_layout.id),
					"description": order.vehicle.seats_layout.description
				} if order.vehicle.seats_layout else None
			} if order.vehicle else None,
			"driver": {
				"id": str(order.driver.id),
				"name": order.driver.name
         	} if order.driver else None,
			"line": str(order.line),
			"route": {
				"id": str(order.route.id),
				"description": order.route.description,
				"color": order.route.color,
				"subenterprise": {
					"id": str(order.route.subenterprise.id),
					"name": order.route.subenterprise.name				
     			}
    		}  if order.route else None,
			"waypoints": [serialize_waypoint(wp) for wp in order.waypoints],
			"direction": order.direction,
			"scheduled_at": order.scheduled_at.isoformat() if order.scheduled_at else None,
			"confirmed": order.confirmed,
			"confirmed_at": order.confirmed_at.isoformat() if order.confirmed_at else None,
			"confirmed_by": str(order.confirmed_by.id) if order.confirmed_by else None,
			"confirm_annotations": order.confirm_annotations,
			"accepted": order.accepted,
			"accepted_at": order.accepted_at.isoformat() if order.accepted_at else None,
			"accept_location": {
				"type": "Point",
				"coordinates": order['accept_location']['coordinates']
			} if order.accept_location else None,
			"arrived_departure_place": order.arrived_departure_place,
			"arrived_departure_place_at": order.arrived_departure_place_at.isoformat() if order.arrived_departure_place_at else None,
			"departure_place_location": {
				"type": "Point",
				"coordinates": order['departure_place_location']['coordinates']
         	} if order.departure_place_location else None,
			"start_time": order.start_time,
			"start_at": order.start_at.isoformat() if order.start_at else None,
			"start_point": str(order.start_point),
			"started_improdutive_time": order.started_improdutive_time,
			"started_improdutive_time_at": order.started_improdutive_time_at.isoformat() if order.started_improdutive_time_at else None,
			"started_odometer_value": order.started_odometer_value,
			"start_location": {
				"type": "Point",
				"coordinates": order['start_location']['coordinates']	
			} if order.start_location else None,
			"start_vehicle_location": {
				"type": "Point",
				"coordinates": order['start_vehicle_location']['coordinates']	
			} if order.start_vehicle_location else None,
			"start_travel_scheduled_at": order.start_travel_scheduled_at.isoformat() if order.start_travel_scheduled_at else None,
			"started_travel": order.started_travel,
			"started_travel_at": order.started_travel_at.isoformat() if order.started_travel_at else None,
			"start_travel_location": {
				"type": "Point",
				"coordinates": order['accept_location']['coordinates']
    		} if order.accept_location else None,
			"completed": order.completed,
			"completed_at": order.completed_at.isoformat() if order.completed_at else None,
			"completed_odometer_value": order.completed_odometer_value,
			"complete_location": order.complete_location.to_mongo().to_dict() if order.complete_location else None,
			"completed_vehicle_location": order.completed_vehicle_location.to_mongo().to_dict() if order.completed_vehicle_location else None,
			"complete_scheduled_at": order.complete_scheduled_at.isoformat() if order.complete_scheduled_at else None,
			"end_time": order.end_time,
			"end_at": order.end_at.isoformat() if order.end_at else None,
			"end_point": str(order.end_point),
			"delivered": order.delivered,
			"delivered_at": order.delivered_at.isoformat() if order.delivered_at else None,
			"delivered_odometer_value": order.delivered_odometer_value,
			"delivery_location": {
				"type": "Point",
				"coordinates": order['delivery_location']['coordinates']
    		} if order.delivery_location else None,
			"delivered_after_time": order.delivered_after_time,
			"justification_text": order.justification_text,
			"finished_automatically": order.finished_automatically,
			"attachments": [att.to_mongo().to_dict() for att in order.attachments],
			"checklist_initial": str(order.checklist_initial),
			"checklist_sanitary": str(order.checklist_sanitary),
			"customized": order.customized,
			"customized_by": str(order.customized_by),
			"support_vehicle": str(order.support_vehicle),
			"support_driver": str(order.support_driver),
			"support_start_point": str(order.support_start_point),
			"delivered_after_time_unfounded": order.delivered_after_time_unfounded,
			"delivered_after_time_verified": order.delivered_after_time_verified,
			"delivered_after_time_verified_at": order.delivered_after_time_verified_at.isoformat() if order.delivered_after_time_verified_at else None,
			"delivered_after_time_user_update": str(order.delivered_after_time_user_update),
			"is_valid": order.is_valid,
			"time_slot": order.time_slot.to_mongo().to_dict() if order.time_slot else None,
			"trips_performed": [trip.to_mongo().to_dict() for trip in order.trips_performed],
			"is_delayed_vehicle": order.is_delayed_vehicle,
			"delayed_at": order.delayed_at.isoformat() if order.delayed_at else None,
			"delayed_vehicle_time": order.delayed_vehicle_time,
			"delayed_vehicle_distance": order.delayed_vehicle_distance,
			"chat_room_id": str(order.chat_room_id),
			"count_requests": order.count_requests,
			"edited_history": order.edited_history,
			"wrong_location": order.wrong_location,
			"active": order.active,
		}
  
		return data
  
  
  
