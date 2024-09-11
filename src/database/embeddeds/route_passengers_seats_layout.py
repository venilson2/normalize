from src.database.embeddeds.vehicle_seats_row import VehicleSeatsRow
from bson import ObjectId
from src.database.embeddeds.way_point_route import WaypointRoute
from mongoengine.fields import (
    StringField,
    EmbeddedDocument,
    EmbeddedDocumentListField
)

class RoutePassengersSeatsLayout(EmbeddedDocument):
	oid = ObjectId()
	description = StringField()
	vehicle_type = StringField()
	positions = EmbeddedDocumentListField(VehicleSeatsRow)