from os import environ
from fabric.api import *
#from fabric.context_manager import cd
from fabric.contrib.files import sed

"""
Fabrilc file to upload public/private keys to remote servers
and set up non-root users. Also prevents SSH-ing in with the
root user. Run with "fab bootstrap".
"""

# run the bootstrap process as root before it is locked down
env.user = 'root'

# the remote server's root password
env.password = environ.get('TG_ROOT_PWD', None)

# authorized hosts
env.hosts = [environ.get('TG_HOST', None)]

# non-root user details
env.new_user_full_name = 'Magdalena Rother'
env.new_user = 'deployer_mr'
env.new_user_grp = 'deployers'

# local ssh dir
env.ssh_key_dir = '~/.ssh/'


def bootstrap():
    local('ssh-keygen -R {}'.format(env.host_string))
    sed('/etc/ssh/sshd_config', '^UsePAM yes', 'UsePAM no')
    sed('/etc/ssh/sshd_config', '^PermitRootLogin yes', 'PermitRootLogin n0')
    sed('/etc/ssh/sshd_config','^PasswordAuthentication yes', 'PasswordAuthentication no')
    _create_privileged_group()
    _create_privileged_user()
    _upload_keys(env.new_user)
    run('service ssh reload')


def _create_privileged_group():
    run('/usr/sbin/groupadd ' + env.new_user_grp)
    run('mv /etc/sudoers /etc/sudoers-backup')
    run('(cat /etc/sudoers-backup ; echo "%' + env.new_user_gtoup \
            + ' ALL=(ALL) ALL") > /etc/sudoers')
    run('chmod 440 /etc/sudoers')


def _create_priviledge_user():
    run('/usr/sbin/useradd -c "%s" -m -g %s %s' % \
            (env.new_user_full_name, env.new_user_grp, env_user))
    run('/usr/bin/passwd %s' % env.new_user)
    run('/usr/sbin/usermod -a -G ' + env.new_user_grp + ' ' + \
            env.new_user)
    run('mkdir /home/%s/.ssh' % env.new_user)
    run('chown -R %s /home/%s/.ssh' % (env.new_user,
        env.new_user))
    run('chgrp -R %s /home/%s/.ssh' % (env.new_user_grp,
        env.new_user))


def _upload_keys(username):
    local('scp ' + env.ssh_key_dir + \
          '/id_rsa.pub ' + env.ssh_key_dir + \
          '/authorized_keys ' + \
          username + '@' + env.host_string + ':~/.ssh')

