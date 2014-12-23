## NOTE

Pavel Andreev no longer needed this site, so it is no longer accessible, but you still can chechk out contentless version.

## Environment

Install required python packages with

`sudo pip install -r pip-requirments.txt`

## To run project localy perform:

```bash
cd /your_project_path/website/
pyhton manage.py runserver
```

You can go to http://localhost:8000/ and check out current version  
Administration url is http://localhost:8000/damin/

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

Mac OS binaries are missing gettext, so install and link it to make commands above work

```bash
brew install gettext
brew link gettext
```
