
from flask_restful import Resource
from mongoengine import DoesNotExist
from werkzeug.exceptions import NotFound

from models import Ticket as TicketModel
from schemas import Ticket as TicketSchema, Message as MessageSchema


class Ticket(Resource):
    schema = TicketSchema()

    def get(self, id):
        """Get ticket with ID"""
        try:
            return self.schema.dump(TicketModel.objects.get(ticket_id=id))
        except DoesNotExist:
            raise NotFound(f'Ticket with id:{id} was not found.')

    def delete(self, id):
        """Delete ticket"""
        try:
            TicketModel.objects.get(ticket_id=id).delete()
            return {
                'message': 'Ticket successfully deleted.'
            }
        except DoesNotExist:
            raise NotFound(f'Ticket with id:{id} was not found.')

    def patch(self, id):
        """Update ticket"""
        pass


class Tickets(Resource):
    schema = TicketSchema()

    def get(self):
        """Get all tickets"""
        # TODO: Implement offset and limit for batch tickets GET
        return self.schema.dump(TicketModel.objects, many=True)

    def post(self):
        """Add a new ticket"""
        pass

    def delete(self):
        """Delete all tickets"""
        ticket = self.schema.get(TicketModel.objects, many=True).delete()      
        #ticket = TicketModel.objects.get(self).delete()
        ticket.save()


class IncomingMessage(Resource):
    schema = MessageSchema()

    def get(self, ticket_id, message_id):
        """Get incoming message"""
        ticket = TicketModel.objects.get(ticket_id=ticket_id)
        try:
            return self.schema.dump(next(message for message in ticket.incoming_messages if message.id == message_id))
        except DoesNotExist:
            raise NotFound(f'Ticket with id:{ticket_id} was not found.')
        except StopIteration:
            raise NotFound(f'Incoming message with id: {message_id} was not found')

    def delete(self, ticket_id, message_id):
        """Delete incoming message"""
        try:
            ticket = TicketModel.objects.get(ticket_id=ticket_id)
            message = next(message for message in ticket.incoming_messages if message.id == message_id)
            ticket.incoming_messages.remove(message)
            ticket.save()

            return 'incoming message deleted'
        except DoesNotExist:
            raise NotFound(f'Ticket with id:{ticket_id} was not found.')
        except StopIteration:
            raise NotFound(f'Incoming message with id: {message_id} was not found')

    def put(self, ticket_id, message_id):
        """Replace incoming message"""
        pass

    def patch(self, ticket_id, message_id):
        """Update incoming message"""
        pass


class IncomingMessages(Resource):
    schema = MessageSchema()

    def get(self, ticket_id):
        """Get all incoming messages"""
        try:
            return self.schema.dump(TicketModel.objects.get(ticket_id=ticket_id).incoming_messages, many=True)
        except DoesNotExist:
            raise NotFound(f'Ticket with id:{ticket_id} was not found.')

    def delete(self, ticket_id):
        """Delete all incoming messages"""
        # ticket = (TicketModel.objects.get(ticket_id=ticket_id).incoming_messeges)
        try:
            ticket = TicketModel.objects.get(ticket_id=ticket_id)
            del ticket.incoming_messages
            ticket.save()
            
            return "All incoming messaged deleted"
        except DoesNotExist:
            raise NotFound(f'Ticket with id:{ticket_id} was not found.')

    def post(self, ticket_id):
        """Add an incoming message"""
        pass


class OutgoingMessage(Resource):
    schema = MessageSchema()

    def get(self, ticket_id, message_id):
        """Get outgoing message"""
        ticket = TicketModel.objects.get(ticket_id=ticket_id)
        try:
            return self.schema.dump(next(message for message in ticket.outgoing_messages if message.id == message_id))
        except DoesNotExist:
            raise NotFound(f'Ticket with id:{ticket_id} was not found.')
        except StopIteration:
            raise NotFound(f'Outgoing message with id: {message_id} was not found')

    def put(self, ticket_id, message_id):
        """Replace outgoing message"""
        pass

    def patch(self, ticket_id, message_id):
        """Update outgoing message"""
        pass

    def delete(self, ticket_id, message_id):
        """Delete outgoing message"""
        pass


class OutgoingMessages(Resource):
    schema = MessageSchema()

    def get(self, ticket_id):
        """Get all outgoing messages"""
        try:
            return self.schema.dump(TicketModel.objects.get(ticket_id=ticket_id).outgoing_messages, many=True)
        except DoesNotExist:
            raise NotFound(f'Ticket with id:{ticket_id} was not found.')

    def post(self, ticket_id):
        """Add and outgoing message"""
        pass

    def delete(self, ticket_id):
        """Delete all outgoing messages"""
