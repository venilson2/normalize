from src.database.models.work_calendar import WorkCalendar
from src.database.embeddeds.way_point_route import WaypointRoute
from mongoengine.fields import (
    StringField,
    EmbeddedDocument,
    ReferenceField,
    IntField,
    EmbeddedDocumentListField
)


class RouteWorkCalendar(EmbeddedDocument):
	work_calendar 					= ReferenceField(WorkCalendar)
	work_shift                      = StringField()
	arrival_time_incoming           = StringField()
	arrival_time_outcoming          = StringField()
	additional_time_type            = StringField()
	additional_time_type_waypoints  = IntField()
	waypoints                       = EmbeddedDocumentListField(WaypointRoute)