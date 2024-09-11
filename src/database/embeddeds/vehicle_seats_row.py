from src.database.embeddeds.vehicle_seat import VehicleSeat

from mongoengine.fields import (
    EmbeddedDocument,
    EmbeddedDocumentListField
)

class VehicleSeatsRow(EmbeddedDocument):
	seats = EmbeddedDocumentListField(VehicleSeat)