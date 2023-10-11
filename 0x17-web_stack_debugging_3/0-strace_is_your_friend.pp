# Fix typo in Wordpress config and restart the Apache server

# correct phpp typo
exec {'fix_typo_in_wordpress_config':
  command     => '/bin/sed -i s/phpp/php/g /var/www/html/*.php',
  refreshonly => true
}

# Service resource to ensure apache2 is restarted and running
service {'apache2':
  ensure  => running,
  enable  => true,
  require => Exec['fix_typo_in_wordpress_config']
}
