# add the holborton user and increase amount of files to open
exec { 'increase-hard-file-limit':
  command => 'sudo sed -i "/holberton hard/s/5/8192/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'increase-soft-file-limit':
  command => 'sudo sed -i "/holberton hard/s/4/8192/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
