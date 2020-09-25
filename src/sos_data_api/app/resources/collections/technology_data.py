from mongoengine import Document, StringField, ListField


class TechnologyData(Document):
    name = StringField()
    tags = ListField()
