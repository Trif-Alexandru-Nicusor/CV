from nicegui import ui
from Functions import universalFunctions
from dotenv import load_dotenv
import os , hashlib
load_dotenv(dotenv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)) , '.env'))
def hash_password(password):
    hashed_password = hashlib.sha512(password.encode()).hexdigest()
    return hashed_password
def login(user , password):
    password = hash_password(password)
    if universalFunctions.dataBaseQuerys(f"SELECT * FROM {os.environ.get('database')} WHERE {os.environ.get('userUser')} = '{user}' AND Password = '{password}'") == True:
        universalFunctions.goToPage(page = 'homeLogged')
    elif universalFunctions.dataBaseQuerys(f"SELECT * FROM {os.environ.get('database')} WHERE {os.environ.get('userUser')} = '{user}' AND Password = '{password}'") == False:
        ui.notify(message = 'User or password are incorect .' , position = 'center')
    elif universalFunctions.dataBaseQuerys(f"SELECT Password FROM {os.environ.get('database')} WHERE User = '{user}'") == 'Error':
        ui.notify(message = 'Database problem .' , position = 'center')
