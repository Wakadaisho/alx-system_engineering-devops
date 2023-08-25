# Configure ssh config file to connect to a server without a password

file {'/home/ubuntu/.ssh':
  ensure => 'directory',
  owner => 'ubuntu',
  group => 'ubuntu',
}

file {'/home/ubuntu/.ssh/config':
  ensure => 'file',
  owner => 'ubuntu',
  group => 'ubuntu',
  content => 'Host alx_web_01
	HostName 100.26.165.122
	User ubuntu
	PasswordAuthentication no
	IdentityFile ~/.ssh/school
	ServerAliveInterval 15
	ServerAliveCountMax 3
'
}
