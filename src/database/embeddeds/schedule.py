from src.database.models.vehicle import Vehicle
from mongoengine.fields import (
    StringField,
    EmbeddedDocument,
    ReferenceField
)

class Schedule(EmbeddedDocument):
	departure_time 	= StringField()
	vehicle         = ReferenceField(Vehicle)