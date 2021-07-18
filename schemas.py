from marshmallow import Schema, fields


class Message(Schema):
    id = fields.Integer()
    message = fields.String()
    created = fields.DateTime()
    updated = fields.DateTime()
    user_id = fields.Integer(data_key='userId')


class Ticket(Schema):
    ticket_id = fields.Integer(data_key='ticketId')
    subject = fields.String()
    phone = fields.Integer()
    intents = fields.List(fields.String)
    incoming_messages = fields.List(fields.Nested(Message), data_key='incomingMessages')
    outgoing_messages = fields.List(fields.Nested(Message), data_key='outgoingMessages')
