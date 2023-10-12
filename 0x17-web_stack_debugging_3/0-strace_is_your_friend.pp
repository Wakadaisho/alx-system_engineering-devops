# Fix typo in Wordpress config and restart the Apache server

# correct phpp typo
exec {'fix_typo_in_wordpress_config':
  command     => '/bin/sed -i s/phpp/php/g /var/www/html/wp-settings.php',
}
