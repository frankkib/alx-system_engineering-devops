class { 'nginx':
  worker_processes        => auto,
  worker_connections      => 2048,
  multi_accept            => 'on',
  sendfile                => 'on',
  tcp_nopush              => 'on',
  tcp_nodelay             => 'on',
  keepalive_timeout       => 65,
  client_max_body_size    => '8m',
  client_body_buffer_size => '128k',
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Class['nginx'],
  notify  => Service['nginx'],
}
