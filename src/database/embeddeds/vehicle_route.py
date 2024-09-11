from src.database.embeddeds.activity_time import ActivityTime
from src.database.models.vehicle import Vehicle

from mongoengine.fields import (
    EmbeddedDocument,
    ReferenceField,
    EmbeddedDocumentListField
)

class VehicleRoute(EmbeddedDocument):
	vehicle 		= ReferenceField(Vehicle)
	activity_times 	= EmbeddedDocumentListField(ActivityTime)