# killing command using puppet
exec { 'killmenow':
  command => 'pkill killmenow'
}
