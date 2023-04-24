# Installing flask
package { 'Flask':
  ensure   => '2.10',
  name     => 'flask',
  provider => 'pip3',
}
