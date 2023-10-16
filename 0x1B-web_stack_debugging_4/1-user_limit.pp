# Remove file limits for user holberton

# Remove nofile limits
exec {'remove_holberton_limits':
  command     => '/bin/sed -i s/^holberton/# holberton/g /etc/security/limits.conf',
}
