# Install nginx, redirect /redirect_me location to a youtube video, add header

package {'nginx':
  ensure => present
}

file_line {'X-Served-By header':
  path  => '/etc/nginx/sites-available/default',
  after => '^server',
  line  => '	add_header X-Served-By $hostname;'
}

service {'nginx':
  ensure => running,
  enable => true
}
