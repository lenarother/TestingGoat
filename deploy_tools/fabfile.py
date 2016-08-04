import os
import random

from fabric.contrib.files import append, exists, sed
from fabric.api import env, local, run

REPO_URL = 'https://github.com/lenarother/TestingGoat.git'


def deploy():
    # repository level, this folder contains django project
    # deployment tools, docmentation
    # and non-repository folders: static, database, virtualenv
    site_folder = os.path.join('/home', env.user, 'sites', env.host)
    # django project level, this folder contains manage.py
    project_folder = os.path.join(site_folder, 'superlists')
    _get_latest_source(site_folder)
    _update_settings(project_folder, env.host)
    _update_virtualenv(site_folder)
    _update_static_files(project_folder)
    _update_database(project_folder)


def _get_latest_source(site_folder):
    if exists(os.path.join(site_folder, '.git')):
        run('cd {} $$ git fetch'.format(site_folder))
        print('Fetched')
    else:
        run('git clone {} {}'.format(REPO_URL, site_folder))
    current_commit = local("git log -n 1 --format=%H", capture=True)
    print(current_commit)
    print(type(current_commit))
    run('cd {} && git reset --hard'.format(site_folder))


def _update_settings(project_folder, site_name):
    settings_path = os.path.join(project_folder, 'superlists', 'settings.py')
    sed(settings_path, "DEBUG = True", "DEBUG = False")
    sed(settings_path,
        'ALLOWED_HOSTS = .+$',
        'ALLOWED_HOSTS = [{}]'.format(site_name)
    )
    secret_key_file = os.path.join(project_folder, 'superlists', 'secret_key.py')
    if not exists(secret_key_file):
        chars = 'abcdefghijklmnopqrstuwxyz0123456789!@#$%^&*(-_=+)'
        key = ''.join(random.SystemRandom().choice(chars) for _ in range(50))
        append(secret_key_file, "SECRET_KEY = '{}'".format(key))
    append(settings_path, '\nfrom .secret_key import SECRET_KEY')


def _update_virtualenv(site_folder):
    venv_folder = os.path.join(site_folder, 'virtualenv')
    if not exists(os.path.join(venv_folder, 'bin', 'pip')):
        run('virtualenv --python=python3 {}'.format(venv_folder))
    run('{}/bin/pip install -r {}/requirements.pip'.format(venv_folder, site_folder))


def _update_static_files(project_folder):
    run('cd {} && ../virtualenv/bin/python3 manage.py collectstatic --noinput'.format(project_folder))


def _update_database(project_folder):
    db_folder = os.path.join(project_folder, '..', 'database')
    if not exists(db_folder):
        run('mkdir -p {}'.format(db_folder))
    run('cd {} && ../virtualenv/bin/python3 manage.py migrate --noinput'.format(project_folder))
