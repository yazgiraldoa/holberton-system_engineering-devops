# Use strace to find an error
exec { 'fix_apache_error':
    command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php; sudo service apache2 restart',
    path    => ['/bin', '/usr/bin', '/usr/sbin']
}
