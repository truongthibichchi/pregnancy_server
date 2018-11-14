# pregnancy_server
1) Install MySql: https://dev.mysql.com/downloads/mysql/
2) Create database: pregnacy_summary_infos.sql
3) Setting database: /configs/settings.py: 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': '<your password>',
        'NAME': 'pregnancy',
    }
}
