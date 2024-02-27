from nicegui import ui
import random , string
from Functions import universalFunctions
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)) , '.env'))
def randomPassword():
    all_possible_chars = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(random.choice(all_possible_chars) for _ in range(8))
    return random_string
def resetPassword(email, user):
    newPassword = randomPassword()
    if universalFunctions.dataBaseQuerys(f"SELECT * FROM {os.environ.get('database')} WHERE {os.environ.get('userEmail')} = '{email.value}' AND {os.environ.get('userUser')} = '{user.value}'") == True:
        universalFunctions.dataBaseQuerys(f"UPDATE {os.environ.get('database')} SET {os.environ.get('userPassword')} = SHA2('{newPassword}', 512) WHERE {os.environ.get('userEmail')} = '{email.value}' AND {os.environ.get('userUser')} = '{user.value}'")
        universalFunctions.sendEmail(email = email.value , subject = 'Recover Password' , messageSent = f'Password for the account {user.value} was reseted .\n New password : {newPassword}')
        email.value , user.value = '' , ''
        ui.notify(message = 'Password was reseted , check your email .' , position = 'center')
    elif universalFunctions.dataBaseQuerys(f"SELECT * FROM {os.environ.get('database')} WHERE {os.environ.get('userEmail')} = '{email.value}' AND {os.environ.get('userUser')} = '{user.value}'") == False:
        ui.notify(message = 'User or email are incorect .' , position = 'center')
    elif universalFunctions.dataBaseQuerys(f"SELECT * FROM {os.environ.get('database')} WHERE {os.environ.get('userEmail')} = '{email.value}' AND {os.environ.get('userUser')} = '{user.value}'") == 'Error' :
        ui.notify(message = 'Databaseproblems .' , position = 'center')