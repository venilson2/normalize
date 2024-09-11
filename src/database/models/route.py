from src.database.embeddeds.time_slot import TimeSlot
from src.database.embeddeds.route_passengers_seats_layout import RoutePassengersSeatsLayout
from src.database.models.enterprise import Enterprise
from src.database.models.subenterprise import SubEnterprise
from src.database.models.user import User
from src.database.embeddeds.route_work_calendar import RouteWorkCalendar
from src.database.embeddeds.schedule import Schedule
from src.database.embeddeds.vehicle_route import VehicleRoute
from fmconsult.database.models.base import CustomBaseDocument
from mongoengine.fields import (
	BooleanField, 
    ReferenceField,
    StringField,
    EmbeddedDocumentListField,
    MultiPointField
)


DIRECTION_OPTIONS = ('incoming', 'outcoming', 'both', 'circular')

class Route(CustomBaseDocument):
	# Collection configuration
	meta = {'collection': 'routes'}

	# Collection fields
	hexcode 		= StringField()
	description 	= StringField()
	acronym         = StringField()
	color 			= StringField()
	direction 		= StringField(choices=DIRECTION_OPTIONS, default='both')
	vehicles 		= EmbeddedDocumentListField(VehicleRoute)
	schedule_grid 	= EmbeddedDocumentListField(Schedule)
	work_calendars 	= EmbeddedDocumentListField(RouteWorkCalendar)
	enterprise 		= ReferenceField(Enterprise)
	subenterprise 	= ReferenceField(SubEnterprise)
	seats_layouts 	= EmbeddedDocumentListField(RoutePassengersSeatsLayout)
	customized 		= BooleanField(default=False)
	customized_by 	= ReferenceField(User)
	time_slots		= EmbeddedDocumentListField(TimeSlot)
	path 			= MultiPointField()
	active 		    = BooleanField()
	wrong_location 	= BooleanField(default=False)
	inactive_at		= BooleanField()