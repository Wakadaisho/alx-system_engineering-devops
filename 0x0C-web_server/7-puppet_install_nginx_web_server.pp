# Install nginx, redirect /redirect_me location to a youtube video

package {'nginx':
  ensure => present
}

file {'/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!
'
}

file_line {'Redirect Me':
  path  => '/etc/nginx/sites-available/default',
  after => '^server',
  line  => 'rewrite ^/redirect_me http://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;'
}

service {'nginx':
  ensure => running,
  enable => true
}
