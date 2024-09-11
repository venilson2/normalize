from mongoengine.fields import (
    StringField,
    ReferenceField,
    EmbeddedDocument
)

DIRECTION_OPTIONS = ('incoming', 'outcoming', 'both', 'circular')

class LineRoute(EmbeddedDocument):
	route = ReferenceField('Route')
	direction = StringField(choices=DIRECTION_OPTIONS)