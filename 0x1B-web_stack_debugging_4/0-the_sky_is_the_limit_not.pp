# Increment the number of file descriptors per worker
exec { 'add_file_descriptors':
    command => 'sed -i s/15/1500/g /etc/default/nginx; sudo service nginx restart',
    path    => ['/bin', '/usr/bin', '/usr/sbin']
}
