import datetime

import mongoengine

from cocokat_com.nosql.comicpanel import ComicPanel


class Comic(mongoengine.Document):
    name = mongoengine.StringField()
    issue_number = mongoengine.IntField()
    created_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    panels = mongoengine.EmbeddedDocumentListField(ComicPanel)

    meta = {
        'db_alias': 'core',
        'collection': 'comics'}

    def __repr__(self):
        return f'Comic {self.name}, Issue {self.issue_number}'
