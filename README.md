## Tickets
Generating Tickets from a CSV File and generating a JSON file.

#### git clone https://github.com/EdnahM/tickets
- pip install -r  requirements.txt

#### Change the URI for  mongo db connect to be same as your database credentials in the /data/loader.py and  app.py
This is if you have set the authorization and created a superuser for your mongo database.
- connect(host="mongodb://admin:[Your Password]@127.0.0.1:27017/test?authSource=admin") 

otherwise use
- connect('test')

#### Load your database connection 
- python3 /data/loader.py

#### Run the application with the resources.
- python3 app.py

#### Test using postman eg a get request
- http://127.0.0.1:5001/tickets

Also run

python3 test.py to do the test sample.

### Happy Coding!!










