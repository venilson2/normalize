from src.database.embeddeds.parking_address import ParkingAddress
from src.database.embeddeds.course import Course
from src.database.embeddeds.attachment import Attachment
from src.database.embeddeds.trip_performed import TripPerformed
from src.database.embeddeds.time_slot import TimeSlot
from src.database.embeddeds.way_point_route import WaypointRoute

from fmconsult.database.models.base import CustomBaseDocument
from mongoengine.fields import (
	BooleanField, 
 	DateTimeField, 
   	IntField, 
    ReferenceField,
    StringField,
    EmbeddedDocumentListField,
    EmbeddedDocumentField,
    ListField,
    DynamicField
)

USER_PROFILES = ('master', 'admin', 'traffic-control', 'driver', 'engineer', 'customer', 'passenger')

class User(CustomBaseDocument):
	# Collection configuration
	meta = {'collection': 'users'}

	# Collection fields
	name 					= StringField(required=True)
	full_name 				= StringField()
	login 					= StringField(required=True)
	password 				= DynamicField()
	profile 				= StringField(required=True, choices=USER_PROFILES)
	enterprise 				= ReferenceField('Enterprise')
	subenterprise 			= ReferenceField('SubEnterprise')
	subenterprises 			= ListField(ReferenceField('SubEnterprise'))
	cpf 					= StringField()
	enrollment 				= StringField()
	address 				= StringField()
	personal_phone_number 	= StringField()
	company_phone_number 	= StringField()
	cnh_number 				= StringField()
	cnh_due_date 			= DateTimeField()
	cnh_front_path 			= StringField()
	cnh_back_path 			= StringField()
	change_password 		= BooleanField(default=True)
	avatar_path 			= StringField()
	last_vehicle_driven 	= ReferenceField('Vehicle')
	courses 				= EmbeddedDocumentListField(Course)
	verified 				= BooleanField(default=False)
	passenger 				= ReferenceField('Passenger')
	validation_code 		= IntField()
	admission_at 			= DateTimeField()
	resignation_at 			= DateTimeField()
	app_last_login_version 	= StringField()
	vacation_start 			= DateTimeField()
	vacation_end 			= DateTimeField()
	parking_address 		= EmbeddedDocumentField(ParkingAddress)
	active 					= BooleanField()
	wrong_location 			= BooleanField(default=False)
	inactive_at 			= DateTimeField()
 
 
	def to_json(user):
		return {
			'id': str(user.id),
			'name': user.name,
			'profile': user.profile,
			'avatar_path': user.avatar_path,
			'last_vehicle_driven': str(user.last_vehicle_driven),
			'courses': user.courses,
			'active': user.active,
			'wrong_location': user.wrong_location,
			'admission_at': user.admission_at,
			'resignation_at': user.resignation_at,
			'vacation_start': user.vacation_start,
			'vacation_end': user.vacation_end,
			'passenger': str(user.passenger),
			'validation_code': user.validation_code,
			'change_password': user.change_password,
		}