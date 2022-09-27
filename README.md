# configure_vm
## Pipeline for generic vm configuration

## Creating ansible central node
pipeline: `configure_ansible_control_node.yml` </br>

**Please do not use `"` in passwords. I have no idea how to escape them in passwords** </br>
Works for Ubuntu 20.04 lts </br>
Azure environment have to be install by the user that is in sudoers. Do `apt update & upgrade` first. Nothing else is needed </br>
Please override passwords variables in the pipeline run. </br>
`ansible` user will be created. It's public ssh key for ansible hosts is show in the last pipeline step
