# This is repository for Pavel Andreev website

## Environment

Install required python packages with

`sudo pip install -r pip-requirments.txt`

## To run project localy cd to andreev_ru and run

```
cd website
pyhton manage.py runserver
```

You can go to http://localhost:8000/admin and check out administration interface

## Database

For now we will use local database to sync all changes via git
Credentials are:
```
username: admin
password: password
```

## Update and Modify Locale Strings

To update all translatable strings, perform this:

```bash
cd /your_project_path/website/andreev_ru/main
django-admin.py makemessages --all
```

This will updates `django.po` for each locale in main project's locale folder

To compile all messages, run

```bash
cd /your_project_path/website/andreev_ru/main
django-admin.py compilemessages
```

### Mac OS X hint

Mac OS binaries are missing gettesx, so install and link it to make commands above work

```bash
brew install gettext
brew link gettext
```
