### Runserver
python manage.py runserver --settings=core.settings.dev                     <br/>

<!-- common commands -->
python manage.py makemigrations --settings=core.settings.dev                <br/>
python manage.py migrate --settings=core.settings.dev                       <br/>
python manage.py createsuperuser --settings=core.settings.dev               <br/>

## CONFIGURATION (important)    

JWT_SECRET_KEY = "your-secret-key"          <br/>

#Email Config                               <br/>
EMAIL_BACKEND = " "                         <br/>
EMAIL_HOST = " "                            <br/>
EMAIL_PORT = " "                            <br/>
EMAIL_USE_SSL = True                        <br/>
EMAIL_HOST_USER = " "                       <br/>
EMAIL_HOST_PASSWORD = " "                   <br/>
DEFAULT_FROM_EMAIL = " "                    <br/>