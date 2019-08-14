# create a custom HTTP header response

package { 'nginx':
  ensure => installed,
  name   => 'nginx',
}

file_line { 'header':
  ensure   => present,
  path     => '/etc/nginx/sites-available/default',
  after    => 'server_name _;',
  line     => 'add_header X-Served-By "$HOSTNAME";',
  multiple => true
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
