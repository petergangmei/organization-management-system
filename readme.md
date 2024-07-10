# Welcome & Thank you for checking out!

Visit demo page: https://organization-management-system-ten.vercel.app/

## CONFIGURATION (important)    
JWT_SECRET_KEY = "your-secret-key"          <br/><br/>

#Email Config                               <br/>
EMAIL_BACKEND = " "                         <br/>
EMAIL_HOST = " "                            <br/>
EMAIL_PORT = " "                            <br/>
EMAIL_USE_SSL = True                        <br/>
EMAIL_HOST_USER = " "                       <br/>
EMAIL_HOST_PASSWORD = " "                   <br/>
DEFAULT_FROM_EMAIL = " "                    <br/>

#AWS Config
AWS_ACCESS_KEY_ID = ''                      <br/>
AWS_SECRET_ACCESS_KEY = ''                  <br/><br/>

AWS_REGION_NAME = ''                        <br/>
AWS_STORAGE_BUCKET_NAME = ''                <br/>


## Additionals help!
### Some basic command 
python manage.py runserver --settings=core.settings.dev                     <br/>

<!-- common commands -->
python manage.py makemigrations --settings=core.settings.dev                <br/>
python manage.py migrate --settings=core.settings.dev                       <br/>
python manage.py createsuperuser --settings=core.settings.dev               <br/>