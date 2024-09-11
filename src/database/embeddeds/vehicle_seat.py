from mongoengine.fields import (
    EmbeddedDocument,
    StringField,
    BooleanField,
    ObjectIdField
)

class VehicleSeat(EmbeddedDocument):
	name        = StringField()
	is_hall     = BooleanField(default=False)
	is_void     = BooleanField(default=False)
	is_driver   = BooleanField(default=False)
	passenger   = ObjectIdField()