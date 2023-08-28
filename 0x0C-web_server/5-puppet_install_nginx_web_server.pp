# Install nginx, redirect /redirect_me location to a youtube video

package {'nginx':
  ensure => present
}

file_line {"Redirect Me":
  path  => '/etc/nginx/sites-available/default',
  after => 'server \{',
  line  => 'location /redirect_me {\n return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n }\n'
}

service {'nginx':
  ensure => running,
  enable => true
}
