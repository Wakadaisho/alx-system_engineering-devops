# Configure ssh config file to connect to a server without a password

file_line { 'SSH_IdentityFile':
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school'
}

file_line { 'SSH_PasswordAuthentication':
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no'
}
