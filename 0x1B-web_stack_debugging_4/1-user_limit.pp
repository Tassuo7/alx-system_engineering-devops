# add the holborton user and increase amount of files to open
exec { 'increase-file-limit':
  command => 'sudo sed -i "/holberton hard/s/5/8192/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'increase-file-limits2':
  command => 'sudo sed -i "/holberton hard/s/4/8192/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
