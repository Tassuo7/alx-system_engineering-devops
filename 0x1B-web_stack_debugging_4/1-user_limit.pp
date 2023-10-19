# add the holborton user and increase amount of files to open
exec { 'increase-file-limit':
  command => 'sed -i "/holberton5/s/5/8192/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'increase-file-limits':
  command => 'sed -i "/holberton4/s/4/8192/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
