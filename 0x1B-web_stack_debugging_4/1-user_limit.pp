# debugging task #1
exec { 'fix_hardlimit':
  path    => ['/usr/bin/', '/bin/'],
  command => 'sed -i "56c holberton hard nofile 1048576" /etc/security/limits.conf',
}
exec { 'fix_softlimit':
  path    => ['/usr/bin/', '/bin/'],
  command => 'sed -i "57c holberton soft nofile 1048576" /etc/security/limits.conf',
}
