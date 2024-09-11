from src.database.models.enterprise import Enterprise
from src.database.embeddeds.vehicle_seats_row import VehicleSeatsRow
from fmconsult.database.models.base import CustomBaseDocument
from mongoengine.fields import (
    ReferenceField,
    StringField,
    EmbeddedDocumentListField,
    BooleanField
)


class VehicleLayout(CustomBaseDocument):
	# Collection configuration
	meta = {'collection': 'vehicle_layouts'}
	
	# Collection fields
	description = StringField()
	positions = EmbeddedDocumentListField(VehicleSeatsRow)
	vehicle_type = StringField()
	enterprise = ReferenceField(Enterprise)
	wrong_location = BooleanField()