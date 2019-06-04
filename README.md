Role Name
=========

Install and configure sshguard service

Parameters
=========

* **sshguard_args** - sshguard parameters
e.g.
```
sshguard__args: -a 5 -p 180 -s 600
```

* **sshguard_whitelist_ip** - list of ip addressed to add to whitelist
e.g.
```
sshguard__whitelist_ip:
- 8.8.8.8
- 129.32.12.31
```

Example Playbook
=========

```
- hosts: all
  roles:
    - role: ansible-role-sshguard
```
