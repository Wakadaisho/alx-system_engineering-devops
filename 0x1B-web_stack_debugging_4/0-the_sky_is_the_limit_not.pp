# Increase number of files limit in nginx

exec {'add_nofile_limit_directive':
  path     => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  command  => '/bin/sed -i "/^worker_processes/a worker_rlimit_nofile 10000;" /etc/nginx/nginx.conf',
}

exec {'restart nginx':
  path     => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  command  => 'kill `ps -C nginx fch -o pid | head -1` && nginx',
}
