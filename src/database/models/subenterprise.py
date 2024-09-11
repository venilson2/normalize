from fmconsult.database.models.base import CustomBaseDocument
from mongoengine.fields import (
	BooleanField, 
    ReferenceField,
    StringField,
    DateTimeField
)

from src.database.models.enterprise import Enterprise

CREDENTIAL_CARD_TYPE = ('aba-track','serial','wiegand','decimal')

class SubEnterprise(CustomBaseDocument):
	# Collection configuration
	meta = {'collection': 'subenterprises'}

	# Collection fields
	name 					= StringField()
	hexcode 				= StringField()
	acronym 				= StringField()
	enterprise 				= ReferenceField(Enterprise)
	use_temperature_control = BooleanField(default=False)
	credential_card_type 	= StringField(choices=CREDENTIAL_CARD_TYPE)
	inactive_at 			= DateTimeField()