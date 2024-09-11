from src.database.models.enterprise import Enterprise
from src.database.models.subenterprise import SubEnterprise
from src.database.models.line_route import LineRoute
from fmconsult.database.models.base import CustomBaseDocument
from mongoengine.fields import (
    StringField,
    ReferenceField,
    EmbeddedDocumentListField
)

class Line(CustomBaseDocument):
	# Collection configuration
	meta = {'collection': 'lines'}

	# Collection fields
	description = StringField()
	enterprise = ReferenceField(Enterprise)
	subenterprise = ReferenceField(SubEnterprise)
	routes = EmbeddedDocumentListField(LineRoute)