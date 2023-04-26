#setting up nginx


package { 'nginx':
  ensure => installed,
}

file { '/etc/nginx/sites-available/default':
  content => template('nginx/default.conf.erb'),
  notify  => Service['nginx'],
}
file { '/etc/nginx/sites-enabled/default':
  ensure => 'link',
  target => '/etc/nginx/sites-available/default',
  notify => Service['nginx'],
}

file { '/var/www/html/index.html':
  content => "Hello World!\n",
  notify  => Service['nginx'],
}
service { 'nginx':
  ensure => 'running',
  enable => true,
}
server {
    listen 80;

    root /var/www/html;
    index index.html;

    location /redirect_me {
        return 301 /new_location;
    }

    location /new_location {
        return 200 'This page has moved permanently.';
    }

    location / {
        if ($request_method = 'GET') {
            return 200 'Hello World!';
        }
    }
}
