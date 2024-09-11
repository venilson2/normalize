from fmconsult.database.models.base import CustomBaseDocument

from mongoengine.fields import (
    StringField,
    ReferenceField,
    BooleanField,
    EmbeddedDocumentListField
)

from src.database.models.subenterprise import SubEnterprise
from src.database.embeddeds.time_slot import TimeSlot
from src.database.embeddeds.way_point_route import WaypointRoute

DIRECTION_OPTIONS = ('incoming', 'outcoming', 'both', 'circular')

class WorkSchedule(CustomBaseDocument):
	meta = {'collection': 'work_schedule'}
	
	enterprise 			= ReferenceField('Enterprise')
	work_calendar 		= ReferenceField('WorkCalendar')
	vehicle 			= ReferenceField('Vehicle')
	driver 				= ReferenceField('User')
	line 				= ReferenceField('Line')
	route 				= ReferenceField('Route')
	waypoints 			= EmbeddedDocumentListField(WaypointRoute)
	subenterprise 		= ReferenceField(SubEnterprise)
	start_time 			= StringField()
	start_point 		= ReferenceField('Point')
	end_time 			= StringField()
	end_point 			= ReferenceField('Point')
	direction 			= StringField(choices=DIRECTION_OPTIONS)
	is_day_turn_line 	= BooleanField(default=False)
	time_slots			= EmbeddedDocumentListField(TimeSlot)