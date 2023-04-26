# creating a file
file { '/tmp':
  require => File['/tmp/school'],
}
file { '/tmp/school':
  ensure  => 'file',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I Love Puppet',
}
