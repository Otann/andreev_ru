# This is repository for Pavel Andreev website

## Environment

Check all installed packages with `sudo pip freeze`
Install missing ones with `sudo pip install <package_name>`
Here is required list:

```
ipython
django-modeltranslation
markdown2
pytils
django-imaging
```

## To run project localy cd to andreev_ru and run

```
pyhton manage.py runserver
```

You can go to http://localhost:8000/admin and check out administration interface

## Database

For now we will use local database to sync all changes via git
Credentials are:
```
username: root
password: password
```