from fmconsult.database.models.base import CustomBaseDocument
from mongoengine.fields import (
	BooleanField, 
 	DateTimeField, 
  	FloatField, 
   	IntField, 
    ReferenceField,
    StringField,
    PointField,
    ObjectIdField,
    ListField
)

from src.database.models.enterprise import Enterprise
from src.database.models.vehicle_kayout import VehicleLayout

GPS_UPDATE_FONTS = ('vehicle-tracker', 'driver-app', 'passenger-app')


class Vehicle(CustomBaseDocument):
	meta = {'collection': 'vehicles'}

	plate                           = StringField()
	description                     = StringField()
	line                            = ReferenceField('Line')
	route                           = ObjectIdField()
	active_order                    = ObjectIdField()
	icon                            = StringField()
	getrak_id                       = IntField()
	getrak_ids                      = ListField()
	is_online                       = BooleanField(default=False)
	speed                           = IntField()
	location                        = PointField()
	enterprise                      = ReferenceField(Enterprise)
	gps_updated_at                  = DateTimeField()
	gps_update_font                 = StringField(default ='vehicle-tracker', choices=GPS_UPDATE_FONTS)
	fuel_tank_size                  = FloatField()
	odometer_value                  = FloatField()
	odometer_value_last_fuel_supply = FloatField()
	autonomy_average                = FloatField()
	fuel_avaliable_stock            = FloatField()
	fuel_stocked_at                 = DateTimeField()
	seats_layout                    = ReferenceField(VehicleLayout)
	purchased_at                    = DateTimeField()
	sold_at                         = DateTimeField()
	vehicle_rfid                    = ObjectIdField()
	vehicle_jammer                  = ObjectIdField()
	wrong_location					= StringField()
	alert_days_expiration_artesp 	= IntField(default=10)
	alert_days_expiration_mip 		= IntField(default=10)
	alert_days_expiration_dtp  		= IntField(default=10)
	alert_days_expiration_emtu 		= IntField(default=10)
	expiration_artesp_at			= DateTimeField()
	expiration_mip_at				= DateTimeField()
	expiration_dtp_at				= DateTimeField()
	expiration_emtu_at				= DateTimeField()
	active							= BooleanField()
	inactive_at						= DateTimeField()