# strace_is_your_friend.
exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/',
  onlyif  => 'grep -q "phpp" /var/www/html/wp-settings.php',
  require => File['/var/www/html/wp-settings.php'],
}

