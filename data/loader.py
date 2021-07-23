"""
loader.py
Loads data from CSV files into a database
"""

import csv
from datetime import datetime
from mongoengine import Document, EmbeddedDocument, StringField, IntField, DateTimeField, ListField, EmbeddedDocumentListField

from mongoengine import connect

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

connect(host="mongodb://admin:yourpassword@127.0.0.1:27017/test?authSource=admin")

tickets = {}


def generate_subject(raw_subject):
    if raw_subject.startswith('['):
        phone = raw_subject[4:14]
        subject = raw_subject[16:]
        return phone, subject
    else:
        return None, raw_subject.strip()


with open('./data/Subjects.csv') as subjects:
    reader = csv.DictReader(subjects)
    for row in reader:
        id = row['ticket_id']
        phone, subject = generate_subject(row['subject'])
        tickets[row["ticket_id"]] = Ticket(ticket_id=id, phone=phone, subject=subject)

with open('./data/Messages.csv') as messages:
    reader = csv.DictReader(messages)
    for row in reader:
        if row['body_text'].startswith('Detected intent:'):
            text = row['body_text'].split(') ')[1]
            intent = row['body_text'][16:].split(' (')[0]
            tickets[row['ticket_id']].intents.append(intent)
            message = Message(id=row['id'], message=text, user_id=int(row['user_id']),
                              created=datetime.strptime(row['created_at'], '%Y-%m-%d %H:%M:%S'),
                              updated=datetime.strptime(row['created_at'], '%Y-%m-%d %H:%M:%S'))
            if row['incoming'] == 'TRUE':
                tickets[row["ticket_id"]].incoming_messages.append(message)
            else:
                tickets[row['ticket_id']].outgoing_messages.append(message)
        else:
            message = Message(id=row['id'], message=row['body_text'], user_id=int(row['user_id']),
                              created=datetime.strptime(row['created_at'], '%Y-%m-%d %H:%M:%S'),
                              updated=datetime.strptime(row['created_at'], '%Y-%m-%d %H:%M:%S'))
            if row['incoming'] == 'TRUE':
                tickets[row["ticket_id"]].incoming_messages.append(message)
            else:
                tickets[row['ticket_id']].outgoing_messages.append(message)

for ticket_id, ticket in tickets.items():
    ticket.save()
