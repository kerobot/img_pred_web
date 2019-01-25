# img_web

clone

cd img_pred_web

python -m venv venv

activate

python -m pip install --upgrade pip

pip install -r requirements.txt

XXX python manage.py migrate

XXX python manage.py createsuperuser

python manage.py runserver
http://127.0.0.1:8000/admin/

> copy .\.env.sample .\.env
> code .\.env
