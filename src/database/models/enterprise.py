from fmconsult.database.models.base import CustomBaseDocument
from mongoengine.fields import (
	BooleanField, 
   	IntField, 
    StringField,
)

ENTERPRISE_WORK_FORMATS = ('lines', 'routes')

class Enterprise(CustomBaseDocument):
	# Collection configuration
	meta = {'collection': 'enterprises'}

	# Collection fields
	name = StringField()
	use_access_control 	= BooleanField(default=False)
	use_app_mobile 		= BooleanField(default=False)
	use_app_driver 		= BooleanField(default=False)
	use_speed_control 	= BooleanField(default=False)
	work_format 		= StringField(choices=ENTERPRISE_WORK_FORMATS)
	getrak_id 			= IntField()
	wrong_location 		= BooleanField(default=False)
	active 				= BooleanField(default=True)