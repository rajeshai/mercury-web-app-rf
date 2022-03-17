import django_heroku
ALLOWED_HOSTS = ['*','mercury-ml-web-app.herokuapp.com','https://mercury-ml-web-app.herokuapp.com/', 'http://mercury-ml-web-app.herokuapp.com/',
                '127.0.0.1',
                'https://mercury-ml-web-app.herokuapp.com',
                'http://mercury-ml-web-app.herokuapp.com']
django_heroku.settings(locals())
