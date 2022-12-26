from os import environ
from dotenv import load_dotenv, find_dotenv

dotenv_path = find_dotenv()

load_dotenv(dotenv_path, override=False)

load_dotenv()

AWS_ACCESS_KEY = environ.get('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')
AWS_BUCKET_NAME = environ.get('AWS_BUCKET_NAME')
AWS_PROJECT_NAME = environ.get('AWS_PROJECT_NAME')
AWS_REGION = environ.get('AWS_REGION')
AWS_BUCKET_ENDPOINT = environ.get('AWS_BUCKET_ENDPOINT')


# Configurações Gerais
class Config:
    
    # Agendador de Tarefas
    SCHEDULER_API_ENABLED = True

    # Validacoes de senha 
    possiblePasswordErrors = ["", None]
    MINIMUM_PASWORD_LENGHT = 8


    # Tempo maximo de validade do pin de troca de senha, em minutos
    VALID_VERIFICATION_PIN_TIME = 5


    # Configuracoes flask e sql 
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    
    # Configs JWT
    JWT_SECRET_KEY = environ.get("JWT_SECRET_KEY")


    # Configuracoes email
    #EMAIL = environ.get("EMAIL")

    MAIL_SERVER = environ.get("MAIL_SERVER")
    MAIL_PORT = environ.get("MAIL_PORT")
    MAIL_USERNAME = environ.get("MAIL_USERNAME")
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False

    MAIL_PASSWORD = environ.get("MAIL_PASSWORD")

    HOST_FTP = environ.get("HOST_FTP")
    USER_FTP = environ.get("USER_FTP")
    PASS_FTP = environ.get("PASS_FTP")
