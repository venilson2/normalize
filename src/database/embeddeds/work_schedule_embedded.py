from src.database.embeddeds.way_point_route import WAYPOINT_STATUS
from src.database.embeddeds.schedule import Schedule
from src.database.embeddeds.way_point_passenger import WaypointPassenger
from mongoengine.fields import (
	BooleanField, 
 	DateTimeField, 
  	FloatField, 
   	IntField, 
    StringField,
    EmbeddedDocument,
    EmbeddedDocumentListField,
    ObjectIdField,
    ListField,
    DictField,
    EmbeddedDocumentField,
    MultiPointField
    
)

class EnterpriseEmbedded(EmbeddedDocument):
	id = ObjectIdField()
	name = StringField()

class WorkScheduleEmbedded(EmbeddedDocument):
	id = ObjectIdField()
	is_day_turn_line = BooleanField()

class WorkCalendarEmbedded(EmbeddedDocument):
	id = ObjectIdField()
	name = StringField()
	work_shift = StringField()
 
class SeatsLayoutEmbedded(EmbeddedDocument):
	id = ObjectIdField()
	description = StringField()

class VehicleEmbedded(EmbeddedDocument):
	id = ObjectIdField()
	getrak_id = IntField()
	getrak_ids = ListField(IntField())
	plate = StringField()
	description = StringField()
	seats_layout = EmbeddedDocumentField(SeatsLayoutEmbedded)
	icon = StringField()
	is_online = BooleanField(default=False)
	speed = FloatField()
	location = DictField()
	updated_at = DateTimeField()

class SubEnterpriseEmbedded(EmbeddedDocument):
	id = ObjectIdField()
	name = StringField()
	hexcode = StringField()
	active = BooleanField()
	created_at = DateTimeField()

class RouteEmbedded(EmbeddedDocument):
	id = ObjectIdField()
	hexcode = StringField()
	description = StringField()
	acronym = StringField()
	subenterprise = EmbeddedDocumentField(SubEnterpriseEmbedded)
	color = StringField()
	direction = StringField()
	customized = BooleanField()
	customized_by = StringField()
	schedule_grid 	= EmbeddedDocumentListField(Schedule)
	path 			= MultiPointField()
	work_calendars = ListField(EmbeddedDocumentField(WorkCalendarEmbedded))

class DriverEmbedded(EmbeddedDocument):
	id = ObjectIdField()
	name = StringField()

class PointEmbedded(EmbeddedDocument):
	id = ObjectIdField()
	description = StringField()
	location = DictField()
	wrong_location = BooleanField()
	
class PassengerEmbedded(EmbeddedDocument):
	name = StringField()
	
class WaypointRouteEmbedded(EmbeddedDocument):
	point = EmbeddedDocumentField(PointEmbedded)
	
	incoming_time = StringField()
	incoming_distance = FloatField()
	incoming_duration = FloatField()

	outcoming_time = StringField()
	outcoming_distance = FloatField()
	outcoming_duration = FloatField()
	
	passengers = EmbeddedDocumentListField(WaypointPassenger)
	status = StringField(choices=WAYPOINT_STATUS, default='pending')
	comments = StringField()
	scheduled_at = DateTimeField()
	executed_at = DateTimeField()
	vehicle_tracker_passed = BooleanField(default=False)
	vehicle_tracker_passed_time = IntField() # Seconds
	vehicle_tracker_passed_distance = IntField() # Meters

class TimeSlotEmbedded(EmbeddedDocument):
	description = StringField()
	start_time 	= StringField()
	end_time 	= StringField()
	driver		= EmbeddedDocumentField(DriverEmbedded)
	vehicle		= EmbeddedDocumentField(VehicleEmbedded)
 
class UserEmbedded(EmbeddedDocument):
	id = ObjectIdField()
	name = StringField()
 
class WorkScheduleEmbedded(EmbeddedDocument):

	enterprise 		= EmbeddedDocumentField(EnterpriseEmbedded)
	work_calendar 	= EmbeddedDocumentField(WorkCalendarEmbedded)
	vehicle 		= EmbeddedDocumentField(VehicleEmbedded)
	driver 			= EmbeddedDocumentField(DriverEmbedded)
	route 			= EmbeddedDocumentField(RouteEmbedded)
	subenterprise 	= EmbeddedDocumentField(SubEnterpriseEmbedded)
	start_point 	= EmbeddedDocumentField(PointEmbedded)
	end_point 		= EmbeddedDocumentField(PointEmbedded)
	waypoints 		= EmbeddedDocumentListField(WaypointRouteEmbedded)