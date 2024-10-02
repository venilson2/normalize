from mongoengine.fields import (
    StringField,
    EmbeddedDocument,
    PointField,
    ReferenceField
)

class ParkingAddress(EmbeddedDocument):
    formatted_address   = StringField()
    street              = StringField()
    district            = StringField()
    city                = StringField()
    state               = StringField()
    zip_code            = StringField()
    number              = StringField()
    location            = PointField()
    point               = ReferenceField('Point')