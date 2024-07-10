#!bin/bash

#Build project

python3.9 -m pip install -r requirements.txt

python3.9 manage.py makemgirations --noinput
python3.9 manage.py migrate --noinput

# python3.9 manage.py collectstatic --noinput