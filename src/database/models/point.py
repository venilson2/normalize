from fmconsult.database.models.base import CustomBaseDocument
from mongoengine.fields import (
	ReferenceField,
	StringField,
	PointField
)

POINT_CATEGORIES = ('passenger','parking')

class Point(CustomBaseDocument):
	meta = {'collection': 'points'}

	# Collection fields
	category        = StringField(choices=POINT_CATEGORIES)
	description     = StringField()
	location        = PointField()
	enterprise      = ReferenceField('Enterprise')
 
	def to_json(self):
		data = {
			"id": str(self.id),
			"category": self.category,
			"description": self.description,
			"location": {
				"type": "Point",
				"coordinates": self['location']['coordinates'],
				"latitude": self['location']['coordinates'][0] if self['wrong_location'] == True else self['location']['coordinates'][1],
				"longitude": self['location']['coordinates'][1] if self['wrong_location'] == True else self['location']['coordinates'][0]
			} if self.location else None,
			"wrong_location": self['wrong_location'],
			"enterprise": str(self.enterprise.id) if self.enterprise else None
		}
		
		return data