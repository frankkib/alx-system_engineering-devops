# Create 'holberton' user
user { 'holberton':
  ensure => present,
  shell  => '/bin/bash',
}

file { '/etc/ssh/sshd_config':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => template('module/sshd_config.erb'),
  notify  => Service['sshd'],
}

service { 'sshd':
  ensure => running,
  enable => true,
}

