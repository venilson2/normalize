from datetime import datetime

from mongoengine.fields import (
    EmbeddedDocument,
    DateTimeField,
    StringField,
    BooleanField
)

COURSES = ('orders', 'repair_request', 'fuel_supply_record', 'checklist_vehicle', 'checklist_sanitary')

class Course(EmbeddedDocument):
	name = StringField(choices=COURSES)
	is_done = BooleanField(default=False)
	completed_at = DateTimeField(default=datetime.now)