from fmconsult.database.models.base import CustomBaseDocument

from mongoengine.fields import (
    StringField,
    ReferenceField,
    BooleanField
)

class WorkCalendar(CustomBaseDocument):
    meta = {'collection': 'work_calendar'}

    enterprise 	    = ReferenceField('Enterprise')
    name 		    = StringField()
    description     = StringField()
    active 		    = BooleanField()
    wrong_location 	= BooleanField(default=False)