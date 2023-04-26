#setting up nginx


package { 'nginx':
  ensure => installed,
}

  # Create Nginx server block
file { '/etc/nginx/sites-available/default':
  content => template('nginx/default.conf.erb'),
  notify  => Service['nginx'],
}

#       # Enable Nginx server block
file { '/etc/nginx/sites-enabled/default':
  ensure => 'link',
  target => '/etc/nginx/sites-available/default',
  notify => Service['nginx'],
}

#             # Create index.html file
  file { '/var/www/html/index.html':
  content => "Hello World!\n",
  notify  => Service['nginx'],
}
          # Define Nginx service
  service { 'nginx':
  ensure => 'running',
  enable => true,
}
