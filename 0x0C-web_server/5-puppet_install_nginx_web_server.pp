# Install nginx, redirect /redirect_me location to a youtube video

package {'nginx':
  ensure => present
}

file {'/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!
'
}

service {'nginx':
  ensure => running,
  enable => true
}
