from flask import Flask
from flask_restful import Api
from mongoengine import connect

from resources import Tickets, Ticket, IncomingMessage, IncomingMessages, OutgoingMessage, OutgoingMessages
connect(host="mongodb://admin:admin123@127.0.0.1:27017/test?authSource=admin")

app = Flask(__name__)
api = Api(app)

api.add_resource(Tickets, '/tickets')
api.add_resource(Ticket, '/ticket/<int:id>') 

api.add_resource(IncomingMessage, '/ticket/<int:ticket_id>/incoming-message/<int:message_id>')
api.add_resource(IncomingMessages, '/ticket/<int:ticket_id>/incoming-messages')

api.add_resource(OutgoingMessage, '/ticket/<int:ticket_id>/outgoing-message/<int:message_id>')
api.add_resource(OutgoingMessages, '/ticket/<int:ticket_id>/outgoing-messages')

if __name__ == '__main__':
    app.run(port=5001)
