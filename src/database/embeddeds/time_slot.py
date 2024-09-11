from mongoengine.fields import (
    StringField,
    EmbeddedDocument,
    ObjectIdField,
)

class TimeSlot(EmbeddedDocument):
	description = StringField()
	start_time 	= StringField()
	end_time 	= StringField()
	driver		= ObjectIdField()
	vehicle		= ObjectIdField()