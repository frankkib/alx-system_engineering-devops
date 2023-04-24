# creating a file
$filename = '/tmp'
file { $filename:
  ensure => 'directory'
}

file { '/tmp/school':
  ensure  => 'file',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I Love Puppet',
}
