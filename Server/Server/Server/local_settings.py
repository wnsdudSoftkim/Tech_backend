import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATABASES  = {
    'default': {
        'ENGINE'   : 'django.db.backends.mysql',
        'NAME'     : 'mydb',
        'USER'     : 'jun',
        'PASSWORD' : 'tjdnftkfka0501',
        'HOST'     : 'jun.co60jiy75jrv.ap-northeast-2.rds.amazonaws.com',
        'OPTIONS': {'charset': 'utf8mb4'},
        'PORT'     :'3306', 
    }
}	
DEBUG = True