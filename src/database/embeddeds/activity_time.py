from mongoengine.fields import (
    EmbeddedDocument,
    StringField
)

class ActivityTime(EmbeddedDocument):
	start_time  = StringField()
	end_time    = StringField()