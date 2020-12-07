#kills the program killmenow

exec { 'pkill':
  command => 'pkill -f killmenow',
  path    => '/usr/local/bin/',
  }
