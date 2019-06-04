import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_service_enabled(Service):
    service = Service('sshguard')
    assert service.is_enabled

def test_file_exists(File):
    file = File('/etc/sshguard/whitelist')
    assert file.exists
