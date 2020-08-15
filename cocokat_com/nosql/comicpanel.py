import datetime

import mongoengine


class ComicPanel(mongoengine.EmbeddedDocument):
    img_src = mongoengine.StringField()
    alt_text = mongoengine.StringField()
    add_date = mongoengine.DateTimeField(default=datetime.datetime.now)

    meta = {
        'db_alias': 'core',
        'collection': 'comics'}
