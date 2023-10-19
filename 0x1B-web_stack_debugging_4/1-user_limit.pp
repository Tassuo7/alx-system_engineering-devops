# add the holborton user and increase amount of files to open
exec { 'increase-file-limit':
  provider => shell,
  command => 'sudo sed -i "s/nofile 5/nofile 50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'increase-file-limits2':
  command => 'sudo sed -i "s/nofile 4/nofile 40000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
