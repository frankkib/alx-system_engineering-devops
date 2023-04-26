# killing command using puppet
exec { 'killmenow':
  command => '/usr/bin/pkill killmenow',
  path    => '/usr/bin',
  onlyif  => '/usr/bin/pgrep killmenow',
}
