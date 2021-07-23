## Tickets Generation
Generating Tickets from a CSV File and generating a JSON file.

### git clone https://github.com/EdnahM/tickets

Make sure you are in the tickets working directory
cd into the tickets directory.
- cd tickets/

### Create a new python virtual environment or anaconda environment:
*Python venv*
- pip install virtualenv
- virtualenv [yourvirtualenv name]

*Anaconda virtual environment*
- conda create -n yourenvname python=x.x anaconda

### Activate your virtual Environment:
*python venv  Mac OS/linux*
- source [yourvirtualenv]/bin/activate 

*Python venv windows*
- [yourvirtualenv]\Scripts\activate

*Anaconda virtual environment*
-conda activate [yourvirtualEnv]

### Install the requirements:

- pip install -r  requirements.txt

### Change the URI for  mongo db connect to be same as your database credentials in the /data/ loader.py and  app.py

This is if you have set the authorization and created a superuser for your mongo database.

- connect(host="mongodb://admin:[Your Password]@127.0.0.1:27017/test?authSource=admin") 

otherwise use
- connect('test')

#### Load your database connection 
- python3 /data/loader.py

#### Run the application 
- python3 app.py

#### Test using postman eg a get request
- http://127.0.0.1:5001/tickets


Or Run for testing get requests
python3 test.py 

### Happy Coding!!










