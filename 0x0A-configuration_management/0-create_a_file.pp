#this function creates the file
  file { '/tmp/holberton':
  ensure  => 'present',
  owner   => 'www-data',
  group   => 'www-data',
  content => "I love Puppet\n",
  mode    => '0744',
  }
