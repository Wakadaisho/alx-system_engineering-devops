# Kill the process killmenow

exec { 'pkill -f killmenow':
  path => ['/usr/bin', '/usr/sbin', '/bin']
}
