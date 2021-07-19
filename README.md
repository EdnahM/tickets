## Tickets
Generating Tickets from a CSV File and generating a JSON file.

#### git clone https://github.com/EdnahM/tickets
- pip install -r  requirements.txt

- cd /data

Download the data and save as csv files per excel sheet. Messages.csv and Subjects.csv in the /data folder.

#### Change the URI for  mongo db connect to be same as your database credentials. in the /data/loader.py and  app.py

- connect(host="mongodb://admin:[Your Password]@127.0.0.1:27017/test?authSource=admin")

#### Load your database connection 
- python3 /data/loader.py

#### Run the application with the resources.
- python3 app.py

#### Test using postman eg a get request
- http://127.0.0.1:5001/tickets

## Hapy Coding!!










