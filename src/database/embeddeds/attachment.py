from datetime import datetime, timedelta

from mongoengine.fields import (
    EmbeddedDocument,
    DateTimeField,
    StringField
)

class Attachment(EmbeddedDocument):
	name 		= StringField()
	size 		= StringField()
	extension	= StringField()
	path 		= StringField()
	description = StringField()
	uploaded_at = DateTimeField(default=datetime.now)