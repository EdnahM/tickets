from mongoengine import Document, EmbeddedDocument, IntField, StringField, ListField, EmbeddedDocumentListField, \
    DateTimeField


class Message(EmbeddedDocument):
    id = IntField(primary_key=True)
    message = StringField()
    created = DateTimeField()
    updated = DateTimeField()
    user_id = IntField()


class Ticket(Document):
    ticket_id = IntField(primary_key=True)
    subject = StringField()
    phone = IntField()
    intents = ListField(StringField(max_length=240))
    incoming_messages = EmbeddedDocumentListField('Message')
    outgoing_messages = EmbeddedDocumentListField('Message')

    meta = {
        'collection': 'tickets'
    }


