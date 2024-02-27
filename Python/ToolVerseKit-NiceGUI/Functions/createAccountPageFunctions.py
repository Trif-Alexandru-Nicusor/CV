import main , os
from Functions import universalFunctions
from nicegui import ui
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
load_dotenv(dotenv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)) , '.env'))

def addAccount(user , email , password):
    if user.value == '' or email.value == '' or password.value == '':
        ui.notify(message = 'You need to complete all lines .')
    else:
        if universalFunctions.dataBaseQuerys(f"SELECT * FROM {os.environ.get('database')} WHERE {os.environ.get('userUser')} = '{user.value}'") == True:
            ui.notify(message = 'User already exists .' , position = 'center')
        else:
            if universalFunctions.dataBaseQuerys(f"INSERT INTO {os.environ.get('database')} ({os.environ.get('userUser')}, {os.environ.get('userEmail')}, {os.environ.get('userPassword')}) VALUES ('{user.value}', '{email.value}', SHA2('{password.value}' , 512))") == False:
                ui.notify(message = 'You account was created you can go to login . You got a confirmation email .' , position = 'center')
                universalFunctions.sendEmail(email = email.value , subject = 'Account created' , messageSent = f'Your account was created .\nUser : {user.value}\nPassword : {password.value}')
                user.value , email.value , password.value = '' , '' , '' 
            elif universalFunctions.dataBaseQuerys(f"INSERT INTO {os.environ.get('database')} ({os.environ.get('userUser')}, {os.environ.get('userEmail')}, {os.environ.get('userPassword')}) VALUES ('{user.value}', '{email.value}', SHA2('{password.value}' , 512))") == 'Error':
                ui.notify(message = 'Database problems .' , position = 'center')
        if universalFunctions.dataBaseQuerys(f"SELECT * FROM {os.environ.get('database')} WHERE {os.environ.get('userUser')} = '{user.value}'") == 'Error':
            ui.notify(message = 'Database problems .' , position = 'center')