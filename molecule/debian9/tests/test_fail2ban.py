import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_fail2ban_server(host):

    assert host.service('fail2ban').is_enabled
    assert host.service('fail2ban').is_running

    defaults = host.file('/etc/fail2ban/jail.d/defaults-fiaasco.local')
    assert defaults.exists
    assert defaults.contains('a.host.name')
    assert defaults.contains('1.2.3.4/32')

    jails = host.file('/etc/fail2ban/jail.d/jails-fiaasco.local')
    assert jails.exists
