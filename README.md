

python3 manage.py runserver
- run app
http://127.0.0.1:8000


python3 manage.py startapp products
- initialize a new django package


every time we want to create new views function:
views module => create new function
in urls module => create path to new apps urls file
in new apps urls file => define new urlpattern to map new function to url end point

db.sqlite3 - use DB Browser to open
basic database file
settings.py => installed_apps => add complete path to modules apps ProductsConfig class
python3 manage.py makemigrations
=> migrations folder created in app/module
python3 manage.py migrate
load db.sqlite3 file in db browser - database created


create Offer
    - offer text field, coupon code (VCA2142)
    - description (20% off all products)
    - discount, floating point number (0.2)


http://127.0.0.1:8000/admin/login/?next=/admin/
administration login screen
create superuser
python3 manage.py createsuperuser
admin

login => manage users and groups in administrative panel

