import smtplib , ssl , mysql.connector , main , os , sys
from nicegui import ui
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
load_dotenv(dotenv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)) , '.env'))
db_config = {
    'host': os.environ.get('host'),
    'user': os.environ.get('user'),
    'password': os.environ.get('password'),
    'database': os.environ.get('database'),
}
def get_executable_directory():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.abspath(sys.argv[0]))
def sendEmail(email  , subject ,  messageSent):
    gmail_user = os.environ.get('gmail')
    app_password = os.environ.get('gmailPassword')
    message = MIMEMultipart()
    message["From"] = gmail_user
    message["To"] = email
    message["Subject"] = subject
    message.attach(MIMEText(messageSent, "plain"))
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(gmail_user, app_password)
        server.sendmail(gmail_user, email, message.as_string())
def goToPage(page):
    ui.run_javascript(f'''
                        window.location.href = "http://127.0.0.1:8080/{page}"
                    ''')
def dataBaseQuerys(query):
    try:
        connection = mysql.connector.connect(
            host = os.environ.get('host'),
            user = os.environ.get('user'),
            password = os.environ.get('password'),
            database = os.environ.get('database')
        )
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        connection.commit()
        if result is not None and len(result) > 0:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error: {e}")
        return 'Error'