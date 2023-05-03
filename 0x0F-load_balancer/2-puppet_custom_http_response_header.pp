# HTTP response
exec { 'command'
  command  => 'sudo apt-get -y update;
  sudo apt-get -y nginx;
  sudo sed i "/listen 80 default_server;/add_headerX-served-By $HOSTNAME;" /etc/nginx/sites-available/default; 
  sudo `service nginx restart',
  provider => shell,
}
