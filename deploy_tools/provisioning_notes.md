Provistioning a vew site
========================

## Required packages:

* nginx
* Python 3
* Git
* pip
* vitualenv

eg, on Ubuntu:

```
  sudo apt-get install nginx git python3 python3-pip
  sudo pip3 install virtualenv
```

## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with, eg, staging.my-domain.com

## Upstart job

* see gunicorn-upstart.template.conf
* replace SITENAME with eg, staging.my-domain.com

## Folder structure:
Assume we have a user account at /home/username

/home/username
|__ sites
    |__ SITENAME
        |__ database --> python manage.py migrate
        |__ superlists --> code
        |__ static --> python manage.py collectstatic
        |__ virtualenv

