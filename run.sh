git pull
source v_newehr/bin/activate
pip install -r requirements.txt  # all requirements - gunicorn djang$

python manage.py migrate
python manage.py collectstatic --noinput
sudo systemctl restart ehr
deactivate
