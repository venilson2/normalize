from datetime import datetime, timedelta

from mongoengine.fields import (
    EmbeddedDocument,
    ObjectIdField,
    DateTimeField,
    ListField
)

class TripPerformed(EmbeddedDocument):
	boarding_point 		= ObjectIdField('Point')
	passengers_boarded 	= ListField()
	executed_at 		= DateTimeField(default=datetime.now)