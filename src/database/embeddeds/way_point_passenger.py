from mongoengine.fields import (
 	DateTimeField, 
    StringField,
    EmbeddedDocument,
    ObjectIdField
)

PASSENGER_STATUS = ('pending', 'shipped', 'skipped')

class WaypointPassenger(EmbeddedDocument):
	passenger = ObjectIdField()
	status = StringField(choices=PASSENGER_STATUS, default='pending')
	comments = StringField()
	updated_at = DateTimeField()