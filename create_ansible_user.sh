#!/bin/bash
[[ $1 == */authorized_keys ]] || { echo "Provide authorized_keys file" ; exit ; }
sudo useradd -m -s /sbin/nologin ansible
sudo usermod -aG sudo ansible
[[ $(whoami) == root ]] || sudo usermod -aG ansible "$(whoami)"
echo "ansible ALL=(ALL) NOPASSWD: ALL" | sudo tee -a /etc/sudoers
sudo install -m 640 -o ansible -g ansible -D -t /home/ansible/.ssh "$1"
cat /home/ansible/.ssh/authorized_keys
